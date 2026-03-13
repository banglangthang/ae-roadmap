# Project 1: AI Chatbot CLI

## Phase: 1 - Foundations (2-3 weeks)

## Overview
Build a command-line chatbot that integrates with LLM APIs (OpenAI/Anthropic). This project will teach you the fundamentals of working with AI APIs, prompt engineering, and conversation management.

---

## Learning Objectives
- [x] Python fundamentals for AI development
- [x] Working with REST APIs
- [x] LLM API integration (OpenAI/Anthropic)
- [x] Prompt engineering techniques
- [x] Conversation history management
- [x] System prompts and few-shot examples
- [x] Error handling and rate limiting

---

## What You Will Build

### Core Features
1. **Basic Chat Interface** - Send messages to LLM, display responses
2. **Conversation History** - Maintain context across messages
3. **System Prompts** - Different AI personalities/modes
4. **Streaming Responses** - Real-time output like ChatGPT

### Stretch Goals
- Multi-model support (GPT + Claude)
- Token counting and cost tracking
- Save/load conversations

---

# STEP-BY-STEP IMPLEMENTATION GUIDE

## Step 1: Environment Setup

### Tasks
- [x] Create a virtual environment
- [x] Install required packages
- [x] Set up your API key securely

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Python venv | https://docs.python.org/3/library/venv.html | How to create isolated Python environments |
| pip basics | https://pip.pypa.io/en/stable/getting-started/ | How to install packages |
| python-dotenv | https://pypi.org/project/python-dotenv/ | How to manage environment variables securely |

### What to Implement
1. Create `venv` folder with virtual environment
2. Create `requirements.txt` with dependencies
3. Create `.env` file (from `.env.example`) with your API key

### Hints
- Never commit `.env` to git (it contains secrets)
- Use `python-dotenv` to load environment variables

---

## Step 2: Make Your First API Call

### Tasks
- [x] Get an API key from OpenAI or Anthropic
- [x] Make a simple API call
- [x] Print the response

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| OpenAI Quickstart | https://platform.openai.com/docs/quickstart | How to make your first API call |
| OpenAI Chat API | https://platform.openai.com/docs/guides/text-generation | Understanding chat completions |
| Anthropic Quickstart | https://docs.anthropic.com/en/docs/quickstart | Alternative: Using Claude API |
| OpenAI Python SDK | https://github.com/openai/openai-python | Official Python library |

### Key Concepts to Understand
1. **Messages format**: `[{"role": "user", "content": "Hello"}]`
2. **Roles**: `system`, `user`, `assistant`
3. **API Response structure**: How to extract the reply

### What to Implement
Create `src/api_client.py`:
- Function to initialize the OpenAI/Anthropic client
- Function to send a message and get a response
- Test it with a simple "Hello, how are you?"

### Checkpoint
You should be able to run your script and see the AI respond.

---

## Step 3: Build the Chat Loop

### Tasks
- [x] Create a loop that takes user input
- [x] Send input to API
- [x] Display response
- [x] Repeat until user quits

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Python input() | https://docs.python.org/3/library/functions.html#input | Getting user input |
| Rich library | https://rich.readthedocs.io/en/latest/ | Beautiful terminal output |
| Rich Console | https://rich.readthedocs.io/en/latest/console.html | Printing formatted text |

### What to Implement
Create `src/main.py`:
- Main loop: `while True`
- Get input from user
- Check for quit command (`/quit`)
- Call your API client
- Print the response nicely

### Checkpoint
You should have a working chat in your terminal!

---

## Step 4: Add Conversation History

### Tasks
- [x] Store messages in a list
- [x] Send full history with each request
- [x] Understand context window limits

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| OpenAI Chat Format | https://platform.openai.com/docs/guides/text-generation#building-prompts | How messages build context |
| Context Window | https://platform.openai.com/docs/models | Token limits per model |
| Conversation Memory | https://www.pinecone.io/learn/series/langchain/langchain-conversational-memory/ | Patterns for managing history |

### Key Concept: Why History Matters
LLMs are **stateless** - they don't remember previous messages. YOU must send the conversation history each time:

```
Request 1: [user: "My name is John"]
Request 2: [user: "My name is John", assistant: "Nice to meet you!", user: "What's my name?"]
```

### What to Implement
Create `src/history.py`:
- Class or functions to manage message history
- Add message function
- Get messages for API function
- Clear history function

### Checkpoint
The AI should remember what you said earlier in the conversation.

---

## Step 5: Implement System Prompts

