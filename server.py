from flask import Flask, request, jsonify, send_from_directory
import os
from openai_api import OpenAIAPI

app = Flask(__name__, static_folder='public')
port = int(os.environ.get('PORT', 3000))

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('public', path)

@app.route('/getChatbotResponse', methods=['POST'])
def get_chatbot_response():
    data = request.get_json()
    user_message = data.get('userMessage')
    
    # Use OpenAI API to generate a response
    chatbot_response = OpenAIAPI.generate_response(user_message)
    
    # Send the response back to the client
    return jsonify({'chatbotResponse': chatbot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
