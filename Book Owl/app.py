
from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfFileReader
from gtts import gTTS
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/convert', methods=['POST'])
def convert():
    pdf_file = request.files['pdf_file']
    pdf_reader = PdfFileReader(pdf_file)
    text = ''
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extract_text()
    
    tts = gTTS(text)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    
    return send_file(audio_file, as_attachment=True, download_name='audiobook.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
