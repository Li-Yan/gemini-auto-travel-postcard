### Show a dialog for inputing image
from tkinter.filedialog import askopenfilename

filename = askopenfilename()
print("Input image file: ", filename)

### Sumary of input
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What is name of the city in the picture")

place_name = "Paris"

print(response.text)

### Generate image
from vertexai.preview.vision_models import ImageGenerationModel

image_prompt = f"please show a Generate a visually captivating and refreshing image of {place_name}"
# image_prompt = "Generate a visually captivating and refreshing image of a glass of freshly squeezed lemonade against a vibrant background. The lemonade should be served in a tall, clear glass, with condensation dripping down the sides. Add a wedge of lemon and a sprig of mint for added freshness and visual appeal. Set the glass of lemonade against a vibrant gradient backdrop, creating a sense of depth and dimension. Ensure the lighting enhances the translucency of the lemonade and the texture of the lemon wedge. Experiment with vibrant color tones and a photorealistic art style to make the image pop."
print("Image prompt: ", image_prompt)

model = ImageGenerationModel.from_pretrained("imagegeneration@005")
images = model.generate_images(prompt=image_prompt)

images[0].save(location="./gen-img.png", include_generation_parameters=True)