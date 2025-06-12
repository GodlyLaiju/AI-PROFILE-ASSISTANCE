## AI-PROFILE-ASSISTANCE

A Gradio-powered chat interface for interacting with an AI profile of **Godly Laiju**, powered by PDF summarization and Gemini API.

---

### Features

* **PDF Summary Generation**: Uses Hugging Face transformers to extract and summarize content from a PDF (e.g., resume), outputting to `summary.txt`.
* **Natural Language Chat**: Leverages Gemini (OpenAI) to answer questions about career, qualifications, achievements, and contact details based on the generated summary.
* **Interactive UI**: Gradio interface for PDF upload, summary review, and conversational Q\&A.

---

### Project Structure

```text
AI-PROFILE-ASSISTANCE/
├── src/
│   ├── main.py           # Gradio app entrypoint
│   ├── generate_summary.py  # PDF loader and Hugging Face summarizer
│   └── load_pdf.py       # PDF parsing utilities
├── summary.txt           # Generated summary of the PDF (e.g., resume)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (keys & paths)
└── README.md             # This file
```

---

## Setup & Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/your-org/AI-PROFILE-ASSISTANCE.git
   cd AI-PROFILE-ASSISTANCE
   ```
2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Environment Variables** (`.env`):

   ```dotenv
   HUGGINGFACE_API_KEY=your_huggingface_token
   GEMINI_API_KEY=your_gemini_api_key
   ```
2. **Summary File**:

   * After running the summarizer, `summary.txt` will contain a Markdown-friendly overview of your resume content.

---

## Usage

1. **Generate PDF Summary**:

   ```bash
   python src/generate_summary.py --input $PDF_PATH --output summary.txt
   ```
2. **Start the Chat Interface**:

   ```bash
   python src/main.py
   ```
3. **Interact**:

   * Upload or confirm `summary.txt` in the Gradio UI.
   * Ask questions about Godly Laiju’s career, skills, achievements, or how to reach out.

---

## Example Summary (`summary.txt`)

> A concise Markdown summary of the uploaded PDF will appear here once generated. Include key sections like Education, Experience, Skills, and Achievements.

---

*Enjoy exploring the My profile!*
