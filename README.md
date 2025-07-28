# Poem Generator — Sinh Thơ Lục Bát với VinaLLaMA

Đây là dự án sử dụng AI tạo ra các bài thơ lục bát tiếng Việt.  
Project sử dụng mô hình ngôn ngữ lớn VinaLLaMA và fine-tuned trên tập dữ liệu thơ lục bát.

---

## Demo

**Xem thêm demo [tại đây](https://www.youtube.com/watch?v=x4v4GgdI9Fs)**

<div style="text-align:center;">
  <img src="demo/img.png" alt="demo poem generation" width="95%">
</div>

<div style="text-align:center;">
  <img src="demo/img.gif" alt="demo poem generation" width="95%">
</div>

---

Toàn bộ dữ liệu được thu thập bằng **Selenium** từ các trang web như **thivien.net**, **lucbat.com**..., cũng như một số bộ **public dataset** có sẵn. 

Dữ liệu sau khi thu thập sẽ được **tiền xử lý**, lọc nhiễu và chuẩn hóa theo cấu trúc thơ lục bát. Sau đó, mô hình **VinaLLaMA** được fine-tune để học cách tiếp nối thơ một cách tự nhiên, đúng nhịp và giữ được chất thơ truyền thống.

Mô hình sau huấn luyện có khả năng tiếp tục viết các đoạn thơ lục bát dựa trên một dòng đề bài đầu vào, duy trì vần điệu và ngữ nghĩa phù hợp.

---

## Dataset

Các bạn có thể xem [tại đây](https://drive.google.com/file/d/1w5XEUwTi8lCB9eFM_DnSIJ8VaMMrsfi3/view)

---

## License

Dự án này là mã nguồn mở và được phát hành theo giấy phép MIT.

---

Thanks for visiting!
