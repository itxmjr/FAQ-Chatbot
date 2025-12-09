---
title: CodeAlpha FAQ Chatbot
emoji: 🤖
colorFrom: red
colorTo: yellow
sdk: streamlit
sdk_version: 1.51.0
app_file: app.py
pinned: false
license: mit
---

# 🤖 CodeAlpha FAQ Chatbot

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51+-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.7+-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

A smart, lightweight FAQ chatbot built with Python and Streamlit. This app uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to accurately match user queries against a predefined knowledge base, providing instant and relevant answers.

## ✨ Features

- **Natural Language Understanding**: Uses NLP techniques (Tokenization, N-grams) to understand the intent behind user queries.
- **High Accuracy Matching**: Powered by Scikit-learn's TF-IDF vectorization and cosine similarity scoring.
- **Dual Interface**: Interact via a web UI (Streamlit) or a command-line interface (CLI).
- **Confidence Metrics**: Displays similarity scores to transparently show how well a question matches.
- **Easy Customization**: The knowledge base is a simple JSON file, making it easy to update or expand.

## 🚀 Demo

*(Add a screenshot or GIF of your application here)*

## 🛠️ Tech Stack

- **[Python](https://www.python.org/)**: Core programming language.
- **[Streamlit](https://streamlit.io/)**: Framework for building the web interface.
- **[Scikit-learn](https://scikit-learn.org/)**: Machine learning library for vectorization and similarity calculation.
- **[NLTK](https://www.nltk.org/)**: Natural Language Toolkit for text preprocessing. NLTK resources are automatically managed via `nltk_setup.py`.

## 📦 Installation

Ensure you have Python 3.13 or higher installed.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/CodeAlpha/CodeAlpha_FAQ_Chatbot.git
    cd CodeAlpha_FAQ_Chatbot
    ```

2.  **Install Dependencies**
    It is recommended to use a virtual environment.

    Using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

    Using `uv` (if applicable):
    ```bash
    uv sync
    ```

## 🎮 Usage

### Option 1: Web Interface (Streamlit)
For a visual, interactive experience:
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### Option 2: Command Line Interface (CLI)
To chat directly from your terminal:
```bash
python -m src.app_cli
```

### Initial Setup
The application will automatically check for and download necessary NLTK resources (stopwords, punkt, etc.) the first time you run it, using `src/nltk_setup.py`.

## 📂 Project Structure

```
CodeAlpha_FAQ_Chatbot/
├── app.py                 # Main Streamlit application entry point
├── data/
│   └── faqs.json          # Knowledge base (JSON format)
├── src/
│   ├── app_cli.py         # Command-line interface for the chatbot
│   ├── chatbot.py         # Core Chatbot class implementation
│   ├── vectorizer.py      # TF-IDF vectorization logic
│   ├── similarity.py      # Cosine similarity calculation
│   ├── nltk_setup.py      # Automated NLTK resource downloader
│   ├── preprocessing.py   # Text cleaning and tokenization
│   └── data_loader.py     # JSON data loading utilities
├── tests/                 # Unit tests
└── requirements.txt       # Project dependencies
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

Space: https://huggingface.co/spaces/aibymjr/CodeAlpha_FAQ_Chatbot

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built with ❤️ by M Jawad ur Rehman using Streamlit and Python.</sub>
</div>
