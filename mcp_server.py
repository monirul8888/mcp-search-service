# Create AI Web Scapper Tool
# Step 1: Search The Tool


import http.client
import json
import os
import httpx
import asyncio
from dotenv import load_dotenv
from utils import clean_html_text


#========================================
from fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("Docs")

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_URL = "https://google.serper.dev/search"

async def search_web(query: str)-> dict | None:
    
    payload = json.dumps({
    "q": query,
    "num":2
    })
    
    headers = {
    'X-API-KEY': SERPER_API_KEY,
    'Content-Type': 'application/json'
    }
    #conn = http.client.HTTPSConnection("google.serper.dev")
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SERPER_URL,
            headers=headers,
            data = payload,
            timeout=30.0
        )
        
        response.raise_for_status()
        return response.json()
    
        #conn.request("POST", "/search", payload, headers)
        # res = conn.getresponse()
        # data = res.read()
        # return(data.decode("utf-8"))

res = asyncio.run(search_web(query = "ChromaDB official documentation"))

print(res)


# Step 2: Open Official Documentation

async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
         response = await client.get(
            url,
            timeout=30.0
        )
         cleaned_response = clean_html_text(response.text)
         return cleaned_response
    


# Step 3: Read Documentation and Write Code
docs_urls = {
"langchain": "python.langchain.com/docs",
"llama-index": "docs.llamaindex.ai/en/stable",
"openai": "platform.openai.com/docs",
"uv": "docs.astral.sh/uv"
}

@mcp.tool()
async def get_docs(query: str, libray:str):
    
    """
    Search the latest docs for a given query and library.
    Supports langchain, openai, llama-index and uv.

    Args:
        query: The query to search for (e.g. "Publish a package with UV")
        library: The library to search in (e.g. "uv")

    Returns:
        Summarized text from the docs with source links.
    """
    if libray not in docs_urls:
        raise ValueError(f"Library {libray} not Supported in This Tools")
    query = f"site:{docs_urls[libray]} {query}"
    results = await search_web(query)
    
    if len(results["organic"])==0:
        return "No Result Found"
    
    text_parts = []
    for result in results["organic"]:
        link = result.get("link", "")
        raw = await fetch_url(link)
        if raw:
            labeled = f"SOURCE: {link}\n{raw}"
            text_parts.append(labeled)           
    return "\n\n".join(text_parts)


def main():
    
    mcp.run(transport="stdio")
    
if __name__ == "__main__":
    main()
    
    


