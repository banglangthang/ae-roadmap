# Project 4: Full AI SaaS Application

## Phase: 4 - Production AI (4-6 weeks)

## Overview
Build a production-ready AI SaaS application that combines everything you've learned. This project includes user authentication, multiple AI features, usage tracking, and deployment to the cloud.

---

## Prerequisites
- [ ] Completed Project 1 (Chatbot)
- [ ] Completed Project 2 (RAG)
- [ ] Completed Project 3 (Agents)
- [ ] Basic understanding of web development

---

## Learning Objectives
- [ ] Full-stack AI application architecture
- [ ] User authentication & authorization
- [ ] Database design for AI apps
- [ ] Token usage tracking & billing
- [ ] Rate limiting & API security
- [ ] Deployment & DevOps
- [ ] Monitoring & observability

---

## What You Will Build

### Core Features
1. **User Management** - Registration, login, API keys
2. **AI Features** - Chat, Document Q&A, Research Agent
3. **Usage Tracking** - Token counting, limits, cost tracking
4. **Admin Dashboard** - User management, analytics

### Stretch Goals
- Stripe payment integration
- Team/organization support
- Custom fine-tuned models

---

# STEP-BY-STEP IMPLEMENTATION GUIDE

## Step 1: Understand SaaS Architecture

### Tasks
- [ ] Learn about full-stack architecture
- [ ] Understand API design principles
- [ ] Learn about microservices vs monolith

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| FastAPI Introduction | https://fastapi.tiangolo.com/tutorial/ | Modern Python web framework |
| REST API Design | https://restfulapi.net/ | API design principles |
| SaaS Architecture | https://12factor.net/ | 12-factor app methodology |
| Full-Stack AI Apps | https://fullstackdeeplearning.com/course/2022/ | Production AI systems |

### Key Concept: Layered Architecture
```
┌─────────────┐
│  Frontend   │  ← User interface (React/Next.js)
├─────────────┤
│  API Layer  │  ← REST endpoints (FastAPI)
├─────────────┤
│  Services   │  ← Business logic (AI, Auth, Usage)
├─────────────┤
│  Data Layer │  ← Databases (PostgreSQL, Redis, Vector)
└─────────────┘
```

### Self-Check
Can you explain why we separate frontend, backend, and database?

---

## Step 2: Set Up Backend Framework

### Tasks
- [ ] Create FastAPI project structure
- [ ] Set up configuration management
- [ ] Create health check endpoint
- [ ] Set up CORS for frontend

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| FastAPI First Steps | https://fastapi.tiangolo.com/tutorial/first-steps/ | Creating your first API |
| FastAPI Project Structure | https://fastapi.tiangolo.com/tutorial/bigger-applications/ | Organizing larger apps |
| Pydantic Settings | https://docs.pydantic.dev/latest/concepts/pydantic_settings/ | Configuration management |
| FastAPI CORS | https://fastapi.tiangolo.com/tutorial/cors/ | Cross-origin requests |

### What to Implement
Create `backend/` folder structure:
- `app/main.py` - FastAPI app initialization
- `app/config.py` - Environment configuration
- `app/routes/` - API endpoints folder
- Basic health check: `GET /health`

### Checkpoint
Running `uvicorn app.main:app --reload` should start your server.

---

## Step 3: Database Setup

### Tasks
- [ ] Choose and set up PostgreSQL
- [ ] Learn SQLAlchemy ORM
- [ ] Create database models
- [ ] Set up migrations with Alembic

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| SQLAlchemy Tutorial | https://docs.sqlalchemy.org/en/20/tutorial/ | ORM basics |
| FastAPI + SQLAlchemy | https://fastapi.tiangolo.com/tutorial/sql-databases/ | Integration guide |
| Alembic Tutorial | https://alembic.sqlalchemy.org/en/latest/tutorial.html | Database migrations |
| PostgreSQL Basics | https://www.postgresql.org/docs/current/tutorial.html | Database fundamentals |
| Docker PostgreSQL | https://hub.docker.com/_/postgres | Running PostgreSQL in Docker |

### Key Concept: Database Models
```
User
├── id (primary key)
├── email
├── hashed_password
├── created_at
└── is_active

Usage
├── id
├── user_id (foreign key)
├── model
├── input_tokens
├── output_tokens
├── cost
└── timestamp
```

### What to Implement
Create `app/models/`:
- `user.py` - User model
- `usage.py` - Usage tracking model
- Set up Alembic for migrations

### Checkpoint
You should be able to create tables and run migrations.

---

## Step 4: User Authentication

### Tasks
- [ ] Understand JWT authentication
- [ ] Implement user registration
- [ ] Implement user login
- [ ] Protect routes with auth middleware

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| FastAPI Security | https://fastapi.tiangolo.com/tutorial/security/ | Auth overview |
| JWT Authentication | https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ | JWT implementation |
| Password Hashing | https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/ | Secure passwords |
| OAuth2 Concepts | https://oauth.net/2/ | Auth standards |
| python-jose | https://python-jose.readthedocs.io/ | JWT library |
| passlib | https://passlib.readthedocs.io/ | Password hashing |

