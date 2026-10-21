# Validation report — 2.0.0

Ngày: 21/10/2026. Phạm vi: tệp, YAML, đường dẫn, định tuyến theo tài liệu và logic prompt. Không có quyền/công cụ Veo; toàn bộ sinh video, âm thanh, khẩu hình, độ đồng nhất và độ chính xác thời lượng thực tế: NOT RUN.

## Phân loại bằng chứng
- Script validate.py: kiểm tra tự động cấu trúc, không gọi mô hình Veo.
- quick_validate.py của skill-creator: kiểm tra frontmatter và tên.
- Review thủ công: ví dụ bướm, lớp học, gốm, An tưới cây và các quy tắc QC; không có video.
- Forward test: agent độc lập đọc Skill và trả lời yêu cầu văn bản, ghi trong forward-test.md. Đây là kiểm tra thực thi hướng dẫn trong môi trường agent, không chứng minh auto-trigger trong mọi sản phẩm.

## Kết quả logic được rà soát
| Nhóm | Kết luận | Giới hạn |
|---|---|---|
| Router, 18 năng lực | Đã ánh xạ trong SKILL.md | Tự kích hoạt bằng UI chưa kiểm chứng |
| Prompt nhanh | Đủ khung 7 thành phần | Chưa sinh video |
| Điện ảnh | Một dolly-in, thao tác có điểm tựa | Chưa xác minh vật lý |
| I2V | Có gate thiếu ảnh và mẫu có điều kiện | Chưa có ảnh/video thật |
| Nhiều cảnh | Khóa đầy đủ, đạo cụ nối hợp lý | Khóa không bảo đảm model tuân thủ |
| Giáo dục | Ví dụ bay hơi không cần sôi | Chưa đối chiếu chương trình riêng |
| Thoại Việt | Câu có dấu, một người nói | Chưa thử phát âm/khẩu hình |
| Máy cố định | Loại bỏ chỉ dẫn máy mâu thuẫn | Chưa quan sát camera thật |
| Feedback | Tách bằng chứng, giả thuyết, sửa, thử lại | Chưa có feedback thử video thật |

Không có tỷ lệ thành công. LICENSE cố ý chưa tạo theo yêu cầu chủ sở hữu. ZIP và log kết quả tự động được xác nhận sau khi đóng gói; trạng thái GitHub được báo riêng bằng commit đã đọc lại.

## Kết quả chạy thực tế
- quick_validate.py: `Skill is valid!`.
- tests/validate.py: 79/79 assertions PASS (tệp không rỗng, frontmatter, tên, liên kết, metadata UI, khóa lặp, tay cầm đạo cụ).
- Forward test: 5 yêu cầu ban đầu; ca nhiều cảnh phát hiện mâu thuẫn khóa đạo cụ, đã sửa tài liệu và chạy lại ca đó, reviewer PASS logic. Thêm một ca feedback giả lập: PASS về nhãn bằng chứng; chưa thử ghi feedback vào tệp.
- Không coi I2V thiếu ảnh là đã chạy I2V thực tế; chỉ gate thiếu ảnh đạt.
- ZIP: 27 tệp, CRC đạt; giải nén thành công và đối chiếu từng byte với nguồn.
- Git diff: chỉ thêm bộ Skill, không xóa tệp; đã kiểm tra khoảng trắng.
