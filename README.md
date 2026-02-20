🤖 AI Job Search Agent: From Inbox Chaos to Strategic Clarity
Product Vision: To eliminate the "administrative tax" of the job search, allowing high-level professionals to spend 100% of their cognitive energy on interviews and relationship building, not inbox management.

💡 Why I Built This (The Problem)
In a modern job search, the "mental load" is the silent productivity killer. As a Product Leader with 14 years of experience, I noticed a recurring friction point: Information Fragmentation.

Between LinkedIn pings, recruiter emails, and automated portal updates, the signal-to-noise ratio in a Gmail inbox is incredibly low. I found myself spending 60+ minutes every morning just "sorting" before I could actually "work."

I built this agent to act as a 0-cost Chief of Staff—turning a chaotic inbox into a strategic morning briefing.

🎯 The Value Proposition
Zero Cost: Built using Python and the Groq AI API (Llama 3/Mixtral), utilizing high-speed inference without a monthly SaaS subscription.

Reduced Context Switching: No need to jump between spreadsheets and email. The agent brings the data to you.

Action-Oriented: It doesn't just "summarize"; it categorizes based on Urgency and Opportunity.

📊 Example Output (The Morning Briefing)
The agent generates a structured markdown report every morning at 8:00 AM:

📅 Daily Job Search Briefing - Oct 24
🔥 URGENT (Action Required Today)

Company A: Recruiter 'Sarah' sent a scheduling link for the Final Round. (Received 4:30 PM yesterday).

Company B: Follow-up needed on the technical take-home assignment due Friday.

💼 PIPELINE UPDATES

Company C: Moved to "Interviewing" stage (Confirmed by automated email).

Company D: Application acknowledged. No action needed.

🌱 NETWORKING & MOMENTUM

You haven't replied to 'Mark' at Google in 3 days. Send a quick "thank you" for the referral.

✅ TOP 3 GOALS FOR TODAY

Schedule Company A Final Round.

Submit Company B Take-home.

Ping 2 new networking leads in Product.

🛠️ Technical Architecture & Data Flow
The agent follows a lean, secure data pipeline:

Authentication: Secure OAuth2 connection to Gmail API (Read-only access).

Filtering: Python script pulls threads from the last 24–48 hours tagged with keywords (e.g., "Interview," "Application," "Recruiter").

Inference: Content is passed to Groq AI using a custom System Prompt designed for high-accuracy extraction and professional tone.

Delivery: Outputs a clean Markdown file or sends a summary to a designated Slack/Discord/Email.

🚀 Getting Started
Prerequisites
Python 3.10+
Gmail API Credentials (credentials.json)
Free Groq API Key

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

Here are the updates you requested:

📊 QUICK STATS:
- Job emails: 7 (including interview reminders and job openings)
- Networking emails: 2
- Rejection emails: 0
- Interview emails: 5

🔥 URGENT:
You have an interview tomorrow (Thursday, February 19, 2026) at 1:00 PM EST

## Author

Built by Abhishek Sahay — Product Leader with 14 years experience, staying hands-on with AI tools.

Connect with me on [LinkedIn](https://www.linkedin.com/in/abisahay/)

## License
MIT — free to use and modify