### Key Concept: JWT Flow
```
1. User sends email + password to /login
2. Server verifies credentials
3. Server creates JWT token with user ID
4. Client stores token
5. Client sends token in headers for future requests
6. Server validates token on each request
```

### What to Implement
Create `app/routes/auth.py`:
- `POST /auth/register` - Create new user
- `POST /auth/login` - Return JWT token
- `GET /auth/me` - Get current user (protected)

Create `app/middleware/auth.py`:
- JWT validation
- Get current user from token

### Checkpoint
You should be able to register, login, and access protected routes.

---

## Step 5: Integrate AI Services

### Tasks
- [ ] Create service layer for AI features
- [ ] Integrate chat functionality (Project 1)
- [ ] Integrate document Q&A (Project 2)
- [ ] Integrate research agent (Project 3)

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| FastAPI Dependencies | https://fastapi.tiangolo.com/tutorial/dependencies/ | Dependency injection |
| Service Pattern | https://www.cosmicpython.com/book/chapter_04_service_layer.html | Service layer design |
| Background Tasks | https://fastapi.tiangolo.com/tutorial/background-tasks/ | Async processing |

### Key Concept: Service Layer
Separate business logic from API routes:
```
Route (handles HTTP) → Service (handles logic) → External APIs (OpenAI, etc.)
```

### What to Implement
Create `app/services/`:
- `ai_service.py` - Wrapper for all AI features
  - `chat()` - From Project 1
  - `document_qa()` - From Project 2
  - `research()` - From Project 3

Create `app/routes/`:
- `chat.py` - `POST /chat`
- `documents.py` - `POST /documents/upload`, `POST /documents/query`
- `agent.py` - `POST /research`

### Checkpoint
All three AI features should work via API endpoints.

---

## Step 6: Token Counting & Usage Tracking

### Tasks
- [ ] Learn how to count tokens
- [ ] Track usage per request
- [ ] Store usage in database
- [ ] Create usage statistics endpoint

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| tiktoken | https://github.com/openai/tiktoken | OpenAI token counting |
| OpenAI Pricing | https://openai.com/pricing | Cost per token |
| Anthropic Pricing | https://www.anthropic.com/pricing | Claude pricing |

### Key Concept: Token Counting
Tokens are NOT characters. Count them properly:
```python
import tiktoken
encoder = tiktoken.encoding_for_model("gpt-4")
tokens = encoder.encode("Hello, world!")
print(len(tokens))  # Number of tokens
```

### What to Implement
Create `app/utils/token_counter.py`:
- Function to count tokens for text
- Function to estimate cost

Create `app/services/usage_service.py`:
- Track usage after each AI call
- Store in database
- Calculate totals for user

Create `app/routes/usage.py`:
- `GET /usage/summary` - User's usage stats
- `GET /usage/history` - Detailed history

### Checkpoint
After each AI request, usage should be tracked and viewable.

---

## Step 7: Rate Limiting

### Tasks
- [ ] Understand rate limiting patterns
- [ ] Implement rate limiting middleware
- [ ] Set limits per user tier

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| FastAPI Rate Limiting | https://slowapi.readthedocs.io/ | SlowAPI library |
| Redis Rate Limiting | https://redis.io/commands/incr/#pattern-rate-limiter | Redis-based limiting |
| Rate Limit Patterns | https://cloud.google.com/architecture/rate-limiting-strategies-techniques | Different strategies |

### Key Concept: Rate Limiting Strategies
- **Fixed Window**: 100 requests per minute
- **Sliding Window**: Smoother, more complex
- **Token Bucket**: Allow bursts

### What to Implement
Create `app/middleware/rate_limit.py`:
- Rate limiter using Redis (or in-memory)
- Different limits for different endpoints
- Return 429 when exceeded

### Checkpoint
Rapid requests should be blocked after limit is reached.

---

## Step 8: Frontend Setup

### Tasks
- [ ] Set up Next.js or React project
- [ ] Create authentication pages
- [ ] Build chat interface
- [ ] Add document upload UI

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Next.js Getting Started | https://nextjs.org/docs/getting-started | React framework |
| Next.js App Router | https://nextjs.org/docs/app | Modern routing |
| Tailwind CSS | https://tailwindcss.com/docs | Styling |
| React Query | https://tanstack.com/query/latest | Data fetching |
| Zustand | https://docs.pmnd.rs/zustand/getting-started/introduction | State management |
| Shadcn UI | https://ui.shadcn.com/ | UI components |

