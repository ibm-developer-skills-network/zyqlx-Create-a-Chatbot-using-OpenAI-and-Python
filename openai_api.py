import os
import requests

class OpenAIAPI:
    @staticmethod
    def generate_response(user_message, conversation_history=None):
        if conversation_history is None:
            conversation_history = []
        
        api_key = os.environ.get('OPENAI_API_KEY')
        endpoint = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        messages = conversation_history + [{"role": "user", "content": user_message}]
        
        payload = {
            "model": "gpt-3.5-turbo-1106",
            "messages": messages,
            "max_tokens": 150
        }
        
        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response_data = response.json()
            
            # Log the entire API response for debugging
            print("Response from OpenAI API:", response_data.get('choices', [{}])[0].get('message'))
            
            # Check if choices array is defined and not empty
            if (response_data.get('choices') and 
                len(response_data['choices']) > 0 and 
                response_data['choices'][0].get('message')):
                return response_data['choices'][0]['message']['content']
            else:
                # Handle the case where choices array is undefined or empty
                print("Error: No valid response from OpenAI API")
                return "Sorry, I couldn't understand that."
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return "Sorry, I couldn't understand that."
