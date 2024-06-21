import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What is name of the city in the picture")

print(response.text)

from IPython.display import Image
from vertexai.preview.vision_models import ImageGenerationModel

model = ImageGenerationModel.from_pretrained("imagegeneration@005")
images = model.generate_images(prompt=response.text)

images[0].save(location="./gen-img1.png", include_generation_parameters=True)

Image('./gen-img1.png', height=500)