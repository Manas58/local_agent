class Executor:
    def __init__(self, registry):
        self.registry = registry

    def execute(self, tool_name, tool_input):
        tool = self.registry.get(tool_name)

        if not tool:
            return f"Tool {tool_name} not found"

        try:
            return tool.run(tool_input)
        except Exception as e:
            return str(e)