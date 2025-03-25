import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('IMG_4073.jpg')

# 이미지 불러오기 실패 시 예외 처리
if img is None:
    print("이미지를 불러오지 못했습니다. 경로 또는 파일명을 확인하세요.")
    exit()

# 리사이즈 (너비가 800보다 크면 축소)
height, width = img.shape[:2]
if width > 800:
    scale = 800 / width
    img = cv2.resize(img, (int(width * scale), int(height * scale)))

# ==============================
# 강한 카툰 효과 (Strong Cartoon)
# ==============================
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur(gray, 5)
edges_strong = cv2.adaptiveThreshold(
    gray_blur, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    9, 5
)
color_strong = cv2.bilateralFilter(img, 9, 300, 300)
cartoon_strong = cv2.bitwise_and(color_strong, color_strong, mask=edges_strong)

# 저장
cv2.imwrite("cartoon_strong.jpg", cartoon_strong)

# ==============================
# 약한 카툰 효과 (Soft Cartoon)
# ==============================
edges_soft = cv2.adaptiveThreshold(
    gray_blur, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11, 9
)
color_soft = cv2.bilateralFilter(img, 5, 100, 100)
cartoon_soft = cv2.bitwise_and(color_soft, color_soft, mask=edges_soft)

# 저장
cv2.imwrite("cartoon_soft.jpg", cartoon_soft)

# ==============================
# 결과 확인용 출력 (선택)
# ==============================
cv2.imshow("Cartoon (Strong)", cartoon_strong)
cv2.imshow("Cartoon (Soft)", cartoon_soft)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("이미지 저장 완료! cartoon_strong.jpg / cartoon_soft.jpg")
