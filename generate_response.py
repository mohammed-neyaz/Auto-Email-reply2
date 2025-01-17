import json
import os
from groq import Groq

def generate_responses():
    # Initialize Groq client
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    # Read emails from emails.json
    try:
        with open("emails.json", "r") as file:
            emails = json.load(file)
    except FileNotFoundError:
        print("Error: emails.json not found")
        return
    
    # Store all responses
    responses = []
    
    # Generate response for each email
    for email in emails:
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant who can generate short emails based on the context of the email body. Keep the tone professional and friendly"
                    },
                    {
                        "role": "user",
                        "content": email['body']
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            
            response = {
                "original_email": email,
                "reply": chat_completion.choices[0].message.content
            }
            responses.append(response)
            
        except Exception as e:
            print(f"Error generating response for email: {e}")
            continue
    
    # Save responses to replies.json
    try:
        with open("replies.json", "w") as file:
            json.dump(responses, file, indent=4)
    except Exception as e:
        print(f"Error saving responses to file: {e}")
