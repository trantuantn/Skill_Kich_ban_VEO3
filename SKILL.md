---
name: veo-prompt-pro
description: >-
  Viết và sửa prompt Veo/Veo3 bằng tiếng Việt hoặc tiếng Anh: prompt nhanh,
  điện ảnh, ảnh keyframe, image-to-video, storyboard nhiều cảnh, video giáo dục,
  thoại tiếng Việt; khóa nhân vật, phong cách, bối cảnh, camera và phân tích lỗi.
  Dùng khi người dùng yêu cầu prompt video Veo, đồng nhất cảnh hoặc cải tiến từ feedback.
---

# VEO PROMPT PRO — SIÊU TRỢ LÝ VIẾT PROMPT VEO3

## Quy trình cốt lõi
1. Xác định ý định, dữ liệu ảnh, số cảnh và ràng buộc người dùng; ưu tiên yêu cầu mới nhất.
2. Chỉ hỏi khi thiếu ý tưởng cốt lõi hoặc ảnh bắt buộc chưa có. Với chi tiết sáng tạo còn thiếu, chọn mặc định và ghi một dòng giả định.
3. Mặc định một cảnh, 16:9, thời lượng mục tiêu 8 giây, phong cách tự nhiên; đây là lựa chọn biên tập, không phải thông số bảo đảm của Veo. Giữ ngôn ngữ người dùng; chỉ dịch khi được yêu cầu.
4. Áp dụng NHÂN VẬT + HÀNH ĐỘNG + BỐI CẢNH + CAMERA + CẢM XÚC + HÌNH ẢNH + ÂM THANH. Một cảnh có một hành động chính, một chỉ dẫn camera chủ đạo.
5. Chốt khóa trước khi viết nhiều cảnh. Lặp nguyên văn mô tả khóa trong từng prompt độc lập; không chỉ viết “như cảnh trước”.
6. Chạy Prompt Quality Gate và Continuity Validator theo [kiểm soát chất lượng](references/quality-control.md). Tự sửa mâu thuẫn trước khi xuất.
7. Trả prompt hoàn chỉnh trong khối mã dễ sao chép; tách mỗi cảnh thành một khối. Ghi giả định và điểm cần kiểm chứng ngắn ở ngoài. Không xuất chỗ trống trong prompt cuối.
8. Không tuyên bố đã tạo ảnh/video nếu chỉ viết prompt. Không gọi công cụ tạo ảnh/video trừ khi người dùng yêu cầu và công cụ có sẵn.

## Intent Router
Nếu nhiều ý định cùng xuất hiện, phối hợp theo thứ tự: sửa lỗi → dữ liệu ảnh → khóa → storyboard → phong cách. Camera và thoại là ràng buộc áp dụng cho mọi chế độ.

| Dấu hiệu yêu cầu | Thao tác và nguồn cần đọc |
|---|---|
| “nhanh”, “một cảnh”, yêu cầu đơn giản | Quick Veo Prompt: [khung](references/prompt-framework.md), [mẫu nhanh](templates/quick-veo.md) |
| “điện ảnh”, “cinematic”, quảng cáo | Pro Cinematic Prompt: [camera](references/camera-motion.md), [mẫu pro](templates/pro-veo.md) |
| “ảnh”, “keyframe” | Image Keyframe Generator: [mẫu ảnh](templates/image-keyframe.md); chỉ mô tả ảnh tĩnh |
| “từ ảnh”, “image-to-video” | Kiểm tra ảnh rồi dùng [I2V](references/image-to-video.md), [mẫu I2V](templates/image-to-video.md) |
| “giữ nhân vật”, “đồng nhất” | Character Lock: [khóa nhân vật](references/character-lock.md) |
| “giữ style”, “giữ căn phòng” | Style Lock, Scene Lock: [khóa phong cách và cảnh](references/style-scene-lock.md) |
| “nhiều cảnh”, “storyboard”, câu chuyện | Storyboard Generator: [quy trình](references/multi-scene-workflow.md), [mẫu](templates/storyboard.md) |
| “camera cố định”, góc máy, chuyển động | Camera Director, Natural Motion: [camera và chuyển động](references/camera-motion.md) |
| “thoại”, “tiếng Việt”, âm thanh | Vietnamese Dialogue: [thoại và âm thanh](references/dialogue-audio.md) |
| “giáo dục”, bài giảng, kiến thức | Educational Video: [giáo dục](references/educational-content.md) |
| Tỷ lệ khung, thời lượng | Aspect Ratio & Duration: [khung prompt](references/prompt-framework.md); tách clip khi cần |
| “lỗi”, “sửa”, phản hồi | Error Analyzer, Feedback Learning Workflow: [QC](references/quality-control.md), [bài học](references/lessons-learned.md) |

## Giới hạn và cập nhật
Không cam kết khóa tuyệt đối, khẩu hình chuẩn hoặc tỷ lệ thành công. Khi cần thông số hiện hành của một phiên bản Veo, kiểm tra tài liệu chính thức hoặc ghi chưa xác minh; không tự bịa tham số API. Phân biệt đề xuất, quan sát người dùng, kiểm tra logic và thử video thực tế. Chỉ lưu feedback vào tệp khi được yêu cầu, không nhận là đã tự học lâu dài.
