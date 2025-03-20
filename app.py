import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np
from deep_translator import GoogleTranslator
from streamlit_cropper import st_cropper

# ---- Page Configuration ----
st.set_page_config(page_title="OCR & Translator", page_icon="🌍", layout="wide")

# ---- Custom Styling Using the Provided Color Palette ----
st.markdown(
    """
    <style>
        /* Body background and text styling */
        body {
            background-color: #A5A5A5;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            color: #000000;
        }
        /* Main container styling */
        .stApp {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            margin: 20px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        }
        /* Header styles */
        h1, h2, h3 {
            color: #6552D0;
            font-size: 2.5em;
            text-align: center;
        }
        /* Increase paragraph text size */
        p {
            font-size: 18px;
        }
        /* Text area styling */
        .stTextArea textarea {
            font-size: 18px;
            background-color: #ffffff;
            color: #000000;
            border: 2px solid #6552D0;
            border-radius: 5px;
        }
        /* Sidebar styling */
        .css-1d391kg { 
            background-color: #6552D0;
        }
        .css-1d391kg .stButton>button {
            background-color: #6552D0;
            color: #ffffff;
        }
        /* File uploader label styling */
        .stFileUploader label {
            color: #000000;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Sidebar ----
with st.sidebar:
    st.image(r"D:\al\project1\Resume_Ranking\images\shutterstock_546995980.webp", width=150)
    st.title("OCR & Translator")
    st.write("Extract text and translate using AI.")
    st.write("---")
    st.write("This AI-powered OCR & Translation app extracts text from uploaded images and translates it into multiple languages. Users can crop the image, perform OCR, and translate the extracted text instantly. It features a user-friendly interface with a visually appealing design using Streamlit.")

# ---- Main Title ----
st.title("🌍 AI-Powered OCR & Translator")

# ---- File Uploader ----
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    # ---- Center the Uploaded Image ----
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    # Display the cropping tool on the uploaded image
    st.write("### ✂ Crop the image to select the text area")
    cropped_image = st_cropper(image, aspect_ratio=None)
    
    if cropped_image is not None:
        # Convert the cropped image to grayscale for OCR processing
        gray = cv2.cvtColor(np.array(cropped_image), cv2.COLOR_RGB2GRAY)
        
        # Perform OCR on the cropped image
        text = pytesseract.image_to_string(gray, lang="eng+fra+spa+deu+chi_sim+hin+ara+mar").strip()

        st.write("### 📝 Extracted Text")
        st.text_area("Extracted Text", text, height=200, key="extracted_text")
        
        st.write("### 🌍 Translate Text")
        lang_options = {
            "English": "en",
            "French": "fr",
            "Spanish": "es",
            "German": "de",
            "Chinese": "zh-cn",
            "Hindi": "hi",
            "Arabic": "ar",
            "Marathi" :"mr"
        }
        selected_languages = st.multiselect("Select languages", list(lang_options.keys()))
        
        if selected_languages and text:
            translations = {}
            for lang in selected_languages:
                translator = GoogleTranslator(source="auto", target=lang_options[lang])
                translations[lang] = translator.translate(text)
            
            st.write("### 📖 Translations")
            for lang, translated_text in translations.items():
                st.write(f"**{lang}:**")
                st.text_area(f"Translation in {lang}", translated_text, height=200, key=f"trans_{lang}")

st.write("### 🛠 How to Use:")
st.markdown(
    """
    1. **Upload an Image**: Click the upload button and select a file.
    2. **Crop the Image**: Use the cropping tool to select the text region.
    3. **Extract & Translate**: The app performs OCR on the cropped area and translates the extracted text into your chosen languages.
    """
) 