### What to Implement
Create `frontend/` folder:
- `/login` page - User login
- `/register` page - User registration
- `/chat` page - Chat interface
- `/documents` page - Document Q&A
- `/dashboard` page - Usage statistics

### Checkpoint
Frontend should connect to backend and all features should work.

---

## Step 9: Docker & Local Development

### Tasks
- [ ] Dockerize backend
- [ ] Dockerize frontend
- [ ] Create docker-compose for all services

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Docker Getting Started | https://docs.docker.com/get-started/ | Container basics |
| Dockerfile Reference | https://docs.docker.com/engine/reference/builder/ | Writing Dockerfiles |
| Docker Compose | https://docs.docker.com/compose/ | Multi-container apps |
| Docker + Python | https://docs.docker.com/language/python/ | Python containers |
| Docker + Node | https://docs.docker.com/language/nodejs/ | Node containers |

### What to Implement
Create:
- `backend/Dockerfile`
- `frontend/Dockerfile`
- `docker-compose.yml` - All services together

### docker-compose should include:
- Backend (FastAPI)
- Frontend (Next.js)
- PostgreSQL
- Redis
- ChromaDB (for vectors)

### Checkpoint
`docker-compose up` should start entire app.

---

## Step 10: Deployment

### Tasks
- [ ] Choose cloud provider
- [ ] Set up CI/CD pipeline
- [ ] Deploy to production
- [ ] Set up monitoring

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Vercel (Frontend) | https://vercel.com/docs | Deploy Next.js |
| Railway (Backend) | https://docs.railway.app/ | Deploy containers |
| Fly.io | https://fly.io/docs/ | Alternative deployment |
| Render | https://render.com/docs | Full-stack deployment |
| GitHub Actions | https://docs.github.com/en/actions | CI/CD |

### Deployment Options
| Service | Best For | Complexity |
|---------|----------|------------|
| Vercel + Railway | Quick start | Low |
| Render | Full-stack | Low |
| Fly.io | Global distribution | Medium |
| AWS/GCP | Full control | High |

### What to Implement
- Set up deployment pipeline
- Configure environment variables
- Set up custom domain (optional)
- Enable HTTPS

### Checkpoint
App should be accessible via public URL!

---

## Step 11: Monitoring & Observability

### Tasks
- [ ] Add error tracking
- [ ] Set up logging
- [ ] Monitor performance
- [ ] Create alerts

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| Sentry | https://docs.sentry.io/platforms/python/integrations/fastapi/ | Error tracking |
| Prometheus | https://prometheus.io/docs/introduction/overview/ | Metrics |
| Grafana | https://grafana.com/docs/ | Dashboards |
| Structured Logging | https://www.structlog.org/ | Better logs |

### What to Monitor
- API response times
- Error rates
- Token usage
- Cost per user
- Active users

### Checkpoint
You should be able to see errors and metrics in dashboards.

---

## Step 12: Security Hardening

### Tasks
- [ ] Security audit
- [ ] Input validation
- [ ] SQL injection prevention
- [ ] API security best practices

### Documentation to Read
| Topic | Link | What to Learn |
|-------|------|---------------|
| OWASP API Security | https://owasp.org/www-project-api-security/ | API vulnerabilities |
| FastAPI Security | https://fastapi.tiangolo.com/tutorial/security/ | Security features |
| Pydantic Validation | https://docs.pydantic.dev/latest/concepts/validators/ | Input validation |

### Security Checklist
- [ ] All inputs validated
- [ ] SQL queries parameterized (SQLAlchemy handles this)
- [ ] Passwords properly hashed
- [ ] JWT tokens expire
- [ ] CORS properly configured
- [ ] Rate limiting active
- [ ] Sensitive data not logged
- [ ] Environment variables for secrets

---

## Stretch Goals

### Payment Integration
- [ ] Add Stripe for payments
- [ ] Create subscription tiers
- **Docs**: https://stripe.com/docs/api

### Team/Organization Support
- [ ] Multi-user organizations
- [ ] Role-based access control
- **Docs**: https://casbin.org/docs/overview (RBAC)

### Fine-tuning
- [ ] Allow users to fine-tune models
- **Docs**: https://platform.openai.com/docs/guides/fine-tuning

---

## Final Project Structure

```
04-ai-saas-app/
├── README.md
├── docker-compose.yml
├── .env.example
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── alembic/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── middleware/
│   │   └── utils/
│   └── tests/
│
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│       ├── app/
│       ├── components/
│       └── lib/
│
└── infrastructure/
    └── nginx.conf
```

---

## Self-Check Questions

After completing this project, you should be able to answer:

1. How does JWT authentication work?
2. Why do we need rate limiting?
3. How do you track token usage for billing?
4. What's the difference between frontend and backend deployment?
5. What security considerations are important for AI apps?

---

## Notes
_Add your learning notes here as you progress_

---

**Status**: Not Started  
**Started**: -  
**Completed**: -
