
from PIL import Image
path = "/Users/anhnd/Desktop/"
images = """Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.08.10.png
Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.08.29.png
Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.08.40.png
Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.08.43.png
Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.08.47.png
Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.09.03.png
Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.09.07.png
Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.09.13.png
Simulator Screenshot - IPhone 11 Pro Max 6.5 inch - 2023-08-27 at 10.09.18.png""".split("\n")
print(images)
for image_name in images:
    image = Image.open(path  + image_name)
    print(image)
    new_image = image.resize((1284, 2778))
    new_image.save(image_name)