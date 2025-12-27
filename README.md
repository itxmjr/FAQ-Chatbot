---
title: FAQ Chatbot
emoji: 🤖
colorFrom: gray
colorTo: green
sdk: docker
pinned: false
license: mit
---

# 🤖 FAQ Chatbot

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15+-000000.svg?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.6+-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

A smart, lightweight FAQ chatbot backend built with Python and FastAPI. This service uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to accurately match user queries against a predefined knowledge base, providing instant and relevant API responses for modern frontends (like Next.js).

## ✨ Features

- **Natural Language Understanding**: Uses NLP techniques (Tokenization, N-grams) to understand the intent behind user queries.
- **High Accuracy Matching**: Powered by Scikit-learn's TF-IDF vectorization and cosine similarity scoring.
- **API-First Design**: Optimized for Next.js or other modern frontend integrations.
- **RESTful Endpoints**: Dedicated endpoints for asking questions, retrieving categories, and getting suggestions.
- **Easy Customization**: The knowledge base is a simple JSON file, making it easy to update or expand.

## 🚀 Demo

<p align="center">
  <img src="./assets/demo.gif" alt="FAQ Chatbot Demo" width="800" />
</p>

## 🛠️ Tech Stack

- **[Python](https://www.python.org/)**: Core programming language.
- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern, fast (high-performance), web framework for building APIs.
- **[Uvicorn](https://www.uvicorn.org/)**: ASGI server for FastAPI.
- **[Scikit-learn](https://scikit-learn.org/)**: Machine learning library for vectorization and similarity calculation.
- **[NLTK](https://www.nltk.org/)**: Natural Language Toolkit for text preprocessing. NLTK resources are automatically managed via `nltk_setup.py`.

## 📦 Installation

Ensure you have Python 3.13 or higher installed.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/itxmjr/FAQ-Chatbot.git
    cd FAQ-Chatbot
    ```

2.  **Install Dependencies**
    It is recommended to use a virtual environment.

    Using `pip`:
    ```bash
    pip install .
    ```

    Using `uv` (if applicable):
    ```bash
    uv sync
    ```

## 🎮 Usage

### 🐍 Backend (FastAPI)
The backend is located in the `backend/` directory.

1.  **Install & Setup**:
    ```bash
    cd backend
    pip install .
    python -m src.nltk_setup
    ```
2.  **Run the server**:
    ```bash
    uvicorn src.api:app --reload --port 8000
    ```
    Access API docs at `http://localhost:8000/docs`.

### ⚛️ Frontend (Next.js)
The frontend is located in the `frontend/` directory.

1.  **Install dependencies**:
    ```bash
    cd frontend
    npm install
    ```
2.  **Run the development server**:
    ```bash
    npm run dev
    ```
    Access the app at `http://localhost:3000`.

## 🧪 Testing

### Backend Tests
Run the backend tests using `pytest`:
```bash
cd backend
pytest
```

## 📂 Project Structure

```
FAQ-Chatbot/
├── backend/               # FastAPI backend service
│   ├── src/               # Backend source code
│   │   ├── api.py         # API endpoints
│   │   ├── chatbot.py     # Core chatbot logic
│   │   └── ...
│   ├── pyproject.toml     # Project configuration
│   └── ...
├── frontend/              # Next.js frontend application
│   ├── src/               # Frontend source code (pages, components)
│   ├── public/            # Static assets
│   └── ...
├── .gitignore             # Root-level ignore file
└── README.md              # Project documentation
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 🌍 Deployment

This application is deployed on Hugging Face Spaces.

Space: https://huggingface.co/spaces/itxmjr/FAQ-Chatbot

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built with ❤️ by M Jawad ur Rehman.</sub>
</div>
