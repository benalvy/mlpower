import easyocr
from PIL import Image
import gradio as gr

# Initialize the EasyOCR Reader
reader = easyocr.Reader(['en', 'hi'])  # You can specify the languages here

# Function to extract text from the image
def ocr_image(image):
    extracted_text = reader.readtext(image)
    # Combine the text results into a single string
    return " ".join([text[1] for text in extracted_text])

# Function to search for a keyword in the extracted text
def search_keyword(extracted_text, keyword):
    if keyword.lower() in extracted_text.lower():
        return f"'{keyword}' found in the text!"
    else:
        return f"'{keyword}' not found in the text."

# Combined function for OCR and keyword search
def process_image(image, keyword):
    extracted_text = ocr_image(image)
    search_result = search_keyword(extracted_text, keyword)
    return extracted_text, search_result

# Gradio interface for uploading image and searching keyword
gr_interface = gr.Interface(
    fn=process_image,
    inputs=["image", "text"],
    outputs=["text", "text"],
    title="OCR with Keyword Search"
)

# Launch the app
if __name__ == "__main__":
    gr_interface.launch(share=True)
