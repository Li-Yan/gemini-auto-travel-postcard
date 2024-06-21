### Show a dialog for inputing image
from tkinter.filedialog import askopenfilename

input_image_path = askopenfilename()
print("Input image file: ", input_image_path)

### Sumary of input
import google.generativeai as genai
import pathlib
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

image_to_text_prompt = "What is name of the city in the picture"
image1 = {
    'mime_type': 'image/jpeg',
    'data': pathlib.Path(input_image_path).read_bytes()
}

response = model.generate_content([image_to_text_prompt, image1])
city_name = response.text

print("City name is: ", city_name)

### Generate image
from vertexai.preview.vision_models import ImageGenerationModel

image_prompt = f"please show a watercolor image of tourist attractions in {city_name}"
print("Image prompt: ", image_prompt)

model = ImageGenerationModel.from_pretrained("imagegeneration@006")
images = model.generate_images(
	prompt=image_prompt,
    number_of_images=1,
    aspect_ratio= "4:3",
	)

images[0].save(location="./gen-img.png", include_generation_parameters=True)

### Add Text Font onto the Image and Display
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

image = Image.open('./gen-img.png')
image_draw = ImageDraw.Draw(image)
# text_font = ImageFont.truetype('FreeMono.ttf', 65)
image_draw.text(
	xy = (96, 96),
	text = city_name,
	align = 'center',
	# font = ImageFont,
	fill = (255, 0, 0)
	)

image.show()

