from transformers import pipeline
import json

def generate_responses():
    # Read the summarization file
    try:
        with open("summarization.json", "r") as summary_file:
            summaries = json.load(summary_file)
        
        # Initialize the text generation pipeline
        pipe = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
        
        responses = {}
        
        # Generate response for each summary
        for email_from, summary in summaries.items():
            messages = [
    {
        "role": "user",
        "content": (
            f"Compose a professional email from Mohammed Neyaz, a Software Developer. "
            f"Address the following summary in a professional, solution-oriented tone:\n\n{summary}"
        )
    }
]
            response = pipe(messages, max_new_tokens=200)
            responses[email_from] = response[0]['generated_text']
        
        # Save responses to reply.json
        with open("reply.json", "w") as reply_file:
            json.dump(responses, reply_file, indent=4)
            
    except Exception as e:
        print(f"Error generating responses: {str(e)}")
