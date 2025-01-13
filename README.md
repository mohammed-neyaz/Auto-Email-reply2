# Auto Email Reply Project

Welcome to the **Auto Email Reply** project! This repository contains a Python-based application that automates email fetching, summarization, and response generation using state-of-the-art NLP models from Hugging Face.

---

## Features

1. **Email Fetching**:
   - Securely connects to your email inbox to fetch emails.
   - Extracts email metadata such as sender, subject, and body content.

2. **Summarization**:
   - Summarizes lengthy email content for quick understanding.
   - Uses a summarization pipeline powered by `facebook/bart-large-cnn`.

3. **Response Generation**:
   - Generates contextually relevant email replies.
   - Leverages `gpt2` or fine-tuned models for personalized responses.

4. **JSON Integration**:
   - Stores fetched emails, summaries, and generated replies in structured JSON files for further use.

---

## Repository Structure

- `fetch_emails.py`: Handles email fetching using the IMAP protocol.
- `summarize_emails.py`: Summarizes email bodies for concise representation.
- `generate_response.py`: Generates responses to emails based on their content.
- `main.py`: Orchestrates the entire workflow of fetching, summarizing, and responding.
- `.env`: Contains sensitive credentials and API keys (ensure it is kept secure).
- `emails.json`: Stores fetched emails in JSON format.
- `summarization.json`: Stores summarized emails.
- `reply.json`: Stores generated replies.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohammed-neyaz/Auto-Email-reply2.git
   cd Auto-Email-reply2
   ```
2. Add your Email id and Google app password in the main.py file

```
   EMAIL_USER="your_email@example.com"
   EMAIL_PASSWORD="your_email_password"
```
3. Add your API keys to the `.env` file:

   ```
   GROQ_API_KEY="your_api_key"
   ```

4. Run the main script:

   ```bash
   python main.py
   ```

---

## Usage

1. **Fetch Emails**:
   The script fetches all emails from the inbox and stores them in `emails.json`.

2. **Summarize Emails**:
   Emails are summarized using NLP techniques and saved to `summarization.json`.

3. **Generate Replies**:
   Based on the email content, replies are generated and stored in `reply.json`.

---

## Dependencies

- Python 3.8+
- `transformers`
- `imaplib`
- `email`
- `dotenv`

---

## Contributing

We welcome contributions! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Author

Mohammed Neyaz 

---

## Acknowledgments

- Hugging Face for their amazing NLP models.
- Open-source contributors for making development easier.

Happy Automating!

