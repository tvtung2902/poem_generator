import textwrap

def generate_poem(prompt, tokenizer, model, max_seq_length = 2048, device = 'cpu', max_new_tokens=200):
    text = f"""<|im_start|>system
Bạn là một AI thi sĩ chuyên sáng tác thơ lục bát bằng tiếng Việt.
Hãy thể hiện cảm xúc tinh tế, sử dụng ngôn từ đẹp, và tuân thủ nghiêm ngặt các quy tắc sau:
- Bài thơ có nhiều cặp dòng: một dòng 6 chữ, sau đó là một dòng 8 chữ.
- Mỗi dòng phải xuống dòng rõ ràng.
- Dòng 6 chữ có đúng 6 từ, dòng 8 chữ có đúng 8 từ.
- Không được viết sai nhịp, không viết quá, viết thiếu số chữ.
- Vần luật phải tự nhiên, đúng phong cách thơ ca truyền thống Việt Nam.
<|im_end|>
<|im_start|>user
Hãy sáng tác một bài thơ lục bát về chủ đề '{prompt}'<|im_end|>

<|im_start|>assistant
"""

    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=max_seq_length
    )

    inputs = {key: value.to(device) for key, value in inputs.items()}

    output = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=0.8,
        top_k=50,
        top_p=0.9,
        repetition_penalty=1.1
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    generated_poem = generated_text.replace(text, "").strip()
    return generated_poem
