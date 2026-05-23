# AI Assistant Web App

A simple web interface for Google Gemini AI with LangSmith tracing.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your API keys:
```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT="your-project-name"
GOOGLE_API_KEY=your-google-api-key
```

3. Run the app:
```bash
python app.py
```

4. Open http://localhost:5000 in your browser

## Deploy to Vercel

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
vercel
```

4. Add environment variables in Vercel dashboard:
   - Go to your project settings
   - Add all variables from your `.env` file
   - Redeploy

## Environment Variables Required

- `GOOGLE_API_KEY` - Your Google AI API key
- `LANGSMITH_API_KEY` - Your LangSmith API key
- `LANGSMITH_PROJECT` - Your LangSmith project name
- `LANGSMITH_TRACING` - Set to "true"
- `LANGSMITH_ENDPOINT` - https://api.smith.langchain.com
