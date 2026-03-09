# Project 3: AI Research Agent

## Phase: 3 - Agents & Automation (4-6 weeks)

## Overview
Build an autonomous AI agent that can research topics, search the web, read articles, and compile summaries. This project leverages your MCP knowledge and teaches you how to build AI systems that use tools to accomplish complex tasks.

---

## Prerequisites
- [ ] Completed Project 1 (API basics)
- [ ] Completed Project 2 (RAG concepts)
- [ ] Basic understanding of MCP

---

## Learning Objectives
- [ ] AI Agent architecture (ReAct pattern)
- [ ] Tool use and function calling
- [ ] MCP (Model Context Protocol) deep dive
- [ ] Multi-step reasoning
- [ ] Agent orchestration
- [ ] Error handling and recovery

---

## What You Will Build

### Core Features
1. **Tool System** - Web search, page reader, note-taking
2. **Agent Loop** - Think → Act → Observe → Repeat
3. **MCP Integration** - Build MCP server with tools
4. **Research Pipeline** - End-to-end research automation

### Stretch Goals
- Multi-agent collaboration
- Human-in-the-loop approval
- Parallel tool execution

---

# STEP-BY-STEP IMPLEMENTATION GUIDE

## Step 1: Understand AI Agents Conceptually

### Tasks
- [ ] Read about AI agents and why they matter
- [ ] Understand the ReAct pattern
- [ ] Learn about tool/function calling

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| What are AI Agents? | https://www.promptingguide.ai/research/llm-agents | Agent fundamentals |
| ReAct Paper | https://arxiv.org/abs/2210.03629 | The ReAct reasoning pattern |
| ReAct Explained | https://www.promptingguide.ai/techniques/react | ReAct with examples |
| LangChain Agents Intro | https://python.langchain.com/docs/concepts/agents/ | Agent concepts |

### Key Concept: What is an Agent?
An agent is an LLM that can **take actions** in a loop:
```
1. THINK:   "I need to find information about X"
2. ACT:     Call web_search("X")
3. OBSERVE: "Found 5 results about X..."
4. THINK:   "Let me read the first article"
5. ACT:     Call read_url("https://...")
6. OBSERVE: "Article says..."
7. THINK:   "I have enough info now"
8. ANSWER:  "Based on my research, X is..."
```

### Key Concept: ReAct Pattern
**Re**asoning + **Act**ing in an interleaved manner:
- The model explains its **reasoning** (Thought)
- Then takes an **action** (Action + Action Input)
- Receives the **result** (Observation)
- Continues until done

### Self-Check
Can you explain the difference between a chatbot and an agent?

---

## Step 2: Understanding Function Calling / Tool Use

### Tasks
- [ ] Learn how LLMs call functions
- [ ] Understand tool definitions
- [ ] Make your first function call

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| OpenAI Function Calling | https://platform.openai.com/docs/guides/function-calling | How to define and call functions |
| Anthropic Tool Use | https://docs.anthropic.com/en/docs/build-with-claude/tool-use | Claude's tool calling |
| OpenAI Tools Guide | https://platform.openai.com/docs/assistants/tools | Tools overview |

### Key Concept: Tool Definition
You describe tools to the LLM, and it decides when to use them:
```json
{
  "name": "web_search",
  "description": "Search the web for current information",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query"
      }
    },
    "required": ["query"]
  }
}
```

### Key Concept: The Flow
1. You send message + available tools to LLM
2. LLM responds with a **tool call** (or regular message)
3. You **execute** the tool and get results
4. You send results back to LLM
5. LLM continues reasoning or gives final answer

### What to Implement
- Create a simple tool definition (e.g., calculator)
- Call OpenAI/Anthropic with the tool
- Parse the tool call response
- Execute the tool and send results back

### Checkpoint
You should see the LLM request a tool call, and respond based on the result.

---

## Step 3: Build Your First Tools

### Tasks
- [ ] Create a web search tool
- [ ] Create a web page reader tool
- [ ] Create a note-taking tool

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Tavily Search API | https://docs.tavily.com/documentation/python | Free search API for AI |
| Tavily Quick Start | https://docs.tavily.com/documentation/quickstart | Getting started |
| BeautifulSoup | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | Web scraping |
| httpx | https://www.python-httpx.org/quickstart/ | HTTP requests |

