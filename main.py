from llm.client import LLMClient
from agent.controller import AgentController
from tools.registry import ToolRegistry
from tools.file_tools import ReadFileTool
from execution.executor import Executor

def main():
    llm = LLMClient()

    registry = ToolRegistry()
    registry.register(ReadFileTool())

    executor = Executor(registry)

    agent = AgentController(
        llm=llm,
        tools=registry.list(),
        executor=executor
    )

    print("Agent Ready\n")

    while True:
        user_input = input(">> ")

        if user_input == "exit":
            break

        result = agent.run(user_input)
        print(f"\n{result}\n")

if __name__ == "__main__":
    main()