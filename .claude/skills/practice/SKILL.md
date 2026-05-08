---
name: practice
description: Design and generate a python assignment in work file.
argument_hint: [concept]
arguments: $concept
allowed-tools: Read, Write, Edit
---

Generate one focused Python exercise as a single .py file in exercises/ dir , so that the user can work on it.

1. Design ONE well-scoped problem that exercises the $concept. Not a tutorial, not a test battery — one problem.
2. Write a .py file in exercises/ with:
- A module docstring containing: problem statement, 2–3 input → expected output examples, acceptance criteria.
- A function stub with a meaningful name and an args/return docstring.
- `raise NotImplementedError` as the body.
   - An `if __name__ == "__main__":` block with sample calls (commented out so the file runs without erroring).
3. Save the file under `exercises/ddmmyyy-<$concept>.py`
3. Reply briefly: where the file is, one sentence on what to do.

Rules:
- No solution in the file. As few hints as possible.
- The docstring should let the user start without re-asking what to do.
- If the topic is too broad, narrow it and say which slice you picked.
