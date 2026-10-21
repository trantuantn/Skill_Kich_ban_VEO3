# Nguồn, bài học và mức bằng chứng

Ngày tổng hợp: 21/10/2026. Không có quyền truy cập Veo trong lần xây dựng này.

## Phạm vi nguồn
- Master Prompt hiện tại: nguồn trực tiếp cho 18 năng lực, bảy thành phần, cấu trúc tệp, yêu cầu kiểm thử và GitHub.
- Kết quả truy xuất ngữ cảnh trước: có bản tóm tắt thiết kế VEO v2.0 gồm router, continuity, quality gate, feedback loop; tóm tắt cũng ghi chưa tạo đủ tệp, chưa xác minh cài, chưa chạy Veo, chưa đẩy GitHub. Đây là lời ghi nhận trước đây, không phải log thử nghiệm.
- Không truy cập được toàn văn mọi cuộc trò chuyện, prompt gốc hoặc clip Veo. Không có feedback video cụ thể hay tỷ lệ thành công có thể xác minh.
- Đã đọc build_skill.py: thuộc PRO 5.0 soạn giáo án, loại khỏi nguồn VEO; không thực thi mã đó.

## Bài học có căn cứ từ quá trình làm việc
| Bài học | Bằng chứng | Phạm vi |
|---|---|---|
| Bản thiết kế không đồng nghĩa bộ Skill đã triển khai | Tóm tắt trước nói chỉ có bản thảo | Phải tạo tệp, kiểm tra ZIP và xác minh commit |
| Không trộn dự án giáo án với VEO | Nội dung build_skill.py đã đọc | Kiểm tra nguồn trước tái sử dụng |
| Không tuyên bố chất lượng video đã thử | Không có clip hoặc quyền Veo | Chỉ báo kiểm tra cấu trúc/logic |

## Đề xuất kỹ thuật, chưa chứng minh bằng video
Lặp khóa nguyên văn; mỗi cảnh một hành động; một chỉ dẫn camera; rút ngắn thoại; thay một biến khi sửa lỗi; theo dõi trạng thái đạo cụ. Đây là quy tắc thiết kế để thử, không phải kết luận thực nghiệm Veo.

Các ví dụ classroom, butterfly, cinematic-scene và multi-scene-story là ví dụ mới được biên soạn, không phải thành công được người dùng xác nhận. Kết quả kiểm tra bản phát hành nằm trong tests/validation-report.md. Khi có feedback thật, ghi nguồn, ngày, prompt/cấu hình và đầu ra trước khi cập nhật bảng bài học.

## Bài học mới từ kiểm tra agent của bản 2.0
Quan sát thật trong kiểm thử văn bản: khóa cảnh ghi “cốc trên bàn” xung đột với hành động cầm cốc. Đã sửa quy tắc để vị trí đạo cụ thuộc trạng thái đầu/cuối từng cảnh, rồi chạy lại: hai prompt mới không còn mâu thuẫn đó. Bằng chứng: tests/forward-test.md. Kết luận chỉ áp dụng cho logic văn bản; chưa chứng minh bằng video. Lượt đầu agent tự đánh giá PASS nhưng reviewer tìm thấy lỗi, vì vậy không dùng tự đánh giá làm bằng chứng duy nhất.
