from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("First MCP Server demo")

# Add a hello tool
@mcp.tool()
def hello(name: str) -> str:
    """Say hello to a person"""
    return f"Hello, {name}!"
