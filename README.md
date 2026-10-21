# VEO PROMPT PRO — SIÊU TRỢ LÝ VIẾT PROMPT VEO3

Phiên bản 2.0.0. Bộ Agent Skill viết prompt; không phải ứng dụng gọi Veo và không kèm khóa API. Hỗ trợ 18 năng lực được định tuyến trong SKILL.md, từ prompt nhanh đến storyboard, khóa nhân vật và sửa lỗi.

## Cài đặt
Giải nén veo-prompt-pro-skill-v2.0.zip. Sao chép thư mục `veo-prompt-pro` vào thư mục skills của môi trường Agent Skills đang dùng (ví dụ `~/.codex/skills/veo-prompt-pro` nếu môi trường đó hỗ trợ). Không đặt thêm một tầng thư mục giữa tên skill và SKILL.md. Tải lại danh sách skill theo môi trường.
Trong ChatGPT Work, nếu Skill đã xuất hiện ở trang Skills thì chọn trực tiếp. Việc cài bằng ZIP phụ thuộc giao diện hỗ trợ; không phải mọi phiên bản ChatGPT đều nhập được ZIP Skill.

## Sử dụng
Gọi `$veo-prompt-pro` kèm ý tưởng, hoặc chọn Skill trong giao diện.
- “Viết prompt Veo nhanh: bướm mở cánh trên lá, camera cố định.”
- “Tạo 2 cảnh An tưới cây, đồng nhất nhân vật, mỗi cảnh mục tiêu 8 giây.”
- “Từ ảnh này, tạo chuyển động nhẹ, giữ nguyên bố cục.” (cần đính kèm ảnh)
- “Sửa prompt này: camera đang zoom dù tôi muốn cố định.”

Đầu ra là prompt dễ sao chép, giả định ngắn và kiểm tra logic. Tỷ lệ/thời lượng là mục tiêu biên tập cần đối chiếu khả năng giao diện Veo. Xem ví dụ đầy đủ tại examples/butterfly.md và examples/multi-scene-story.md.

## Cấu trúc và danh sách tệp
- SKILL.md: entrypoint, router, quy trình và 18 năng lực.
- README.md, CHANGELOG.md: cài, dùng và phiên bản.
- agents/openai.yaml: tên hiển thị và câu gọi mẫu.
- references/: prompt-framework.md, character-lock.md, style-scene-lock.md, camera-motion.md, image-to-video.md, multi-scene-workflow.md, educational-content.md, dialogue-audio.md, quality-control.md, lessons-learned.md.
- templates/: quick-veo.md, pro-veo.md, image-keyframe.md, image-to-video.md, storyboard.md.
- examples/: classroom.md, butterfly.md, cinematic-scene.md, multi-scene-story.md.
- tests/: test-cases.md, validation-report.md, validate.py, forward-test.md.

## Kiểm tra và cập nhật
Chạy `python tests/validate.py` (cần Python 3 và PyYAML). Báo cáo kiểm thử ghi rõ kiểm tra tĩnh, đánh giá logic và phần chưa chạy Veo. Khi sửa, giữ prompt cũ và kết quả phản hồi; chạy lại kiểm tra, cập nhật CHANGELOG, đóng ZIP mới. Dùng patch cho sửa lỗi, minor cho thêm chức năng, major khi đổi quy trình không tương thích.

## Nguồn và giới hạn
Nguồn là Master Prompt và phần ngữ cảnh trước truy xuất được; không có toàn văn lịch sử hoặc thử nghiệm video. Ví dụ là nội dung mới. Khóa nhân vật, thoại, camera và thời lượng không được bảo đảm chỉ bằng prompt. Không có số liệu tỷ lệ thành công.

## Giấy phép
Chưa thêm LICENSE vì chủ sở hữu chưa phê duyệt loại giấy phép. Đề xuất cân nhắc MIT nếu muốn cho phép tái sử dụng rộng rãi; đây chỉ là đề xuất, chưa cấp quyền bằng giấy phép đó. Việc công khai repository không tự thay thế giấy phép.
