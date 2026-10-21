# Image-to-Video

1. Kiểm tra ảnh có trong ngữ cảnh và có xem được không. Nếu chưa có, yêu cầu ảnh; có thể soạn bản text-to-video tạm nhưng không gọi đó là prompt bám ảnh đã phân tích.
2. Ghi các yếu tố nhìn thấy: chủ thể, trang phục, khung hình, ánh sáng, vật thể, phong cách. Không đoán vùng ngoài khung hay danh tính.
3. Chọn chuyển động nhỏ phù hợp ảnh: chớp mắt, thở nhẹ, tóc lay, nước gợn. Đặt trạng thái đầu bám ảnh, trạng thái cuối khả thi.
4. Giữ đặc điểm nhận dạng, bố cục và ánh sáng; chỉ thay điều người dùng yêu cầu. Nếu muốn xoay máy lớn, nêu vùng chưa thấy phải được mô hình suy dựng.
5. Tách nội dung ảnh và lệnh chuyển động; dùng mẫu I2V. Nếu công cụ chỉ hỗ trợ một ảnh đầu, không tự bịa chức năng ảnh cuối.

Không nhắc “ảnh đính kèm” trong bản độc lập khi chưa có ảnh. Không coi prompt ảnh keyframe là lệnh tạo video. Âm thanh vẫn cần chỉ định riêng; ảnh không chứng minh giọng hay tiếng môi trường.
