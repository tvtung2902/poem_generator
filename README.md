# Poem Generator — Sinh Thơ Lục Bát với VinaLLaMA

Đây là dự án sử dụng AI để tạo ra các bài thơ lục bát tiếng Việt.  
Project sử dụng mô hình ngôn ngữ lớn **VinaLLaMA** và được **fine-tune** trên tập dữ liệu thơ lục bát.

---

## Demo

**Xem thêm demo [tại đây](https://www.youtube.com/watch?v=x4v4GgdI9Fs)**

<p align="center">
  <img src="demo/img.png" alt="Poem Generation Screenshot" width="95%">
</p>
<p align="center"><em>Demo poem generation 1</em></p>

<p align="center">
  <img src="demo/img.gif" alt="Poem Generation Animated" width="95%">
</p>
<p align="center"><em>Demo poem generation 2</em></p>

---

## Dataset & Training

Toàn bộ dữ liệu được thu thập bằng **Selenium** từ các trang web như **thivien.net**, **lucbat.com**, cũng như một số bộ **public dataset** sẵn có.

Dữ liệu sau khi thu thập sẽ được **tiền xử lý**, lọc nhiễu và chuẩn hóa theo cấu trúc thơ lục bát. Sau đó, mô hình **VinaLLaMA** được fine-tune để học cách tiếp nối thơ một cách tự nhiên, đúng nhịp và giữ được chất thơ truyền thống.

Mô hình sau huấn luyện có khả năng tiếp tục viết các đoạn thơ lục bát dựa trên một dòng đề bài đầu vào, duy trì vần điệu và ngữ nghĩa phù hợp.

---

### Dataset

Bạn có thể truy cập dataset [tại đây](https://drive.google.com/file/d/1w5XEUwTi8lCB9eFM_DnSIJ8VaMMrsfi3/view)

---

## License

Dự án này là mã nguồn mở và được phát hành theo giấy phép MIT.

---

Thanks for visiting!
