from PIL import Image
import easyocr
from utils.custom_logger import Log_Maker


def Read_Captcha(screenshot_path):
    logger = Log_Maker.log_gen()
    Cut_Image(screenshot_path)
    reader = easyocr.Reader(['en'])
    results = reader.readtext(".\\temp\\div_screenshot_cropped.png", detail=1)

    sorted_results = sorted(results, key=lambda r: r[0][0][0])
    text = ''.join([r[1] for r in sorted_results])
    text1 = text.replace(" ", "")
    print(text1)
    logger.info(f"---> Captcha TEXT: {text}")
    return text1

def Cut_Image(screenshot_path):
    with Image.open(screenshot_path) as img:
        width, height = img.size
        cropped_img = img.crop((1, 1, width - 1, height - 1))
        cropped_img.save(".\\temp\\div_screenshot_cropped.png")
