### Project Book OWL
A complete Python project for a web application 
called ‘Book Owl’ that converts PDF files to audiobooks

1. **Flask Web Application**:
    - A single-page web application with an upload field where users can upload a PDF file.
    - The application should able to convert the PDF to an MP3 audiobook using AI voice.


2. **PDF to Audio Conversion**:
    - Use PyPDF2 to read the PDF file.
    - Use gTTS (Google Text-to-Speech) to convert the text to speech.
    - Use pydub to handle audio file manipulation.


3. **Simple UI Design**:
    - Include a header with the word ‘Book Owl’ as the logo. 
    - The home page should have the logo centered in the header.
    - Below the header, include a stylish dropzone for file uploads and a modern ‘Convert to Audio’ button.
    - Include a placeholder footer with the logo and standard SaaS links such as About, Products, Terms, etc.


4. **Project Structure**:
    - Organize the project with appropriate directories for templates and static files.
    - Provide a requirements.txt file listing all dependencies.
