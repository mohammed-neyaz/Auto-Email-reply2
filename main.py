import json
from fetch_emails import fetch_emails
from summarize_emails import summarize_emails
from generate_response import generate_responses

def main():
    email_user = 'your@gmail.com'   #enter you gmail ID here
    email_password = 'xxxx xxxx xxxx xxxx'   #Enter your google app password here

    print("Logging in...")
    emails = fetch_emails(email_user, email_password)
    print("Fetching emails...")

    with open("emails.json", "w") as email_file:
        json.dump(emails, email_file, indent=4)
    print("Emails saved to emails.json.")

    summarize_emails(emails)
    print("Emails summarized.")
    
    generate_responses()
    print("Responses generated and saved to reply.json")

if __name__ == "__main__":
    main()