### Tool 1: Web Search
- Use Tavily API (free tier available, designed for AI agents)
- Input: search query
- Output: list of results with titles, URLs, snippets

### Tool 2: Web Reader
- Fetch a URL and extract text content
- Use httpx + BeautifulSoup
- Input: URL
- Output: cleaned text content

### Tool 3: Note Taker
- Store notes in memory during research
- Input: note content
- Output: confirmation
- This helps the agent "remember" findings

### What to Implement
Create `src/tools/` folder with:
- `web_search.py` - Search function
- `web_reader.py` - URL reader function
- `note_taker.py` - Note storage

Each tool should:
1. Have a clear function signature
2. Return structured results
3. Handle errors gracefully

### Checkpoint
Each tool should work independently when called directly.

---

## Step 4: Build the Agent Loop

### Tasks
- [ ] Create the agent loop (Think → Act → Observe)
- [ ] Parse LLM responses for tool calls
- [ ] Execute tools and feed results back

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| LangChain Agent Loop | https://python.langchain.com/docs/how_to/migrate_agent/ | Agent execution |
| Building Agents from Scratch | https://til.simonwillison.net/llms/python-react-pattern | Manual agent implementation |
| OpenAI Assistants | https://platform.openai.com/docs/assistants/overview | Alternative approach |

### Key Concept: The Agent Loop
```python
while not done:
    # 1. Call LLM with conversation + tools
    response = llm.call(messages, tools)
    
    # 2. Check if LLM wants to use a tool
    if response.has_tool_call:
        # 3. Execute the tool
        result = execute_tool(response.tool_call)
        
        # 4. Add result to conversation
        messages.append(tool_result)
    else:
        # 5. LLM gave final answer
        done = True
        final_answer = response.content
```

### What to Implement
Create `src/agent.py`:
- Agent class or function
- Loop that calls LLM
- Detects tool calls vs final answers
- Executes tools and continues
- Stops when complete (or max iterations)

### Important: Stop Conditions
Agents can loop forever! Add safety:
- Maximum iterations (e.g., 10)
- Maximum time (e.g., 60 seconds)
- Detect "I'm done" patterns

### Checkpoint
Your agent should be able to search the web and summarize findings.

---

## Step 5: Deep Dive into MCP

### Tasks
- [ ] Understand MCP architecture
- [ ] Read the MCP specification
- [ ] Understand servers, clients, and transports

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| MCP Official Site | https://modelcontextprotocol.io/ | Overview and spec |
| MCP Introduction | https://modelcontextprotocol.io/introduction | What is MCP? |
| MCP Concepts | https://modelcontextprotocol.io/docs/concepts/architecture | Architecture details |
| MCP Python SDK | https://github.com/modelcontextprotocol/python-sdk | Python implementation |

### Key Concept: What is MCP?
MCP (Model Context Protocol) is a **standard way** for AI apps to connect to tools:
```
┌─────────────┐         ┌─────────────┐
│  AI App     │  MCP    │  MCP Server │
│  (Client)   │ ◄─────► │  (Tools)    │
└─────────────┘         └─────────────┘

One protocol, many tools!
```

### Key Concept: MCP Components
1. **Server**: Exposes tools (your implementation)
2. **Client**: Connects to servers (your agent)
3. **Transport**: How they communicate (stdio, HTTP, etc.)

### Why MCP?
- **Standardized**: One way to define tools
- **Reusable**: Share tools across apps
- **Ecosystem**: Use community-built servers

### Self-Check
Can you explain how MCP differs from regular function calling?

---

## Step 6: Build an MCP Server

### Tasks
- [ ] Set up MCP Python SDK
- [ ] Create a simple MCP server
- [ ] Expose your tools via MCP

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| MCP Python Server | https://modelcontextprotocol.io/docs/first-server/python | Building a server |
| MCP Server Examples | https://github.com/modelcontextprotocol/servers | Example servers |
| MCP Tools Spec | https://modelcontextprotocol.io/docs/concepts/tools | Tool definition |

### What to Implement
Create `src/mcp/server.py`:
- Initialize MCP server
- Register your tools (web_search, web_reader, note_taker)
- Handle tool calls
- Return results

