# Character Lock

Lập hồ sơ ID riêng cho từng nhân vật: độ tuổi thể hiện, vóc dáng, khuôn mặt, tóc, trang phục, phụ kiện và giọng. Không tự suy danh tính thật từ ảnh. Giữ đặc điểm ảnh nhìn thấy; đánh dấu chi tiết khuất là chưa rõ.

Ví dụ khóa C01: “An, cô gái Việt Nam trưởng thành, khuôn mặt trái xoan, tóc đen ngang vai, áo khoác vàng trơn, quần xanh đậm, ba lô nâu.”
Lặp nguyên văn chuỗi này ở từng cảnh xuất riêng. Chỉ đổi áo khi kịch bản có thay đồ và ghi thời điểm đổi. Gán tên người nói để tránh tráo giọng.

Tạo bảng theo dõi cảnh: ID, áo, phụ kiện, tay cầm vật gì, vị trí, hướng nhìn, trạng thái cuối. Chuyển trạng thái cuối thành đầu cảnh kế. Ảnh tham chiếu có thể hỗ trợ nếu công cụ cho phép; không bảo đảm đồng nhất tuyệt đối. Khi drift, kiểm tra ảnh nguồn, rút gọn hành động, giữ khóa và thử lại một thay đổi mỗi lần.
