# Autonomous AI Agents & Tool Calling (ReAct Loop)

## What You Will Learn
- Building Autonomous AI Agent reasoning loops (Reasoning + Action = ReAct pattern)
- Tool calling schemas (binding Python functions as executable tools)
- Agent state management and tool execution parsing
- Preventing infinite loops with max step execution limits

## Why This Matters
AI agents move beyond static Q&A by dynamically executing external code tools, querying live databases, searching the web, and performing API actions autonomously to fulfill complex multi-step user goals.

## Agent Loop Cycle (ReAct)

```text
 User Goal → [ Thought: Decide Next Tool ] → [ Action: Call Function ] → [ Observation: Result ] ↺ Repeat until Final Answer
```

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../ai_projects/`.
