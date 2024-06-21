def get_rgb_from_hexadecimal(color_rgb):
	if color_rgb[0] == '#':
		r = int(color_rgb[1:3], 16)
		g = int(color_rgb[3:5], 16)
		b = int(color_rgb[5:7], 16)
		return r, g, b
	else:
		r = int(color_rgb[0:2], 16)
		g = int(color_rgb[2:4], 16)
		b = int(color_rgb[4:6], 16)
		return r, g, b

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

# identify city from image
image_to_text_prompt = "Name of the city in the picture in one or two words"
image1 = {
    'mime_type': 'image/jpeg',
    'data': pathlib.Path(input_image_path).read_bytes()
}
city_name_response = model.generate_content([image_to_text_prompt, image1])
city_name = city_name_response.text
print("City name is: ", city_name)

# get color of the country the city belongs to
city_color_prompt = f"What is the triditional color of country of the city {city_name} in one word"
city_color_response = model.generate_content(city_color_prompt)
city_color = city_color_response.text
city_color_rgb_prompt = f"What is the rgb of color {city_color} into hexadecimal format, pick any one and return just one result"
city_color_rgb_response = model.generate_content(city_color_rgb_prompt)
city_color_rgb = city_color_rgb_response.text
r, g, b = get_rgb_from_hexadecimal(city_color_rgb)
print(f"City color is: {city_color} {city_color_rgb} ({r},{g},{b})")

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
text_font = ImageFont.truetype(font='./RousseauDeco.ttf', size=230)
image_draw.text(
	xy = (100, 100),
	text = city_name,
	align = 'center',
	font = text_font,
	fill = (r, g, b)
	)

image.show()
