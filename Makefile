.PHONY: dev server ui

# Start Django backend (port 8000) + React Router frontend (port 5173)
dev:
	@echo "Starting backend (Django) + frontend (React Router v7)..."
	(uv run python manage.py runserver 8000 &) && (cd frontend && npm run dev &) && echo "Servers running: Django:8000 Frontend:5173"

# Django only
server:
	uv run python manage.py runserver 8000

# Preview URL for visual QA
ui:
	@echo "Open frontend preview at: http://localhost:5173 (Django API: http://localhost:8000)"
