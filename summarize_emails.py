
from transformers import pipeline
import json

def summarize_emails(emails):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summaries = {}

    for email in emails:
        try:
            summary = summarizer(email["body"], max_length=100, min_length=25, truncation=True, do_sample=False)

            summaries[email["from"]] = summary[0]["summary_text"]
        except Exception as e:
            summaries[email["from"]] = "Error summarizing email."

    with open("summarization.json", "w") as summary_file:
        json.dump(summaries, summary_file, indent=4)
