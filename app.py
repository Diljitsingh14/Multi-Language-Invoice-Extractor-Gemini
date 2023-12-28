from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")


def generate(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text


def input_image_value(upload_file):
    if upload_file is None:
        raise FileNotFoundError("No File Found")
    else:
        byte_data = upload_file.getvalue()
        image_parts = [
            {
                "mime_type": upload_file.type,
                "data": byte_data
            }
        ]
        return image_parts


st.set_page_config(page_title="Multi-language Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")
input = st.text_input("Input Prompt : ", key="input")
upload_file = st.file_uploader("Choose an image of the invoice", type=[
                               "jpg", "jpeg", "pdf", "png"])
image = ""

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
 you are an expert in understanding invoices. We will uploaded a image as invoice and
 you will have to answer any question on the based on the upload invoice 
"""

if submit:
    images_data = input_image_value(upload_file)
    response = generate(input, images_data, input_prompt)
    st.subheader("The Response is ")
    st.write(response)