### Tasks
- [ ] Understand what system prompts do
- [ ] Create different "modes" (assistant, coder, teacher)
- [ ] Allow switching between modes

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| System Prompts | https://platform.openai.com/docs/guides/text-generation#system-messages | How to set AI behavior |
| Prompt Engineering | https://www.promptingguide.ai/ | Comprehensive prompt guide |
| OpenAI Best Practices | https://platform.openai.com/docs/guides/prompt-engineering | Official prompting tips |
| Anthropic Prompt Guide | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview | Claude-specific prompting |

### Key Concept: System Message
The system message sets the AI's behavior:
```
{"role": "system", "content": "You are a helpful coding assistant. Always provide code examples."}
```

### What to Implement
Create `src/prompts.py`:
- Dictionary/JSON of different system prompts
- Function to get prompt by mode name
- Function to list available modes

Update `main.py`:
- Add `/mode` command to switch modes
- Load system prompt when mode changes

### Checkpoint
Switching to "coder" mode should make the AI respond differently than "teacher" mode.

---

## Step 6: Add Streaming Responses

### Tasks
- [ ] Implement streaming API calls
- [ ] Display text as it arrives (like ChatGPT)

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| OpenAI Streaming | https://platform.openai.com/docs/api-reference/streaming | How streaming works |
| OpenAI Python Streaming | https://github.com/openai/openai-python#streaming-responses | Python implementation |
| Anthropic Streaming | https://docs.anthropic.com/en/api/streaming | Claude streaming |

### Key Concept: Streaming
Instead of waiting for the full response, you receive chunks:
```
"Hello" → " there" → "!" → " How" → " can" → " I" → " help" → "?"
```

### What to Implement
Update `src/api_client.py`:
- Add `stream=True` parameter
- Iterate over response chunks
- Print each chunk immediately

### Checkpoint
You should see text appearing word-by-word, not all at once.

---

## Step 7: Save and Load Conversations

### Tasks
- [ ] Save conversations to JSON files
- [ ] Load previous conversations
- [ ] List saved conversations

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Python JSON | https://docs.python.org/3/library/json.html | Reading/writing JSON |
| Python pathlib | https://docs.python.org/3/library/pathlib.html | File path handling |

### What to Implement
Update `src/history.py`:
- Save conversation to `conversations/` folder
- Load conversation by ID
- List all saved conversations

Add commands to `main.py`:
- `/save` - Save current conversation
- `/load` - Load a previous conversation
- `/list` - Show saved conversations

### Checkpoint
You should be able to close the app, reopen it, and continue a previous conversation.

---

## Step 8: Error Handling & Polish

### Tasks
- [x] Handle API errors gracefully
- [x] Handle rate limiting
- [x] Add helpful error messages

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| OpenAI Errors | https://platform.openai.com/docs/guides/error-codes | Error types and handling |
| OpenAI Rate Limits | https://platform.openai.com/docs/guides/rate-limits | Understanding rate limits |
| Python try/except | https://docs.python.org/3/tutorial/errors.html | Exception handling |

### Common Errors to Handle
1. **Invalid API key** - Tell user to check `.env`
2. **Rate limit** - Wait and retry, or tell user to slow down
3. **Context too long** - Truncate history or warn user
4. **Network error** - Retry or show friendly message

### Checkpoint
The app should never crash with an ugly error. Always show helpful messages.

---

## Stretch Goals (Optional)

### Multi-Model Support
- [x] Support both OpenAI and Anthropic
- [x] Add `/model` command to switch

**Docs**: Compare the two APIs - notice the differences in message format

### Token Counting
- [x] Count tokens in messages
- [x] Show estimated cost

**Docs**: 
- https://github.com/openai/tiktoken (Token counting library)
- https://openai.com/pricing (Pricing info)

---

## Final Project Structure

```
01-ai-chatbot-cli/
├── README.md
├── requirements.txt
├── .env.example
├── .env                  # Your API keys (don't commit!)
├── src/
│   ├── main.py           # Entry point, chat loop, commands
│   ├── api_client.py     # API wrapper (OpenAI/Anthropic)
│   ├── prompts.py        # System prompts and modes
│   └── history.py        # Conversation management
├── prompts/
│   └── system_prompts.json   # Your custom prompts
└── conversations/
    └── *.json            # Saved conversations
```

---

## Self-Check Questions

After completing this project, you should be able to answer:

1. What is the difference between `system`, `user`, and `assistant` roles?
2. Why do we need to send conversation history with each API call?
3. What is a token and why does it matter?
4. How does streaming differ from regular API calls?
5. What is prompt engineering and why is it important?

---

## Notes
_Add your learning notes here as you progress_

---

**Status**: Done
**Started**: -  
**Completed**: -
