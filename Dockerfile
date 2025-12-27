# Build stage for Next.js frontend
FROM node:20-slim AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
# Set dummy API URL for build time (it will be proxied via next.config.ts)
RUN npm run build

# Final stage
FROM python:3.13-slim

# Install Node.js runtime for Next.js
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up user for HF Spaces (user id 1000)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Copy backend and install dependencies
COPY --chown=user backend/ $HOME/app/backend/
WORKDIR $HOME/app/backend
RUN pip install --no-cache-dir . && python -m src.nltk_setup

# Copy built frontend
COPY --chown=user --from=frontend-builder /app/frontend/.next $HOME/app/frontend/.next
COPY --chown=user --from=frontend-builder /app/frontend/public $HOME/app/frontend/public
COPY --chown=user --from=frontend-builder /app/frontend/node_modules $HOME/app/frontend/node_modules
COPY --chown=user --from=frontend-builder /app/frontend/package.json $HOME/app/frontend/package.json
COPY --chown=user --from=frontend-builder /app/frontend/next.config.ts $HOME/app/frontend/next.config.ts

# Copy start script
COPY --chown=user start.sh $HOME/app/start.sh
RUN chmod +x $HOME/app/start.sh

# HF Spaces expects port 7860
EXPOSE 7860

ENTRYPOINT ["/home/user/app/start.sh"]
