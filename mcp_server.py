# Create AI Web Scapper Tool
# Step 1: Search The Tool


import http.client
import json
import os
import httpx
import asyncio
from dotenv import load_dotenv

load_dotenv()

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



async def fetch_url(url: str):
    async with httpx.AsyncClient as client:
         response = await client.post(
            url,
            timeout=30.0
        )
         
         cleaned_response = clean_html_text(response)
         
         return cleaned_response.text
    







# Step 2: Open Official Documentation
# Step 3: Read Documentation and Write Code


