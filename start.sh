#!/bin/bash

# Start the FastAPI backend on port 8000
echo "Starting FastAPI backend..."
cd $HOME/app/backend
uvicorn src.api:app --host 0.0.0.0 --port 8000 &

# Start the Next.js frontend on port 7860
echo "Starting Next.js frontend..."
cd $HOME/app/frontend
npm run start -- -p 7860
