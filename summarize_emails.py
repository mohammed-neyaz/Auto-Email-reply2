from groq import Groq
import json
import os

def summarize_emails(emails):
    # Initialize Groq client
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    email_groups = {}
    
    # Group emails by sender
    for email in emails:
        sender = email["from"]
        
        # Skip no-reply emails
        if "no-reply" in sender.lower() or "noreply" in sender.lower():
            continue
            
        if sender not in email_groups:
            email_groups[sender] = []
        # Store both subject and body for better context
        email_groups[sender].append({
            "subject": email["subject"],
            "body": email["body"]
        })

    summaries = {}
    for sender, messages in email_groups.items():
        try:
            # If multiple emails exist for the same sender
            if len(messages) > 1:
                prompt = f"""Please provide a consolidated summary of these related emails from the same sender:

                Emails:
                {'\n\n'.join([f'Subject: {msg["subject"]}\nBody: {msg["body"]}' for msg in messages])}

                Combined Summary:"""
            else:
                # For single email
                msg = messages[0]
                prompt = f"""Please provide a concise summary of this email:

                Subject: {msg["subject"]}
                Body: {msg["body"]}

                Summary:"""

            # Call Groq API
            response = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                model="mixtral-8x7b-32768",
                temperature=0.3,
                max_tokens=150,
            )

            summaries[sender] = response.choices[0].message.content.strip()
        except Exception as e:
            summaries[sender] = f"Error summarizing email: {str(e)}"

    with open("summarization.json", "w") as summary_file:
        json.dump(summaries, summary_file, indent=4)
