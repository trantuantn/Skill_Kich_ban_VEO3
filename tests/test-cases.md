# Test cases v2.0.0

Các ca dưới đây kiểm tra định tuyến và logic đầu ra, không đo chất lượng video. Dùng validate.py cho kiểm tra tĩnh; forward-test.md lưu đầu ra của lượt chạy độc lập.

| ID | Đầu vào | Tiêu chí chấp nhận | Bằng chứng |
|---|---|---|---|
| T01 | Viết prompt nhanh mèo bên cửa sổ | Một prompt đủ 7 phần, không hỏi chi tiết nhỏ | Forward test |
| T02 | Điện ảnh người thợ gốm | Một chuyển động máy, tiếp xúc tay/đất hợp lý | examples/cinematic-scene.md và forward test |
| T03 | Từ ảnh này tạo chớp mắt; chưa có ảnh | Yêu cầu ảnh, không bịa đặc điểm | Forward test; ảnh thật NOT RUN |
| T04 | Hai cảnh cầm cốc rồi đặt xuống | Lặp khóa, cùng tay, cốc có trạng thái đầu/cuối | Forward test |
| T05 | Giáo dục bay hơi | Không nói cần sôi; không giả nước biến mất ngay | examples/classroom.md và forward test |
| T06 | Cô giáo nói câu tiếng Việt | Đúng dấu, một người nói, không tự dịch | Forward test |
| T07 | Camera cố định và dolly-in cùng lúc | Bỏ chuyển động máy, ưu tiên cố định | Forward test |
| T08 | Máy tự zoom dù yêu cầu đứng yên | Quan sát/giả thuyết/sửa/tiêu chí thử lại tách biệt | QC review và bài sửa forward test |
| T09 | Muốn lưu feedback thành bài học | Chỉ ghi khi được yêu cầu; không khẳng định sửa đã thành công | references/quality-control.md, đánh giá tĩnh |
| T10 | Storyboard An tưới cây | Tay phải, áo và ánh sáng giữ; tổng 16 giây | examples/multi-scene-story.md, script và review |
| T11 | Prompt ảnh keyframe bướm | Ảnh tĩnh không nhạc/thoại hoặc diễn tiến thời gian | examples/butterfly.md, review |
| T12 | Thời lượng clip dài hoặc tỷ lệ khác | Ghi mục tiêu, đối chiếu giao diện, chia clip | prompt-framework.md, đánh giá tĩnh |
| T13 | Yêu cầu không liên quan video như tính 2+2 | Không nên tự dùng skill chỉ vì đã cài | Metadata review; auto-trigger runtime NOT RUN |

## Cách đánh giá lại
Chạy script, đọc từng prompt so với tiêu chí, sau đó thử trên Veo khi có quyền. Lưu phiên bản model, cấu hình, ảnh đầu nếu có, prompt, clip và kết quả quan sát. Một PASS logic không nâng thành PASS video. Các ca dựa trên tài liệu chỉ là kiểm tra tĩnh, không phải thực thi agent.
