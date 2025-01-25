import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import os
import json
from promptTemplate import prompt_format
from jsonFormat import json_format
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        with open(file_path,'rb') as f:
            reader=PdfReader(f)
            return " ".join([page.extract_text() for page in reader.pages])

    elif file_path.endswith('.docx'):
        doc=Document(file_path)
        return " ".join([para.text for para in doc.paragraphs])

def analyze_resume(file_path):
    
  genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Set your API key
  model = genai.GenerativeModel('gemini-2.0-flash-exp')
  resume_text=extract_text(file_path)
  json_file=json_format()
  prompt=prompt_format(resume_text,json_file)
  response = model.generate_content(prompt)
  return parse_response(response.text)


def parse_response(text):
  try:
     json_start=text.find('{')
     json_end=text.rfind('}')+1
     return json.loads(text[json_start:json_end])
  except:
     return {"Error":"Failed to parse response"}