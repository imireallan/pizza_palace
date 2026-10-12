# Pizza Palace — Billing System

Billing-only system (no persistence). Records orders (pizza size + toppings) and generates itemized receipts with 5% tax (rounded up).

## Setup

Requires Python 3.11+ with `uv` (or pip) and Node 18+.

```bash
# Backend
make server        # Django: localhost:8000

# Full stack (backend + frontend)
make dev           # Django:8000 + React Router:5173

# Or manually
uv sync
python manage.py runserver 8000        # backend
cd frontend && npm install && npm run dev  # frontend (localhost:5173)
```

## Features
- React Router v7 frontend (`frontend/app/components/OrderForm.tsx`)
- Django backend (`billing/engine.py`, `core/urls.py` endpoint `/api/billing/`)
- CORS configured for `localhost:5173`
- Tailwind-styled form with chip-style toppings, receipt modal
- Manual QA verified at each phase (engine, endpoint, UI, styling)

## Repository
Feature branch: `feature/billing` (open PR #1 at github.com/imireallan/pizza_palace)

## Requirements covered
- Size/topping selection, add/remove pizzas before submit
- Validation (unknown size, unknown topping, at least one pizza)
- Plain-text receipt (subtotal, 5% TAX rounded up, total)
- In-memory (no persistence per ADR-0001)
