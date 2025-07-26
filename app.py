from unsloth import FastLanguageModel
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer
import torch
import uvicorn


# Cấu hình
MODEL_PATH = "vinallama_poem_model"
MAX_SEQ_LENGTH = 512

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

print ("ok")
# API setup
app = FastAPI()

# Định nghĩa request
class Prompt(BaseModel):
    title: str

@app.post("/generate")
def generate_poem(prompt: Prompt):
    system_prompt = """Bạn là một AI thi sĩ chuyên sáng tác thơ lục bát bằng tiếng Việt.
Hãy thể hiện cảm xúc tinh tế, sử dụng ngôn từ đẹp, và tuân thủ nghiêm ngặt các quy tắc sau:
- Bài thơ có nhiều cặp dòng: một dòng 6 chữ, sau đó là một dòng 8 chữ.
- Mỗi dòng phải xuống dòng rõ ràng.
- Dòng 6 chữ có đúng 6 từ, dòng 8 chữ có đúng 8 từ.
- Không được viết sai nhịp, không viết quá, viết thiếu số chữ.
- Vần luật phải tự nhiên, đúng phong cách thơ ca truyền thống Việt Nam.
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Hãy sáng tác một bài thơ lục bát về chủ đề '{prompt.title}'"}
    ]

    prompt_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    inputs = tokenizer(prompt_text, return_tensors="pt").to(model.device)


    outputs = model.generate(**inputs, max_new_tokens=256, do_sample=True, temperature=0.8)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Tách phần thơ
    generated_poem = result.split("assistant")[-1].strip()

    return {"poem": generated_poem}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
