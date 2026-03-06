import os
from datetime import datetime, timezone
from pathlib import Path

from google import genai


def day_index_1_to_365(now_utc: datetime) -> int:
    # Day-of-year (1..366), wrap to 1..365
    doy = now_utc.timetuple().tm_yday
    return ((doy - 1) % 365) + 1


def read_prompt_line(prompts_file: Path, idx_1_based: int) -> str:
    lines = prompts_file.read_text(encoding="utf-8").splitlines()
    if len(lines) < 365:
        raise ValueError(f"Expected 365 lines in {prompts_file}, found {len(lines)}")
    return lines[idx_1_based - 1].strip()


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY env var")

    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    now_utc = datetime.now(timezone.utc)
    idx = day_index_1_to_365(now_utc)

    repo_root = Path(__file__).resolve().parents[1]
    prompts_file = repo_root / "leetcode_365_prompts.txt"
    prompt = read_prompt_line(prompts_file, idx)

    # Output path with the exact naming scheme requested
    out_dir = repo_root / "solutions"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"Day {idx}.py"

    system = (
        "You are an expert competitive programmer.\n"
        "Return ONLY valid Python code.\n"
        "No markdown. No backticks. No explanations outside comments.\n"
        "Use LeetCode style: class Solution with the expected method.\n"
        "Include a small self-test under if __name__ == '__main__': with 2–3 cases.\n"
    )

    client = genai.Client(api_key=api_key)

    resp = client.models.generate_content(
        model=model,
        contents=system + "\n\n" + prompt,
        config={
            "temperature": 0.2,
        },
    )

    code = (resp.text or "").strip()
    if not code:
        raise RuntimeError("Empty model response")

    # Basic safety: ensure it's python-ish and not markdown
    if "```" in code:
        code = code.replace("```python", "").replace("```", "").strip()

    out_file.write_text(code + "\n", encoding="utf-8")
    print(f"Wrote: {out_file}")


if __name__ == "__main__":
    main()