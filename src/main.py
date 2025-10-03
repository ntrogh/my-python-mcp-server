import logging
from fastmcp import FastMCP

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger("GreetingMCP")

# Create the MCP server
mcp = FastMCP("Greeting Server")


@mcp.tool
async def greeting(name: str) -> str:
    """Generate a greeting message for the given name.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        str: A greeting message in the format "Hello <name>"
    """
    logger.info(f"Generating greeting for: {name}")
    
    if not name or not name.strip():
        return "Error: Name cannot be empty"
    
    greeting_message = f"Hello {name.strip()}"
    logger.info(f"Generated greeting: {greeting_message}")
    
    return greeting_message


@mcp.prompt
def create_greeting_prompt(name: str) -> str:
    """Generate a prompt to create a greeting using the greeting tool.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        str: A prompt instructing to use the greeting tool
    """
    logger.info(f"Greeting prompt created for: {name}")
    
    return f"""Please generate a greeting for the person named "{name}".

Use the `greeting` tool to create a personalized greeting message."""


if __name__ == "__main__":
    logger.info("MCP Greeting server starting")
    mcp.run()