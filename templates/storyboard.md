# Mẫu storyboard

Đây là mẫu có biến có chủ đích; điền mọi biến trước khi xuất cho người dùng. Với ảnh tĩnh, không yêu cầu âm thanh hoặc chuyển động theo thời gian.

```text
Khóa nhân vật: {character_lock}
Khóa phong cách: {style_lock}
Khóa bối cảnh: {scene_lock}
Tổng thời lượng mục tiêu: {total}

| Cảnh | Giây | Trạng thái đầu | Hành động | Camera | Âm thanh | Trạng thái cuối |
|---|---|---|---|---|---|---|
| {scene_id} | {seconds} | {start} | {action} | {camera} | {audio} | {end} |

Prompt độc lập cho cảnh {scene_id}: {full_seven_component_prompt_with_expanded_locks}
```
