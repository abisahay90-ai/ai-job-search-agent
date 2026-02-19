# ai-job-search-agent
A free AI agent that reads your Gmail and gives you a daily job search briefing. Built with Python + Groq AI
# 🤖 AI Job Search Agent

A free AI agent that reads your Gmail every morning and gives you a daily job search briefing — built with Python + Groq AI (completely free).

## What It Does

Every morning it analyzes your inbox and tells you:
- 🔥 What needs urgent replies today
- 💼 Interview requests and application updates
- 🌱 Networking follow-ups you shouldn't miss
- ✅ Your top 3 action items for the day

## Built With (All Free)
- Python
- Gmail API (Google Cloud — free tier)
- Groq AI — Llama 3.3 70B (free)

## Setup Guide

### 1. Clone this repo
```bash
git clone https://github.com/YOUR-USERNAME/ai-job-search-agent.git
cd ai-job-search-agent
```

### 2. Install dependencies
```bash
pip install groq google-auth google-auth-oauthlib google-api-python-client
```

### 3. Get your free API keys
- **Groq API key** (free): console.groq.com
- **Gmail API credentials**: console.cloud.google.com

### 4. Add your keys
Open `agent.py` and paste your Groq API key where indicated.
Place your `credentials.json` from Google Cloud in the same folder.

### 5. Run it
```bash
python agent.py
```

A browser window will open to connect your Gmail. After that it runs automatically.

## Sample Output

![Sample Briefing](sample_report.png)

## Author

Built by Abhishek Sahay — Product Leader with 10 years experience, staying hands-on with AI tools.

Connect with me on [LinkedIn](https://linkedin.com/in/YOUR-LINKEDIN)

## License
MIT — free to use and modify
