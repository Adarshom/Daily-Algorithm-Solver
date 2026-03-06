# Daily-Algorithm-Solver

This repository automatically generates and stores one Data Structures and Algorithms (DSA) solution every day using the Gemini API and GitHub Actions. The automation runs daily, generates a Python solution to a LeetCode-style problem, and commits the result directly to the repository.

The project demonstrates a fully automated pipeline that integrates prompt-driven AI code generation with scheduled GitHub workflows.

## Overview

Each day the following process occurs:

1. GitHub Actions triggers the workflow based on a scheduled cron job.
2. The workflow runs a Python script.
3. The script selects the appropriate prompt from a list of algorithm problems.
4. The prompt is sent to the Gemini API.
5. Gemini generates a Python solution.
6. The solution is saved to the repository under the solutions directory.
7. The workflow commits and pushes the new file to the main branch.

The system runs indefinitely and continues generating new solutions each day.

## Repository Structure

```

Daily-Algorithm-Solver/
│
├── README.md
├── requirements.txt
├── leetcode_365_prompts.txt
│
├── scripts/
│   └── generate_daily_solution.py
│
├── solutions/
│   ├── Day_001.py
│   ├── Day_002.py
│   ├── Day_003.py
│   └── ...
│
└── .github/
└── workflows/
└── daily-dsa.yml

```

## Prompt Source

Algorithm prompts are stored in the file:

```

leetcode_365_prompts.txt

```

Each line contains a prompt describing a LeetCode-style problem. The script reads one prompt per day. If the day count exceeds the number of prompts available, the prompts cycle from the beginning.

Example prompt format:

```

Day 1: Solve the LeetCode-style problem 'Two Sum'. Return a clean Python solution with optimal time complexity.

```

## Daily Workflow

The automation runs through GitHub Actions using the workflow:

```

.github/workflows/daily-dsa.yml

```

The workflow is triggered using the cron schedule:

```

23 2 * * *

```

GitHub cron schedules operate in UTC.

This corresponds to the following execution time:

| Timezone | Execution Time |
|----------|----------------|
| UTC | 02:23 |
| IST | 07:53 |

The workflow runs once per day.

## AI Model

The system uses the Gemini API for code generation.

Model used:

```

gemini-2.5-flash

```

This model is suitable for code generation tasks such as algorithm implementation and programming problem solving.

## Generated Output

Solutions are saved in the directory:

```

solutions/

```

File naming follows the pattern:

```

Day_XXX.py

```

Examples:

```

Day_001.py
Day_002.py
Day_003.py

```

The numbering continues indefinitely.

## Day Number Calculation

The day number is calculated relative to a configurable start date defined by the environment variable:

```

START_DATE

```

Example:

```

START_DATE=2026-03-06

```

The calculation used:

```

Day = (Current Date - START_DATE) + 1

```

Example progression:

| Date | Generated File |
|------|----------------|
| March 6 | Day_001.py |
| March 7 | Day_002.py |
| March 8 | Day_003.py |

The counter continues indefinitely.

## Safety Behavior

Before generating a new solution, the script checks if the file for the current day already exists.

Example:

```

solutions/Day_005.py

```

If the file exists, the script exits without generating a new solution and the workflow completes without committing changes.

This prevents duplicate generation.

## Requirements

The project requires Python 3.11 and the following dependency:

```

google-genai

```

Install dependencies with:

```

pip install -r requirements.txt

```

## Gemini API Configuration

Create a Gemini API key from:

```

[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

```

Add the key to the repository secrets.

Repository settings:

```

Settings → Secrets and variables → Actions

```

Create a secret:

```

GEMINI_API_KEY

```

The workflow reads this secret when calling the Gemini API.

## GitHub Actions Configuration

Ensure the following repository settings are enabled.

Enable Actions:

```

Settings → Actions → Allow all actions and reusable workflows

```

Enable workflow write permissions:

```

Settings → Actions → Workflow permissions → Read and write

```

These permissions allow the workflow to commit generated solutions.

## Example Generated Solution

Example generated file:

```

solutions/Day_001.py

````

Example structure:

```python
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
````

## License

MIT License
