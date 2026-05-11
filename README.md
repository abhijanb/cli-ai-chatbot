# AI Chatbot CLI

A lightweight, terminal-based chatbot powered by Google's Gemini AI. This application allows you to interact with advanced generative models directly from your command line, with responses structured in JSON format for easy parsing or integration.

---

## 🚀 Features

- **Gemini Powered**: Built on the latest `google-genai` SDK using the `gemini-2.5-flash` model.
- **JSON Structured Responses**: Automatically requests responses in a consistent JSON format (`{"answer": "..."}`).
- **Environment Driven**: Secure configuration using `.env` files for API key management.
- **Minimalist Design**: Zero-bloat CLI interface for quick interactions.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **AI Integration**: [Google GenAI SDK](https://github.com/googleapis/python-genai)
- **Configuration**: `python-dotenv`
- **Dependencies**: Managed via `requirements.txt`

## 📋 Prerequisites

- Python 3.9 or higher.
- A Google AI Studio API Key. Get one [here](https://aistudio.google.com/app/apikey).

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/abhijanb/cli-ai-chatbot.git
   cd cli-ai-chatbot
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```
   Add your API key to the `.env` file:
   ```env
   API_KEY=[GCP_API_KEY]
   ```

## 🚀 Usage

Start the chatbot by running the `main.py` script:

```bash
python main.py
```

### Commands:
- **Ask anything**: Type your query at the prompt and press Enter.
- **Exit**: Type `exit` to close the application.

## 📄 Example Interaction

```text
what you want to know> What is the capital of France?
{"answer": "The capital of France is Paris."}
```