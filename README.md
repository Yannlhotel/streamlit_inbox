# Mini Mailbox

A lightweight Streamlit application to visualize a mini email inbox and reply to emails either manually or with AI assistance using an Ollama LLM model.

## Features

* Display a list of emails (Inbox) with sender and subject.
* View the full content of a selected email.
* Reply to emails:

  * **Manual mode**: write your own reply.
  * **AI mode**: generate a professional and polite reply using a small LLM (Deepseek) from Ollama.
* Include extra information in AI replies.
* Editable AI-generated replies before sending.

## Project Structure

```
streamlit_ui/
├─ agents/
│  └─ answer_email.py         # Generates AI email replies using Ollama LLM
├─ db_inbox/
│  └─ mail_inbox.json         # Sample email data in JSON
├─ boxmail.py                 # Main Streamlit app
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yannlhotel/streamlit_inbox.git
cd streamlit_inbox
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install langchain-ollama streamlit
```

4. Make sure Ollama is installed locally and the Deepseek model deepseek-r1:1.5b is available.

## Usage

Run the Streamlit app:

```bash
streamlit run streamlit_ui/boxmail.py
```

* Click on a bubble next to an email to view it.
* Click **Answer** to open the reply column.
* Choose **Manual** or **AI** mode for replying.
* Edit the AI-generated reply if needed and click **Send Reply**.

## Notes

* AI replies are generated using the Ollama `Deepseek` small model.
* The app currently simulates sending emails; no real email is sent.
* The Inbox displays a maximum of 5 emails by default.
