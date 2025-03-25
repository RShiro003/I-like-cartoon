# Cartoon Style Image Converter 🎨

Convert real-world images into cartoon-style illustrations using OpenCV.

---

## ✅ Features

- Converts any input image into a cartoon-like version
- Supports **strong** and **soft** cartoon effects
- Uses OpenCV image processing techniques (edge detection + bilateral filtering)

---

## 🖼️ Cartoon Examples

### ▶️ Strong Cartoon Effect (진하게)
![cartoon_strong](cartoon_strong.jpg)

> 색감이 과장되고 윤곽선이 굵게 표현됨. 애니메이션 스타일 느낌에 가까움.

---

### ▶️ Soft Cartoon Effect (자연스럽게)
![cartoon_soft](cartoon_soft.jpg)

> 원본과 유사한 색감 유지. 윤곽선도 얇게 처리되어 현실적인 느낌 유지.

---

## 📌 잘 된 결과 vs 잘 안 된 결과

| 유형 | 설명 | 결과 |
|------|------|------|
| 잘 된 이미지 | 인물 중심, 배경 단순함 | 👍 윤곽선이 잘 표현되고 깔끔한 효과 |
| 잘 안 된 이미지 | 배경 복잡, 조명 어두움 | ⚠️ 윤곽선이 뭉개지거나 경계 흐릿 |

---

## ⚠️ 한계점

- 배경이 복잡한 경우 엣지 검출이 부정확해질 수 있음
- 너무 밝거나 어두운 조명에서는 필터가 이상하게 적용될 수 있음
- 해상도가 너무 큰 이미지는 처리 속도가 느림 → 리사이즈 필요
- 고속 실시간 처리는 어려움 (느린 연산)

---

## 💻 How to Run

```bash
pip install opencv-python
python Main.py
