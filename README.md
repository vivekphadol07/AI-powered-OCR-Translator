# AI-Powered OCR & Translator

## Overview
This AI-powered application extracts text from images using Optical Character Recognition (OCR) and translates it into multiple languages using deep learning models. The system provides a user-friendly interface built with Streamlit, allowing users to upload images, crop selected text areas, and translate extracted text instantly.

## Features
- **Upload Images**: Supports PNG, JPG, and JPEG formats.
- **Crop Image**: Select a specific text area for OCR processing.
- **OCR Extraction**: Uses Tesseract OCR for text recognition.
- **Multi-language Translation**: Translate extracted text into various languages including English, French, Spanish, German, Chinese, Hindi, Arabic, and Marathi.
- **Streamlit UI**: Responsive and visually appealing interface.

## Installation

### Prerequisites
Ensure you have Python installed (>=3.7). Install the required dependencies using the command below:
```bash
pip install streamlit pytesseract pillow opencv-python numpy deep-translator streamlit-cropper
```

### Run the Application
```bash
streamlit run app.py
```

## Usage
1. **Upload an Image**: Select an image containing text.
2. **Crop the Image**: Use the cropping tool to define the text area.
3. **Extract & Translate**: The application extracts text and translates it into the selected languages.

## Technologies Used
- **Streamlit**: Front-end framework for web-based applications.
- **Tesseract OCR**: Optical Character Recognition for text extraction.
- **OpenCV**: Image processing library.
- **Deep Translator (Google Translator API)**: Multi-language translation support.
- **PIL (Pillow)**: Image handling and manipulation.

## Folder Structure
```
📂 OCR_Translator_App
├── 📜 app.py  # Main Streamlit application script
├── 📂 images  # Folder to store uploaded images
├── 📜 requirements.txt  # Required dependencies
└── 📜 README.md  # Project documentation
```

## License
This project is open-source and available under the MIT License.

