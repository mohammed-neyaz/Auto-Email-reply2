# Email Organizer

## Overview
The Email Organizer is a Python-based console application designed to manage email accounts effectively. It fetches emails, summarizes their content, and suggests automated responses using an advanced language model accessed through the GROQ API. The project is aimed at enhancing email productivity by reducing manual effort in reading and responding to emails.

---

## Features

- **Fetch Emails**: Retrieve emails from specified email accounts using IMAP.
- **Summarize Emails**: Generate concise summaries of email content to save time.
- **Generate Responses**: Suggest relevant replies using a powerful LLM accessed via the GROQ API.
- **JSON Storage**: Store fetched emails, summaries, and suggested replies in JSON files for efficient processing and retrieval.

---

## File Structure

```
.
├── emails.json               # Contains fetched emails.
├── summarization.json        # Stores summarized content of emails.
├── replies.json              # Holds generated email responses.
├── fetch_emails.py           # Script to fetch emails using IMAP.
├── summarize_emails.py       # Script for summarizing email content.
├── generate_response.py      # Script to generate responses using the GROQ API.
├── main.py                   # Main script to orchestrate the functionality.
```

---

## How It Works

1. **Fetching Emails**: The `fetch_emails.py` script retrieves emails from configured accounts using IMAP.
2. **Summarizing Emails**: The `summarize_emails.py` script processes the fetched emails and generates summaries stored in `summarization.json`.
3. **Generating Responses**: The `generate_response.py` script uses the GROQ API to generate suggested replies for the summarized emails, saving them in `replies.json`.
4. **Orchestration**: The `main.py` script integrates all functionalities, providing an interactive console-based workflow.

---

## Prerequisites

- **Python 3.8 or higher**
- **IMAP Email Account**: Ensure your email account allows IMAP access.
- **GROQ API Access**: Obtain API credentials for GROQ LLM services.

---

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/mohammed-neyaz/Auto-Email-reply2.git
   cd Auto-Email-reply2
   ```

2. Configure email credentials and GROQ API keys in the respective scripts.

   - Update IMAP server details and email credentials in `fetch_emails.py`.
   - Insert GROQ API credentials in `generate_response.py`.

3. Run the application:

   ```bash
   python main.py
   ```

---

## Usage

- **Interactive Workflow**: Execute `main.py` to perform end-to-end email management.
- **Individual Scripts**:
  - Fetch emails:
    ```bash
    python fetch_emails.py
    ```
  - Summarize emails:
    ```bash
    python summarize_emails.py
    ```
  - Generate responses:
    ```bash
    python generate_response.py
    ```
    
---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- [GROQ API](https://www.groq.com/) for enabling access to advanced LLM capabilities.
- Hugging face libraries for simplifying email access and JSON processing.
