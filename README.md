# Greeting MCP Server

A basic Python MCP (Model Context Protocol) server that provides a simple greeting tool. This server demonstrates the fundamental concepts of MCP with a greeting function that returns "Hello <your name>".

## Features

- **Greeting Tool**: A simple tool that takes a name parameter and returns a personalized greeting
- **Prompt Support**: Includes a prompt template for generating greetings
- **Logging**: Built-in logging for debugging and monitoring
- **Error Handling**: Proper validation and error messages

## Project Structure

```
my-python-mcp-server/
├── .vscode/
│   ├── mcp.json          # MCP server configuration
│   └── settings.json     # VS Code Python settings
├── src/
│   ├── .venv/           # Virtual environment (created during setup)
│   ├── main.py          # Main MCP server implementation
│   └── pyproject.toml   # Project dependencies
└── README.md           # This file
```

## Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager
- VS Code with GitHub Copilot extension

## Setup Instructions

1. **Navigate to the src directory:**
   ```powershell
   cd src
   ```

2. **Create a virtual environment:**
   ```powershell
   uv venv
   ```

3. **Activate the virtual environment:**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. **Install dependencies:**
   ```powershell
   uv sync
   ```

5. **Configure Python interpreter in VS Code:**
   - Open Command Palette (Ctrl+Shift+P)
   - Select "Python: Select Interpreter"
   - Choose the interpreter at `src\.venv\Scripts\python.exe`

6. **Start the MCP server:**
   - Open `.vscode/mcp.json`
   - Click the run button in the editor to start the MCP server
   - Check Output view to see server logs

## Usage

### In GitHub Copilot Chat

1. Ensure Agent mode is selected in Copilot Chat
2. Click the tools icon and enable the `greeting-mcp` tool
3. Use the greeting tool by asking: "Please greet John" or "Say hello to Sarah"

### Available MCP Components

- **Tool**: `greeting(name: str)` - Returns "Hello <name>"
- **Prompt**: `create_greeting_prompt(name: str)` - Generates instructions for using the greeting tool

## Example Interactions

**Using the tool directly:**
```
Input: greeting("Alice")
Output: "Hello Alice"
```

**Using the prompt:**
```
Input: create_greeting_prompt("Bob")
Output: "Please generate a greeting for the person named 'Bob'. Use the `greeting` tool to create a personalized greeting message."
```

## Troubleshooting

- **Tools not visible in Copilot Chat?** Ensure the MCP server is running and enabled in the tools list
- **No logs?** Check that the MCP config points to the correct Python interpreter path
- **Module not found errors?** Make sure you're using the virtual environment's Python interpreter

## Inspiration

This project is inspired by the Microsoft AI Tour 2026 MCP server example from [aitour26-LTG152-from-protocol-to-practice-build-and-use-your-first-mcp-server](https://github.com/microsoft/aitour26-LTG152-from-protocol-to-practice-build-and-use-your-first-mcp-server).

## License

MIT License