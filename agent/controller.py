import json

class AgentController:
    def __init__(self, llm, tools, executor, max_steps=10):
        self.llm = llm
        self.tools = tools
        self.executor = executor
        self.max_steps = max_steps

    def run(self, user_input):
        history = []

        for step in range(self.max_steps):
            prompt = self._build_prompt(user_input, history)

            response = self.llm.chat([{"role": "user", "content": prompt}])

            try:
                parsed = json.loads(response)
            except:
                return f"Invalid response from LLM:\n{response}"

            thought = parsed.get("thought")
            action = parsed.get("action")
            tool_input = parsed.get("input")

            print(f"\n[Step {step+1}]")
            print(f"Thought: {thought}")
            print(f"Action: {action}")

            if action == "final_answer":
                return parsed.get("final_answer")

            # execute tool
            result = self.executor.execute(action, tool_input)

            history.append({
                "thought": thought,
                "action": action,
                "input": tool_input,
                "output": result
            })

        return "Max steps reached"
    
    def _build_prompt(self, user_input, history):
        history_text = "\n".join(
            [f"{h['action']} -> {h['output']}" for h in history]
        )

        return f"""

Previous Steps:
{history_text}

Task:
{user_input}
"""