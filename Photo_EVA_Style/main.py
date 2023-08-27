from PIL import Image, ImageEnhance, ImageOps
import os
import threading
# 处理函数
def process_image(image_path):
    try:
        # 打开图片
        image = Image.open(image_path)
        color_enhancer = ImageEnhance.Color(image)
        # 色温
        image = color_enhancer.enhance(3)
        # 变红
        image = ImageOps.colorize(image.convert("L"), (0, 0, 0), (227, 47, 35))

        # 保存处理后的图片
        filename = os.path.basename(image_path)
        output_path = os.path.join('./processed_photos', filename)
        image.save(output_path)
        print(f"成功处理照片：{filename}")
        
        return image
    except Exception as e:
        print(f"处理照片{image_path}时出现错误：{str(e)}")
        return None

# 处理照片文件夹下的所有照片
photo_folder = './photos'
processed_folder = './processed_photos'
os.makedirs(processed_folder, exist_ok=True)
show_image = None
while type(show_image) != bool:
    if (show_image := input("是否展示图片 y/n:\n")) == "y":
        show_image = True
    elif show_image == "n":
        show_image = False

def show_image_thread(image):
    image.show()
for filename in os.listdir(photo_folder):
    image_path = os.path.join(photo_folder, filename)
    image = process_image(image_path)
    if show_image and image is not None:
        # 创建新线程，在其中展示图片
        thread = threading.Thread(target=show_image_thread, args=(image,))
        thread.start()