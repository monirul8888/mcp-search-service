# Docs MCP Server

An AI-powered MCP (Model Context Protocol) server that searches official documentation, scrapes content, and returns clean AI-readable results for LLM agents.

Built with:

* Python
* FastMCP
* Serper API
* HTTPX
* AsyncIO

---

# Features

* Search official documentation using Google Serper API
* Fetch and clean webpage content
* Async architecture with `httpx`
* MCP-compatible tool server
* Supports multiple documentation providers
* Works with Claude Desktop MCP

---

# Supported Documentation Sources

| Library    | Docs                         |
| ---------- | ---------------------------- |
| LangChain  | https://python.langchain.com |
| LlamaIndex | https://docs.llamaindex.ai   |
| OpenAI     | https://platform.openai.com  |
| UV         | https://docs.astral.sh       |

---

# Project Structure

```text
mcp-search-service/
│
├── mcp_server.py
├── client.py
├── utils.py
├── .env
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/mcp-search-service.git
cd mcp-search-service
```

---

## 2. Create Virtual Environment

Using `uv`:

```bash
uv venv
```

Activate environment:

### Windows

```powershell
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

Using `uv`:

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_api_key
```

---

# Run MCP Server

```bash
python mcp_server.py
```

---

# Claude Desktop MCP Configuration

Add this configuration to Claude Desktop MCP settings:

```json
{
  "mcpServers": {
    "docs-mcp": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "D:\\Python\\MCP\\mcp-search-service",
      "env": {
        "SERPER_API_KEY": "your_serper_api_key",
        "GROQ_API_KEY": "your_groq_api_key"
      }
    }
  }
}
```

---

# Available MCP Tool

## `get_docs`

Search official documentation and return clean readable content.

### Parameters

| Name    | Type   | Description            |
| ------- | ------ | ---------------------- |
| query   | string | Search query           |
| library | string | Supported library name |

---

## Example

```python
await get_docs(
    query="Publish package with uv",
    library="uv"
)
```

---

# Example Output

```text
SOURCE: https://docs.astral.sh/uv/guides/package/

Publishing packages with uv...
```

---

# Supported Libraries

```python
docs_urls = {
    "langchain": "python.langchain.com",
    "llama-index": "docs.llamaindex.ai",
    "openai": "platform.openai.com",
    "uv": "docs.astral.sh"
}
```

---

# Tech Stack

* FastMCP
* HTTPX
* AsyncIO
* Python Dotenv
* Serper API

---

# Future Improvements

* RAG support with ChromaDB
* Multi-page crawling
* AI summarization
* Streaming responses
* Markdown extraction
* Vector search
* Agent memory

---

# Security Notes

* Never expose API keys publicly
* Store secrets in `.env`
* Rotate keys if accidentally committed

---

# License

MIT License

---

# Author

Md. Monirul Islam

* GitHub: https://github.com/monirul8888
* LinkedIn: https://linkedin.com/in/monirul154
