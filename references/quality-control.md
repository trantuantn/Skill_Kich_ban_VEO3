# Prompt Quality Gate, Error Analyzer và Feedback Learning

## Gate trước khi xuất
- Đủ bảy thành phần hoặc ghi rõ thành phần không cần, ví dụ không thoại.
- Một hành động chính; thời gian khả thi; tỷ lệ khung và thời lượng là mục tiêu rõ.
- Camera không mâu thuẫn; camera cố định không chứa lệnh chuyển máy.
- Khóa nhân vật/phong cách/cảnh được lặp đầy đủ ở prompt độc lập.
- Trạng thái đầu/cuối, tay cầm vật, ánh sáng và hướng đi nối được; khóa bối cảnh không chứa vị trí đạo cụ trái với hành động.
- Thoại đúng nguyên văn, đúng người, có khoảng thở; âm nền không lấn.
- Nội dung giáo dục đúng; mô phỏng được ghi nhãn; không bịa nguồn.
- Không còn biến mẫu chưa điền; không hứa kết quả video chưa thử.

Đánh dấu PASS logic, NEEDS FIX hoặc NOT RUN, không dùng phần trăm giả. NEEDS FIX phải sửa trước bàn giao. PASS logic không phải PASS video.

## Phân tích lỗi
Thu tối thiểu prompt cũ và mô tả lỗi; nếu có clip thì ghi mốc giây. Phân loại: drift nhân vật, bối cảnh, vật lý, camera, thoại, thời lượng hoặc kiến thức. Tách quan sát từ video/người dùng khỏi giả thuyết nguyên nhân. Không chẩn đoán chắc chắn khi chỉ có mô tả.

Ví dụ giả định: người dùng nói “máy tự zoom dù muốn cố định”. Giả thuyết: prompt còn “push-in”. Sửa bỏ push-in và thêm tripod fixed frame. Trả prompt đã sửa, thay đổi chính, điều cần xem ở lần thử sau; không nói đã hết lỗi.

## Vòng phản hồi
Ghi bản ghi khi được yêu cầu: ngày, phiên bản prompt, cấu hình nếu biết, nguồn phản hồi, lỗi quan sát, giả thuyết, thay đổi duy nhất, tiêu chí chấp nhận, kết quả thử lại. Dùng nhãn proposed / user-reported / observed / verified theo bằng chứng. Chỉ nâng thành bài học đã thử sau khi có đầu ra tương ứng; không suy rộng từ một clip sang mọi model.
Lưu riêng prompt trước/sau; thay một biến mỗi lượt khi khả thi. Cập nhật patch cho sửa câu, minor cho tính năng, major cho thay quy trình gây không tương thích. Không tự nhận nhớ lâu dài hoặc sửa Skill vĩnh viễn nếu chưa ghi và lưu thành công.
