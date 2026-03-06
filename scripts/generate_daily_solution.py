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
    Reads START_DATE from env in YYYY-MM-DD format.
    Example: 2026-03-06
    """
    start_date_str = os.environ.get("START_DATE", "2026-03-06").strip()
    try:
        return datetime.strptime(start_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc).date()
    except ValueError as exc:
        raise ValueError(
            f"Invalid START_DATE='{start_date_str}'. Expected format: YYYY-MM-DD"
        ) from exc


def calculate_day_number() -> int:
    """
    Calculates project-relative day number:
    Day 1 on START_DATE, Day 2 the next day, etc.
    Wraps after 365.
    """
    start_date = get_start_date()
    today = datetime.now(timezone.utc).date()

    day = (today - start_date).days + 1
    if day < 1:
        day = 1
    elif day > 365:
        day = ((day - 1) % 365) + 1

    return day


def load_prompts() -> list[str]:
    if not PROMPTS_FILE.exists():
        raise FileNotFoundError(f"Prompt file not found: {PROMPTS_FILE}")

    prompts = [line.strip() for line in PROMPTS_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]

    if len(prompts) < 365:
        raise ValueError(
            f"Expected at least 365 non-empty lines in {PROMPTS_FILE}, found {len(prompts)}"
        )

    return prompts


def get_prompt_for_day(day: int, prompts: list[str]) -> str:
    return prompts[day - 1]


def extract_problem_title(prompt: str, day: int) -> str:
    """
    Tries to extract a quoted title from prompt, e.g.
    Day 1: Solve the LeetCode-style problem 'Two Sum'. ...
    Falls back safely if not found.
    """
    match = re.search(r"'([^']+)'", prompt)
    if match:
        return match.group(1).strip()
    return f"Day {day} Problem"


def get_output_file(day: int) -> Path:
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    return SOLUTIONS_DIR / f"Day {day}.py"


def build_model_prompt(prompt: str, day: int, title: str) -> str:
    return f"""
You are an expert Python DSA and LeetCode solver.

Solve the following problem and return ONLY valid Python code.

Hard requirements:
1. Output ONLY Python code. No markdown. No backticks. No prose outside Python comments.
2. Use a LeetCode-style structure:
   - define `class Solution`
   - implement the expected method for the problem
3. Add brief comments explaining the core logic.
4. Include a small `if __name__ == "__main__":` block with 2-3 sample test cases.
5. Keep the solution efficient and clean.
6. Use standard library only.
7. Do not include placeholders like "your code here".
8. Make the code runnable as a standalone Python file.

Metadata:
- Day: {day}
- Problem title: {title}

Prompt:
{prompt}
""".strip()


def generate_code(api_key: str, model: str, prompt: str) -> str:
    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "temperature": 0.2,
            },
        )
    except ClientError as exc:
        message = str(exc)
        if "RESOURCE_EXHAUSTED" in message or "429" in message:
            print("Gemini quota exhausted or rate limited. Skipping this run gracefully.")
            sys.exit(0)
        raise

    text = (response.text or "").strip()
    if not text:
        raise RuntimeError("Gemini returned empty output")

    # Clean accidental code fences if model returns them anyway
    text = text.replace("```python", "").replace("```", "").strip()

    if not text:
        raise RuntimeError("Gemini output became empty after cleanup")

    return text + "\n"


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY environment variable")

    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash").strip()
    if not model:
        model = "gemini-2.5-flash"

    day = calculate_day_number()
    prompts = load_prompts()
    prompt = get_prompt_for_day(day, prompts)
    title = extract_problem_title(prompt, day)
    output_file = get_output_file(day)

    print(f"Calculated day: {day}")
    print(f"Using model: {model}")
    print(f"Output file: {output_file}")

    if output_file.exists():
        print(f"Solution already exists for Day {day}: {output_file}")
        sys.exit(0)

    final_prompt = build_model_prompt(prompt, day, title)
    code = generate_code(api_key=api_key, model=model, prompt=final_prompt)

    output_file.write_text(code, encoding="utf-8")
    print(f"Generated solution written to: {output_file}")


if __name__ == "__main__":
    main()
