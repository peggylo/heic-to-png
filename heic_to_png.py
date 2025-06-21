from PIL import Image
import pillow_heif
import os

# 檔案名稱
input_file = 'IMG_2776.HEIC'
output_file = 'IMG_2776.png'

# 讀取HEIC圖片
heif_file = pillow_heif.read_heif(input_file)
image = Image.frombytes(
    heif_file.mode,
    heif_file.size,
    heif_file.data,
    "raw"
)

# 儲存為PNG
image.save(output_file, format='PNG')

print(f'已將 {input_file} 轉換為 {output_file}') 