from bs4 import BeautifulSoup
import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import Response
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file

app = FastAPI()
load_dotenv()

# Get the API key
api_key = os.getenv("API_KEY")
# Initialize the generative model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')




@app.post("/translate")
async def translate(file: UploadFile = File(...),target_language: str = Form("en")):
    # Read the HTML file content
    html = await file.read()
    print(html)
    # Translate the HTML
    response = model.generate_content(f"Translate the HTML content to {target_language} : {html}")
    translated_html = response.text
    return Response(content=translated_html, media_type="text/html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
