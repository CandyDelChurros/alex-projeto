import os
from flask import Flask, request, render_template, redirect, url_for
import cv2
import PIL.Image
import google.generativeai as genai
from docx import Document

app = Flask(__name__)

genai.configure(api_key="AIzaSyAEYr9MEJ4aCLw6z_s9XHEUvtTmLnzLx3M")
model = genai.GenerativeModel("gemini-1.5-flash")

def process_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 102, 255, cv2.THRESH_BINARY_INV)
    processed_image_path = "static/img/imagem_processada.png"
    cv2.imwrite(processed_image_path, thresh)
    return processed_image_path

def generate_docx(text):
    doc = Document()
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    doc.add_paragraph(text)
    doc.save("static/img/document.docx")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return redirect(request.url)
        image_file = request.files["image"]
        if image_file.filename == "":
            return redirect(request.url)
        
        image_path = os.path.join("static/img", image_file.filename)
        image_file.save(image_path)
        
        processed_image_path = process_image(image_path)

        text_image = PIL.Image.open(processed_image_path)
        response = model.generate_content(["O que está escrito? apenas transcreva o texto sem comentar nada", text_image])

        generate_docx(response.text)

        return render_template("img_to_doc.html", document_url=url_for("static", filename="img/document.docx"))

    return render_template("img_to_doc.html")

if __name__ == "__main__":
    app.run(debug=True)


