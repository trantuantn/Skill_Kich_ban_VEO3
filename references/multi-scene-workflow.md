# Storyboard và Continuity Validator

1. Chốt thông điệp, nhân vật và kết thúc.
2. Lập Character/Style/Scene Lock có ID.
3. Chia theo nhịp hành động; ghi thời lượng mục tiêu từng cảnh và tổng.
4. Mỗi hàng: thời gian, prompt độc lập, camera, âm thanh, trạng thái đầu/cuối, khóa dùng lại.
5. So sánh từng cặp cảnh: vật đang cầm, tay cầm, hướng đi, trang phục, ánh sáng, vị trí. Cảnh nối tiếp không tự đặt lại đạo cụ.
6. Khi có bước nhảy thời gian/không gian, ghi chuyển cảnh rõ. Không giả nối liên tục.
7. Viết đầy đủ khóa trong từng khối prompt để có thể sao chép riêng. Mã ID chỉ giúp quản lý, không thay mô tả.

Ví dụ lỗi: C1 An cầm bình bằng tay phải; C2 tự nhiên bình biến mất. Sửa: giữ bình tay phải hoặc bổ sung động tác đặt bình xuống trước khi cắt.
Dùng tổng thời lượng để lập kế hoạch ghép, không cam kết Veo tạo toàn bộ chuỗi bằng một lần chạy.
