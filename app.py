from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
from langsmith import wrappers

load_dotenv()

app = Flask(__name__)

def get_ai_response(user_question):
    try:
        gemini_client = genai.Client(vertexai=False)
        
        client = wrappers.wrap_gemini(
            gemini_client,
            tracing_extra={
                "tags": ["gemini", "python"],
                "metadata": {
                    "integration": "google-genai",
                },
            },
        )
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_question,
        )
        
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    answer = get_ai_response(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
