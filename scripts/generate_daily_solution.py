import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from google import genai
from google.genai.errors import ClientError


REPO_ROOT = Path(__file__).resolve().parents[1]
PROMPTS_FILE = REPO_ROOT / "leetcode_365_prompts.txt"
SOLUTIONS_DIR = REPO_ROOT / "solutions"


def get_start_date() -> datetime.date:
    """
    Reads START_DATE from environment variable.
    Default fallback if not provided.
    """
    start_date_str = os.environ.get("START_DATE", "2026-03-06").strip()

    try:
        return datetime.strptime(start_date_str, "%Y-%m-%d").replace(
            tzinfo=timezone.utc
        ).date()
    except ValueError:
        raise ValueError(
            f"Invalid START_DATE '{start_date_str}'. Expected format YYYY-MM-DD"
        )


def calculate_day_number() -> int:
    """
    Calculates project-relative day number starting from START_DATE.
    Continues indefinitely (Day 1, Day 2, Day 3 ... Day 1000 etc).
    """
    start_date = get_start_date()
    today = datetime.now(timezone.utc).date()

    day = (today - start_date).days + 1

    if day < 1:
        day = 1

    return day


def load_prompts() -> list[str]:
    if not PROMPTS_FILE.exists():
        raise FileNotFoundError(f"Prompt file not found: {PROMPTS_FILE}")

    prompts = [
        line.strip()
        for line in PROMPTS_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    if len(prompts) < 365:
        raise ValueError(
            f"Expected at least 365 prompts in {PROMPTS_FILE}, found {len(prompts)}"
        )

    return prompts


def get_prompt_for_day(day: int, prompts: list[str]) -> str:
    """
    Cycles through prompts if day > 365
    """
    index = (day - 1) % len(prompts)
    return prompts[index]


def extract_problem_title(prompt: str, day: int) -> str:
    """
    Attempts to extract problem title from prompt.
    Example:
    Day 1: Solve the LeetCode-style problem 'Two Sum'
    """
    match = re.search(r"'([^']+)'", prompt)
    if match:
        return match.group(1).strip()

    return f"Day {day} Problem"


def get_output_file(day: int) -> Path:
    """
    Returns the output file path.
    Example:
    solutions/Day_001.py
    solutions/Day_017.py
    solutions/Day_123.py
    """
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    return SOLUTIONS_DIR / f"Day_{day:03d}.py"


def build_model_prompt(prompt: str, day: int, title: str) -> str:
    """
    Builds the final prompt sent to Gemini.
    """
    return f"""
You are an expert Python DSA and LeetCode solver.

Solve the following problem and return ONLY valid Python code.

Requirements:
1. Output ONLY Python code.
2. Do NOT include markdown or backticks.
3. Use a LeetCode-style solution:
   - define class Solution
   - implement the correct function
4. Include short comments explaining the logic.
5. Include a small test block:

if __name__ == "__main__":

with 2–3 example cases.

Metadata:
Day: {day}
Problem: {title}

Prompt:
{prompt}
""".strip()


def generate_code(api_key: str, model: str, prompt: str) -> str:
    """
    Calls Gemini API to generate the solution code.
    """
    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config={"temperature": 0.2},
        )
    except ClientError as e:
        message = str(e)

        if "RESOURCE_EXHAUSTED" in message or "429" in message:
            print("Gemini quota exhausted. Skipping today's generation.")
            sys.exit(0)

        raise

    text = (response.text or "").strip()

    if not text:
        raise RuntimeError("Gemini returned empty output")

    # Remove accidental code fences
    text = text.replace("```python", "").replace("```", "").strip()

    return text + "\n"


def main():
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY environment variable")

    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

    day = calculate_day_number()

    prompts = load_prompts()
    prompt = get_prompt_for_day(day, prompts)
    title = extract_problem_title(prompt, day)

    output_file = get_output_file(day)

    print(f"Day number: {day}")
    print(f"Model: {model}")
    print(f"Output file: {output_file}")

    if output_file.exists():
        print(f"Solution already exists for Day {day}. Skipping.")
        sys.exit(0)

    final_prompt = build_model_prompt(prompt, day, title)

    code = generate_code(
        api_key=api_key,
        model=model,
        prompt=final_prompt,
    )

    output_file.write_text(code, encoding="utf-8")

    print(f"Solution generated: {output_file}")


if __name__ == "__main__":
    main()
