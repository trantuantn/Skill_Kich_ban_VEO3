# Forward test văn bản — 21/10/2026

Agent độc lập nhận đường dẫn Skill và 5 yêu cầu thực tế, không nhận tiêu chí hay đáp án mẫu. Agent đã đọc Skill; không sửa tệp, không gọi Veo.

## Yêu cầu và đầu ra được ghi nhận
1. Mèo ngồi bên cửa sổ, camera cố định → một prompt 16:9 mục tiêu 8 giây; mèo mướp thở nhẹ, máy tripod, tiếng chim, không thoại. Đủ bảy thành phần; PASS logic.
2. Hai cảnh cô gái cầm cốc rồi đặt xuống → lặp khóa Mai, áo kem, tóc đen; tay phải giữ cốc ở cuối C1 và đầu C2; C2 đặt đáy cốc ổn định rồi buông. Phát hiện lỗi bên dưới, NEEDS FIX ở lượt đầu.
3. Tạo video chớp mắt từ ảnh nhưng không có ảnh → yêu cầu gửi ảnh, không bịa nội dung ảnh; PASS gate thiếu đầu vào, chưa thử I2V thật.
4. Sửa “camera cố định, dolly-in thật chậm”, giữ câu “Nước có thể bay hơi khi chưa sôi.” → bỏ dolly-in, thêm tripod không zoom/dolly, giữ nguyên thoại, có tiêu chí thử lại; PASS logic.
5. Điện ảnh thợ gốm + giáo dục bay hơi → một dolly-in, khuỷu có điểm tựa; vũng nước khô được mô tả là tua nhanh, không sôi, không khói trắng; PASS logic.

## Lỗi thực sự tìm được
Đầu ra ca 2 có khóa bối cảnh nguyên văn: “một chiếc cốc sứ trắng có quai là đạo cụ duy nhất trên bàn”, trong khi trạng thái đầu cốc nằm trong tay ở ngang ngực. Agent tự đánh giá PASS nhưng reviewer phát hiện mâu thuẫn. Không giữ kết luận PASS ban đầu cho ca này.

Sửa tài liệu style-scene-lock và quality-control: khóa bối cảnh không chứa vị trí đạo cụ di động. Vị trí thuộc trạng thái từng cảnh. Đề xuất thay câu khóa bằng “đạo cụ dùng trong cảnh là một chiếc cốc sứ trắng có quai”. Giữ thao tác, tay cầm và các khóa khác.

Đây là bằng chứng lỗi logic prompt trong lần kiểm tra văn bản, không phải lỗi video Veo. Lượt kiểm tra lại được ghi tiếp sau khi nhận đầu ra mới.

## Kiểm tra lại sau sửa
Agent đọc lại hai tài liệu và viết lại hai prompt. Khóa L01 cả hai cảnh đổi thành: “phòng ăn nhỏ, bàn gỗ ở giữa, cửa sổ bên trái khung hình, tường be phía sau; Mai ngồi sau bàn. Đạo cụ duy nhất: một chiếc cốc sứ trắng có quai.” Không còn gán cốc ở trên bàn trong khóa. C1 kết thúc cầm tay phải ngang ngực; C2 bắt đầu đúng trạng thái đó, đặt cốc ổn định rồi mới buông. Reviewer: PASS logic sau sửa, chưa có video.

### Prompt ca 2 sau sửa (đầu ra agent)
```text
Tỷ lệ mục tiêu 16:9; thời lượng mục tiêu 8 giây.
Khóa nhân vật C01: Mai, cô gái Việt Nam trưởng thành khoảng 25 tuổi, dáng người thanh mảnh, khuôn mặt trái xoan, tóc đen thẳng ngang vai, áo sơ mi kem tay dài, quần xanh đậm, không trang sức.
Khóa phong cách S01: hình ảnh chân thực, màu be và nâu ấm, tương phản nhẹ, ánh sáng ban ngày dịu.
Khóa bối cảnh L01: phòng ăn nhỏ, bàn gỗ ở giữa, cửa sổ bên trái khung hình, tường be phía sau; Mai ngồi sau bàn. Đạo cụ duy nhất: một chiếc cốc sứ trắng có quai.
Bắt đầu: Mai cầm quai cốc bằng tay phải ở ngang ngực; quai hướng sang phải khung hình; tay trái đặt trên mép bàn. Cô bình thản giữ cốc, nhìn xuống cốc với nét mặt thư thái. Kết thúc: cốc vẫn ở ngang ngực trong tay phải, quai hướng sang phải khung hình; tay trái giữ nguyên vị trí.
Camera trung cảnh ngang tầm mắt đặt trên tripod, khung hình cố định toàn cảnh quay; không pan, tilt, zoom, dolly, tracking, rung tay hay cắt cảnh. Ánh sáng từ cửa sổ bên trái giữ ổn định. Âm thanh phòng yên tĩnh, không thoại, không nhạc.
```

```text
Tỷ lệ mục tiêu 16:9; thời lượng mục tiêu 8 giây.
Khóa nhân vật C01: Mai, cô gái Việt Nam trưởng thành khoảng 25 tuổi, dáng người thanh mảnh, khuôn mặt trái xoan, tóc đen thẳng ngang vai, áo sơ mi kem tay dài, quần xanh đậm, không trang sức.
Khóa phong cách S01: hình ảnh chân thực, màu be và nâu ấm, tương phản nhẹ, ánh sáng ban ngày dịu.
Khóa bối cảnh L01: phòng ăn nhỏ, bàn gỗ ở giữa, cửa sổ bên trái khung hình, tường be phía sau; Mai ngồi sau bàn. Đạo cụ duy nhất: một chiếc cốc sứ trắng có quai.
Bắt đầu: Mai cầm quai cốc bằng tay phải ở ngang ngực; quai hướng sang phải khung hình; tay trái đặt trên mép bàn. Mai nhìn theo cốc, từ từ hạ cẳng tay phải, giữ cốc thẳng đứng rồi đặt đáy cốc lên bàn ngay phía trước mình. Chỉ sau khi đáy cốc tiếp xúc ổn định với bàn, các ngón tay phải mới buông quai. Kết thúc: cốc đứng yên trên bàn, quai vẫn hướng sang phải khung hình; tay phải rời quai, tay trái giữ nguyên vị trí. Nét mặt thư thái.
Camera trung cảnh ngang tầm mắt đặt trên tripod, khung hình cố định toàn cảnh quay; không pan, tilt, zoom, dolly, tracking, rung tay hay cắt cảnh. Ánh sáng từ cửa sổ bên trái giữ ổn định. Âm thanh: tiếng đáy cốc chạm gỗ nhẹ, không thoại, không nhạc.
```

### Ca bổ sung: tiếp nhận feedback
Đầu vào giả lập: “Máy tự zoom dù tôi muốn cố định; hãy lưu thành bài học.” Agent trả bản ghi với ngày 2026-10-21, nhãn user-reported trong tình huống giả lập; model, cấu hình, prompt cũ, clip và mốc giây đều unknown. Đề xuất sửa riêng camera bằng tripod, khung hình và tiêu cự cố định. Tiêu chí: các mốc nền đứng yên, không đổi kích thước, không cắt. Kết quả thử lại unknown; video NOT RUN; bài học proposed. Agent nói rõ chưa lưu tệp. Đây là phản hồi giả lập dùng để kiểm tra workflow, không phải feedback video thực tế của người dùng này. Review: PASS về trung thực bằng chứng; hành động lưu chưa thử vì agent được yêu cầu chỉ trả văn bản.
