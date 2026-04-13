# 🚀 Local AI Coding Agent (Claude Code–Style)

## 🧠 Project Overview

This project aims to build a **fully local, CLI-based AI coding agent** powered by an LLM (via Ollama), capable of:

- Understanding codebases
- Modifying files
- Executing commands
- Iterating on tasks autonomously
- Logging and monitoring all actions

---

# ⚙️ Tech Stack

## 🧠 Core AI
- LLM Runtime: Ollama  
- Models: llama3 / mistral  

## 💻 Backend
- Language: Python  
- CLI: rich + prompt_toolkit  

## 🧩 Agent System
- Custom agent loop  
- MCP (Model Context Protocol) for tool interaction  

## 🛠️ Tools
- File system tools (read/write/edit)  
- Terminal execution  
- (Future) Git tools  

## 🗄️ Database
- SQLite (primary)
- JSON (optional for quick start)

## 🔐 Safety (Minimal)
- Path restriction (project directory only)
- Command filtering
- File size limits

---

# 🧠 System Architecture
CLI
↓
Agent Loop (step-limited + interruptible)
↓
LLM (Ollama)
↓
MCP Layer (tool interface)
↓
Tools (filesystem, terminal)
↓
Execution Layer (safety + validation)
↓
SQLite (logs + monitoring)


---

# 🗄️ Database Schema

## 🔹 sessions
```sql
id TEXT PRIMARY KEY,
start_time DATETIME,
end_time DATETIME
🔹 messages
id INTEGER PRIMARY KEY AUTOINCREMENT,
session_id TEXT,
role TEXT,
content TEXT,
timestamp DATETIME
🔹 agent_steps
id INTEGER PRIMARY KEY AUTOINCREMENT,
session_id TEXT,
step_number INTEGER,
thought TEXT,
action TEXT,
tool_name TEXT,
input TEXT,
output TEXT,
status TEXT,
timestamp DATETIME
🔹 tool_executions
id INTEGER PRIMARY KEY AUTOINCREMENT,
tool_name TEXT,
arguments TEXT,
result TEXT,
success BOOLEAN,
execution_time FLOAT,
timestamp DATETIME
🔹 audit_logs
id INTEGER PRIMARY KEY AUTOINCREMENT,
action_type TEXT,
target TEXT,
change_summary TEXT,
risk_level TEXT,
timestamp DATETIME
📦 Folder Structure
code_agent/
│
├── main.py
│
├── config/
│   └── settings.py
│
├── agent/
│   ├── core.py
│   ├── controller.py
│   ├── memory.py
│   └── prompt_builder.py
│
├── llm/
│   └── client.py
│
├── mcp/
│   ├── server.py
│   └── tool_adapter.py
│
├── tools/
│   ├── base.py
│   ├── registry.py
│   ├── file_tools.py
│   └── terminal_tools.py
│
├── execution/
│   ├── executor.py
│   ├── validator.py
│   └── safety.py
│
├── database/
│   ├── db.py
│   ├── models.py
│   └── logger.py
│
├── cli/
│   ├── app.py
│   └── ui.py
│
├── utils/
│   └── helpers.py
│
├── data/
│   └── agent.db
│
└── requirements.txt
🧠 Key Design Principles
Tool-first architecture → everything is a tool

Controlled agent loop → no infinite execution

MCP as bridge, not logic

Full observability → every step logged

Local-first system → privacy + control

🎯 End Goal
A system that can:

Read and understand code

Modify files intelligently

Execute commands

Debug errors

Log all actions for monitoring

Operate fully locally

⚡ Notes
Hotkey will act as a manual interrupt for agent execution

Step limits prevent infinite loops

Safety is minimal but focused on preventing data leaks