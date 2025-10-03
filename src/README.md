# Greeting MCP Server

A simple MCP server that provides a greeting tool returning "Hello <your name>".

## Project Purpose

- Demonstrate a basic MCP server implementation using FastMCP
- Provide a simple greeting tool for learning MCP concepts
- Show proper error handling and logging practices

## How to Run Locally

1. **Create virtual environment:**
   ```powershell
   uv venv
   ```

2. **Activate virtual environment:**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   uv sync
   ```

4. **Configure VS Code interpreter:**
   - Ensure `.vscode/settings.json` points to `src\.venv\Scripts\python.exe`
   - Select the interpreter via Command Palette

5. **Start MCP server:**
   - Open `.vscode/mcp.json`
   - Click run button to start the server
   - Check Output view for logs

6. **Use in GitHub Copilot Chat:**
   - Enable Agent mode
   - Enable the greeting-mcp tool
   - Ask for greetings: "Please greet Alice"

## Key Components

- **Tool**: `greeting(name)` - Returns personalized greeting
- **Prompt**: `create_greeting_prompt(name)` - Generates tool usage instructions
- **Logging**: Comprehensive logging for debugging
- **Error Handling**: Input validation and error messages