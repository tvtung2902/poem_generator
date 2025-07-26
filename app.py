from unsloth import FastLanguageModel
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer
import torch
import uvicorn
from generation import *

# Cấu hình
MODEL_PATH = "vinallama_poem_model"
MAX_SEQ_LENGTH = 512
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

# Load model
model, _ = FastLanguageModel.from_pretrained(
    model_name=MODEL_PATH,
    max_seq_length=MAX_SEQ_LENGTH,
    dtype=torch.float16,
    load_in_4bit=True,
    device_map="auto",
)

FastLanguageModel.for_inference(model)

# API setup
app = FastAPI()

# Định nghĩa request
class Prompt(BaseModel):
    title: str

@app.post("/generate")
def gen_poem(prompt: Prompt):
    generated_poem = generate_poem(prompt, tokenizer, model, MAX_SEQ_LENGTH, device)
    generated_poem = generated_poem.split("assistant")[-1].strip()
    return {"poem": generated_poem}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
