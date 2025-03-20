# 🌍 AI-Powered OCR & Translator

This AI-powered application extracts text from images using Optical Character Recognition (OCR) and translates the extracted text into multiple languages. It features a user-friendly interface with a cropping tool, multi-language OCR, and an integrated translation system.

## 🚀 Features
- Upload an image for text extraction.
- Crop the image to focus on the text area.
- Supports multiple languages for OCR (`English, French, Spanish, German, Chinese, Hindi, Arabic, Marathi`).
- Translate extracted text into multiple languages.
- User-friendly interface with Streamlit.

## 📥 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/ocr-translator.git
cd ocr-translator
2️⃣ Set Up a Virtual Environment (Optional but Recommended)
sh
Copy code
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3️⃣ Install Dependencies
sh
Copy code
pip install -r requirements.txt
4️⃣ Install Tesseract OCR
You need to install Tesseract OCR separately.

🔹 Windows
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki
Then, add the Tesseract installation path to your system environment variables.

🔹 Linux
sh
Copy code
sudo apt install tesseract-ocr
🔹 macOS
sh
Copy code
brew install tesseract
▶ Running the Application
After installation, run the Streamlit app using:

sh
Copy code
streamlit run app.py
📌 How to Use
Upload an Image: Click the upload button and select an image.
Crop the Image: Use the cropping tool to select the text area.
Extract Text: OCR will recognize the text from the cropped section.
Translate: Choose target languages, and the app will translate the extracted text.
🛠 Built With
Streamlit - For UI and interactivity
Tesseract OCR - For text extraction
OpenCV & PIL - For image processing
Deep Translator - For translation
🤝 Contributing
Pull requests are welcome! If you have suggestions, feel free to open an issue.

📜 License
This project is licensed under the MIT License.

