AI-Powered OCR & Translator
This AI-powered application extracts text from images using Optical Character Recognition (OCR) and translates the extracted text into multiple languages. It features a user-friendly interface with a cropping tool, multi-language OCR, and an integrated translation system.

Features
Upload an image for text extraction.
Crop the image to focus on the text area.
Supports multiple languages for OCR including English, French, Spanish, German, Chinese, Hindi, Arabic, and Marathi.
Translate extracted text into multiple languages.
User-friendly interface with Streamlit.
Installation
Clone the Repository
git clone https://github.com/your-username/ocr-translator.git
cd ocr-translator

Set Up a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows

Install Dependencies
pip install -r requirements.txt

Install Tesseract OCR
You need to install Tesseract OCR separately.

Windows
Download and install from https://github.com/UB-Mannheim/tesseract/wiki
Then, add the Tesseract installation path to your system environment variables.

Linux
sudo apt install tesseract-ocr

macOS
brew install tesseract

Running the Application
After installation, run the Streamlit app using
streamlit run app.py

How to Use
Upload an Image by clicking the upload button and selecting an image.
Crop the Image using the cropping tool to select the text area.
Extract Text where OCR will recognize the text from the cropped section.
Translate by choosing target languages, and the app will translate the extracted text.
Built With
Streamlit for UI and interactivity
Tesseract OCR for text extraction
OpenCV and PIL for image processing
Deep Translator for translation

License
This project is licensed under the MIT License.



