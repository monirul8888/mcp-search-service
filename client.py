import json
import os
import httpx
import asyncio
from dotenv import load_dotenv
#========================================
from fastmcp import FastMCP
from groq import Groq
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()

server_params = StdioServerParameters(
    command="uv",
    args=["run", "mcp_server.py"],
    env=None
    
)

async def main():

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools_response = await session.list_tools()
            print("Available tools:", [t.name for t in tools_response.tools])

if __name__ == "__main__":
    asyncio.run(main())
    