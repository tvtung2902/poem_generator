# Poem Generator — Sinh Thơ Lục Bát với VinaLLaMA

Đây là một dự án sử dụng AI để tạo ra các bài thơ lục bát tiếng Việt.  
Project sử dụng mô hình ngôn ngữ lớn VinaLLaMA và fine-tuned trên tập dữ liệu thơ lục bát.

Toàn bộ dữ liệu được thu thập bằng **Selenium** từ các trang web như **thivien.net**, **lucbat.com**..., cũng như một số bộ **public dataset** có sẵn. 

Dữ liệu sau khi thu thập sẽ được **tiền xử lý**, lọc nhiễu và chuẩn hóa theo cấu trúc thơ lục bát. Sau đó, mô hình **VinaLLaMA** được fine-tune để học cách tiếp nối thơ một cách tự nhiên, đúng nhịp và giữ được chất thơ truyền thống.

Mô hình sau huấn luyện có khả năng tiếp tục viết các đoạn thơ lục bát dựa trên một dòng đề bài đầu vào, duy trì vần điệu và ngữ nghĩa phù hợp.

---

## Demo

<img src="demo/img.gif" alt="demo poem generation" width="600"/>

---

