# Create AI Web Scapper Tool
# Step 1: Search The Tool


import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")


query = "ChromaDB official documentation"

conn = http.client.HTTPSConnection("google.serper.dev")
payload = json.dumps({
  "q": query, "num":2
})
headers = {
  'X-API-KEY': SERPER_API_KEY,
  'Content-Type': 'application/json'
}
conn.request("POST", "/search", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))







# Step 2: Open Official Documentation
# Step 3: Read Documentation and Write Code


