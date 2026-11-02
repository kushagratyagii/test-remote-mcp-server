
from fastmcp import FastMCP
import random

# Initialize MCP server
mcp = FastMCP("My First MCP Server")


# TOOL 1: Sum of two numbers
@mcp.tool()
def sum_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum."""
    return a + b


# TOOL 2: Roll n dice
@mcp.tool()
def roll_dice(n: int) -> list[int]:
    """Roll n six-sided dice and return their individual results."""
    
    if n <= 0:
        raise ValueError("Number of dice must be greater than zero.")

    results = [random.randint(1, 6) for _ in range(n)]
    
    return results


# Run MCP server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000) 
