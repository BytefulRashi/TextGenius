from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline

# Create a new FastAPI app instance
app = FastAPI()

# Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define a function to handle the GET request at '/generate'
@app.get("/generate", response_class=HTMLResponse)
async def generate_text(request: Request, prompt: str):
    # Use the pipeline to generate text from the given input text
    output = pipe(prompt)
    generated_text = output[0]['generated_text']
    return templates.TemplateResponse("index.html", {"request": request, "prompt": prompt, "output": generated_text})
