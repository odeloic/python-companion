# Python Companion

A collaborative space for practicing Python — work through exercises, get AI-assisted feedback, and sharpen your understanding of core concepts, all from the terminal.

## Prerequisites

- [Claude Code](https://claude.ai/code) (subscription required) — the CLI that powers the slash commands below
- Python 3.10+

## Python environment setup

**macOS / Linux**

Check if Python 3.10+ is already installed:

```bash
python3 --version
```

If not, install it via [pyenv](https://github.com/pyenv/pyenv) (recommended) or your system package manager:

```bash
# macOS (Homebrew)
brew install python@3.12

# Ubuntu / Debian
sudo apt update && sudo apt install python3 python3-venv
```

**Windows**

Download the installer from [python.org](https://www.python.org/downloads/) and check "Add Python to PATH" during installation. Verify with:

```powershell
python --version
```

**Virtual environment (optional but recommended)**

Keeps dependencies isolated per project:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

## How to use

**1. Fork the repo**

Click **Fork** on GitHub to create your own copy. This is where your solutions will live — you can push freely without touching the original.

**2. Clone your fork**

```bash
git clone https://github.com/<your-username>/python-companion.git
cd python-companion
```

**3. Track your progress**

Before you start working on a topic, create a checkpoint you can return to later. Choose whichever fits your style:

- **Branch per topic** — keeps each practice session isolated and easy to compare:
  ```bash
  git checkout -b practice/list-comprehensions
  ```

- **Commit snapshot** — stage your state so you can `git checkout` back to it at any point:
  ```bash
  git add exercises/
  git commit -m "snapshot: before list comprehensions"
  ```

Both approaches let you diff your starting point against your finished solution, or revert and try a different approach.

**4. Open in Claude Code**

```bash
claude .
```

The skills (slash commands) activate automatically inside this directory.

## Skills (slash commands)

Skills are project-local AI workflows. Type them directly in the Claude Code prompt. Each one is purpose-built for a stage of the learning loop: understand → practice → improve.

---

### `/explain [concept]`

Explains a Python concept concisely — what it is, when to reach for it, a minimal example, and one key gotcha.

**Examples:**

```
/explain list comprehensions
/explain decorators
/explain generators
/explain *args and **kwargs
```

**Sample output for `/explain list comprehensions`:**

> List comprehensions are a compact way to build a list from an iterable in a single expression — reach for them when a `for` loop exists only to append to a list.
>
> ```python
> words = ["apple", "hi", "banana"]
> long_words = [w.title() for w in words if len(w) > 3]
> # ["Apple", "Banana"]
> ```
>
> Gotcha: nesting two comprehensions reads left-to-right but executes outer-first — `[x for row in matrix for x in row]` flattens `matrix`, not the reverse.

---

### `/practice [concept]`

Generates a focused exercise file in `exercises/` so you can apply what you just learned. One well-scoped problem, no solution included.

**Examples:**

```
/practice list comprehensions
/practice error handling
/practice dataclasses
```

The file is saved as `exercises/DDMMYYYY-<concept>.py` and contains:
- A problem statement with input/output examples
- A function stub with type hints
- An `if __name__ == "__main__"` block with sample calls

**See an example:** [`exercises/08052026-list-comprehensions.py`](exercises/08052026-list-comprehensions.py)

---

### `/review [file]`

Reviews your solution as an experienced Python programmer and educator. Evaluates correctness, highlights what's good, and gives specific, line-level feedback on what to improve.

**Examples:**

```
/review exercises/08052026-list-comprehensions.py
/review exercises/10052026-decorators.py
```

Feedback is structured in four sections:

| Section | What it covers |
|---|---|
| **Does it work?** | Correctness, bugs, edge cases, missed requirements |
| **What's good** | One or two specific things done well |
| **What could be better** | Line-level feedback tied to a principle (Pythonic idiom, clarity, naming) |
| **Next step** | One concrete thing to try next |

---

## Suggested workflow

```
1. /explain <concept>          # understand it
2. /practice <concept>         # get an exercise
3. edit exercises/<file>.py    # solve it
4. /review exercises/<file>.py # get feedback
5. iterate
```

## Repository layout

```
python-companion/
├── exercises/          # generated exercise files (solve these)
│   └── 08052026-list-comprehensions.py
└── .claude/
    └── skills/         # slash command definitions
        ├── explain/
        ├── practice/
        └── review/
```

## Contributing exercises

Feel free to add your own `.py` files to `exercises/` and share them. Naming convention: `DDMMYYYY-<topic>.py`.
