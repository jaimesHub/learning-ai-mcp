from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("First MCP Server demo")

# Add a hello tool
@mcp.tool()
def hello(name: str) -> str:
    """Say hello to a person"""
    return f"Hello, {name}!"

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers
    """
    return a * b

@mcp.tool()
def sum(a: int, b: int) -> int:
    """
    Sum two numbers
    """
    return a + b

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')