### MCP Tool Structure
```python
# Simplified - see docs for exact format
@server.tool()
def web_search(query: str) -> str:
    """Search the web for information."""
    # Your implementation
    return results
```

### Checkpoint
You should be able to run your MCP server and connect to it.

---

## Step 7: Build an MCP Client

### Tasks
- [ ] Create MCP client
- [ ] Connect to your server
- [ ] Call tools through MCP

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| MCP Python Client | https://modelcontextprotocol.io/docs/first-server/python | Client basics |
| MCP Clients Guide | https://modelcontextprotocol.io/docs/concepts/clients | Client concepts |

### What to Implement
Create `src/mcp/client.py`:
- Connect to MCP server
- List available tools
- Call a tool and get results
- Handle disconnection

### Checkpoint
Client should connect to server and successfully call tools.

---

## Step 8: Connect Agent to MCP

### Tasks
- [ ] Modify agent to use MCP client
- [ ] Dynamically discover tools from MCP
- [ ] Route tool calls through MCP

### What to Implement
Update `src/agent.py`:
- Initialize MCP client
- Get available tools from MCP server
- Convert MCP tools to LLM tool format
- Execute tools via MCP when LLM requests them

### Architecture
```
User Query
    ↓
┌─────────────┐    tool calls    ┌─────────────┐
│   Agent     │ ───────────────► │ MCP Server  │
│   (LLM +    │ ◄─────────────── │ (Tools)     │
│    Client)  │    results       └─────────────┘
└─────────────┘
    ↓
Research Report
```

### Checkpoint
Agent should work exactly as before, but tools are now accessed via MCP.

---

## Step 9: Build the Research Pipeline

### Tasks
- [ ] Create research workflow
- [ ] Generate structured reports
- [ ] Add source citations

### What to Implement
Create complete research flow:
1. User provides research topic
2. Agent searches for information
3. Agent reads relevant pages
4. Agent takes notes on findings
5. Agent synthesizes into report
6. Output formatted report with sources

### Report Format
```markdown
# Research Report: [Topic]

## Summary
[2-3 sentence overview]

## Key Findings
1. [Finding 1]
2. [Finding 2]
...

## Sources
- [Source 1 title](URL)
- [Source 2 title](URL)
```

### Checkpoint
Complete working research agent!

---

## Step 10: Error Handling & Robustness

### Tasks
- [ ] Handle tool failures gracefully
- [ ] Add retries for transient errors
- [ ] Prevent infinite loops

### Common Issues to Handle
| Problem | Solution |
|---------|----------|
| Search returns no results | Try different query |
| URL fails to load | Skip and try next |
| Agent loops forever | Max iterations limit |
| MCP connection fails | Reconnect or fallback |
| LLM refuses task | Better prompting |

### What to Implement
- Try/except around tool calls
- Retry logic with backoff
- Timeout for long operations
- Fallback behaviors

---

## Stretch Goals

### Multi-Agent System
- [ ] Create specialized agents (searcher, reader, writer)
- [ ] Have them collaborate
- **Docs**: https://python.langchain.com/docs/how_to/langgraph/

### Human-in-the-Loop
- [ ] Ask for user approval before actions
- [ ] Let user guide the research
- **Docs**: https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/

### Parallel Tool Execution
- [ ] Run multiple searches simultaneously
- [ ] Speed up research process
- **Docs**: https://docs.python.org/3/library/asyncio.html

---

## Final Project Structure

```
03-ai-research-agent/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── main.py              # Entry point
│   ├── agent.py             # Agent loop
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── web_search.py    # Tavily search
│   │   ├── web_reader.py    # URL reader
│   │   └── note_taker.py    # Notes storage
│   └── mcp/
│       ├── server.py        # MCP server
│       └── client.py        # MCP client
├── outputs/                 # Research reports
│   └── .gitkeep
└── tests/
    └── test_tools.py
```

---

## Self-Check Questions

After completing this project, you should be able to answer:

1. What is the ReAct pattern and why is it effective?
2. How does function calling work in LLMs?
3. What is the agent loop and why do we need stop conditions?
4. What is MCP and how does it standardize tool usage?
5. What are the challenges of building reliable agents?

---

## Notes
_Add your learning notes here as you progress_

---

**Status**: Not Started  
**Started**: -  
**Completed**: -
