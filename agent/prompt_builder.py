def build_prompt(user_input, tools, history):
    tool_descriptions = "\n".join(
        [f"{t['name']}: {t['description']}" for t in tools]
    )

    return f"""
You are an AI coding agent.

You can use tools to solve tasks.

AVAILABLE TOOLS:
{tool_descriptions}

RULES:
- Always respond in JSON
- Decide next step carefully
- Use tools when needed
- If task is complete → use action "final_answer"

FORMAT:
{{
  "thought": "...",
  "action": "...",
  "input": "...",
  "final_answer": "..."
}}

USER INPUT:
{user_input}
"""