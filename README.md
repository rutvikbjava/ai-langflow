# AI Assistant Web App

A simple web interface for Google Gemini AI with LangSmith tracing.

![CI/CD](https://github.com/rutvikbjava/ai-langflow/workflows/CI/CD%20Pipeline/badge.svg)

## Features

- 🤖 Google Gemini AI integration
- 📊 LangSmith tracing for monitoring
- 🎨 Clean, modern UI
- 🚀 Auto-deploy with Vercel CI/CD
- ✅ GitHub Actions for testing

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

## Deploy to Vercel (with Auto CI/CD)

### Option 1: Vercel Dashboard (Recommended - Auto CI/CD)

1. Go to [vercel.com](https://vercel.com) and sign in with GitHub
2. Click "Add New Project"
3. Import your `ai-langflow` repository
4. Configure:
   - Framework Preset: Other
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
5. Add Environment Variables:
   - `GOOGLE_API_KEY`
   - `LANGSMITH_API_KEY`
   - `LANGSMITH_PROJECT`
   - `LANGSMITH_TRACING`
   - `LANGSMITH_ENDPOINT`
6. Click "Deploy"

**CI/CD is now automatic!** Every push to `main` branch will auto-deploy.

### Option 2: Vercel CLI

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
vercel --prod
```

4. Add environment variables in Vercel dashboard

## Environment Variables Required

- `GOOGLE_API_KEY` - Your Google AI API key
- `LANGSMITH_API_KEY` - Your LangSmith API key
- `LANGSMITH_PROJECT` - Your LangSmith project name
- `LANGSMITH_TRACING` - Set to "true"
- `LANGSMITH_ENDPOINT` - https://api.smith.langchain.com
