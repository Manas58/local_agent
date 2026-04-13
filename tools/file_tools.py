import os

class ReadFileTool:
    name = "read_file"
    description = "Read contents of a file. Input: file path"

    def run(self, path):
        if not os.path.exists(path):
            return "File not found"

        with open(path, "r") as f:
            return f.read()