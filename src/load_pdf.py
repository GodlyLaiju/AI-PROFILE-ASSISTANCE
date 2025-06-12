from pypdf import PdfReader


class LoadProfile:
    def __init__(
        self,
        name: str = "Me",
        resume: str = "me/linkedin.pdf",
    ):
        self.name = name
        self.resumepdf = resume
        self.content = ""

    def load_pdf(self):
        """Load the LinkedIn PDF and extract text."""
        # Load the PDF file
        reader = PdfReader(self.resumepdf)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.content += text

        return self.content
