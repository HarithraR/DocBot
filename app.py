from flask import Flask, request, render_template, jsonify
from utils.pdf_processing import extract_text_from_pdf
from utils.vector_store import add_to_vector_store, retrieve_relevant_content
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        # Check if file exists in the request
        if "file" not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # Save the file to the uploads folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Extract text from the uploaded PDF
        text = extract_text_from_pdf(file_path)

        # Add the extracted text to the vector store
        add_to_vector_store(file.filename, text)

        return jsonify({"message": "File uploaded and processed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/query", methods=["POST"])
def query():
    try:
        # Get the user's query from the request
        data = request.json
        query_text = data.get("query", "")
        if not query_text:
            return jsonify({"error": "Query is required"}), 400

        # Retrieve relevant content from the vector store
        response = retrieve_relevant_content(query_text)

        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
