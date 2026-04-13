import requests
import json

class LLMClient:
    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://172.27.16.1:11434/api/generate"

    def chat(self, messages):
        prompt = self._format_messages(messages)

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()["response"]

        return result.strip()

    def _format_messages(self, messages):
        system = """
    You are an AI agent.

    You MUST respond ONLY in valid JSON.

    DO NOT write explanations.
    DO NOT write normal text.
    DO NOT add anything outside JSON.

    STRICT FORMAT:
    {
    "thought": "string",
    "action": "tool_name OR final_answer",
    "input": "string",
    "final_answer": "string"
    }
    """

        formatted = f"SYSTEM:\n{system}\n\n"

        for m in messages:
            formatted += f"{m['role'].upper()}:\n{m['content']}\n\n"

        return formatted