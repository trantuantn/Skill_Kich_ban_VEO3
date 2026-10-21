# Khung prompt và cấu hình

Bảy thành phần có chức năng cụ thể:

| Thành phần | Viết gì |
|---|---|
| Nhân vật | Danh tính, đặc điểm nhìn thấy, trang phục, số lượng |
| Hành động | Một động tác chính; bắt đầu, diễn tiến, kết thúc |
| Bối cảnh | Vị trí, thời điểm, bố trí vật thể |
| Camera | Cỡ cảnh, góc nhìn, cố định hoặc một chuyển động |
| Cảm xúc | Biểu hiện mắt, mặt, tư thế có thể quan sát |
| Hình ảnh | Ánh sáng, chất liệu, bảng màu, phong cách |
| Âm thanh | Tiếng môi trường, lời thoại, nhạc hoặc chỉ định im lặng |

Gộp thành đoạn có quan hệ nhân quả, không nhồi danh sách tính từ. Thiếu nhân vật người thì dùng chủ thể như bướm, vật thể hoặc cảnh quan.

## Tỷ lệ và thời lượng
Dùng 16:9 cho màn hình ngang, 9:16 cho khung dọc, tỷ lệ khác theo yêu cầu và khả năng công cụ. Giữ chủ thể trong vùng an toàn để tránh cắt mặt/tay. Thời lượng ghi là mục tiêu, phải chọn lại trong giao diện nếu giao diện hỗ trợ. Không coi một dòng prompt là thiết lập API.
Mặc định biên tập 8 giây cho một hành động nhỏ. Yêu cầu dài thì chia clip và nêu tổng thời lượng; không ép nhiều sự kiện vào một clip. Nếu thời lượng người dùng yêu cầu chưa được xác minh hỗ trợ, giữ mục tiêu trong storyboard và ghi cần ghép clip.

## Đầu ra
Một dòng giả định nếu có; prompt hoàn chỉnh; một dòng giới hạn nếu ảnh/thông số chưa xác minh. Không thêm thang điểm chất lượng giả. Không gắn nhãn “đã kiểm chứng Veo” cho prompt mới viết.
