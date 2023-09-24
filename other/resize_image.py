
from PIL import Image
path = "/Users/anhnd/Downloads/group_2023-09-12/"
images = """group@3x.png""".split("\n")
print(images)
for image_name in images:
    image = Image.open(path  + image_name)
    print(image)
    new_image = image.resize((512, 512))
    new_image.save(image_name)