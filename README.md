
<img src="https://raw.githubusercontent.com/Li-Yan/gemini-auto-travel-postcard/main/demo/demo.gif" alt="drawing" style="width:800px;"/>

# Desctiption
Given an image, this python tool will use Gemini to get the city of this place and generate a postcard with a watercolor painting of the city.

Let us look at its **AMAZING** result!!!

Check this video for the demo: https://youtu.be/oX28FZ90fZI?si=CfkfIZjfwoddfW-F

Here are the beautiful postcards this tool generates:

| ![output](https://raw.githubusercontent.com/Li-Yan/gemini-auto-travel-postcard/main/output_example/san_francisco_postcard.png) | ![output](https://raw.githubusercontent.com/Li-Yan/gemini-auto-travel-postcard/main/output_example/shanghai_postcard.png)  |
|:--:|:--:|
| ![output](https://raw.githubusercontent.com/Li-Yan/gemini-auto-travel-postcard/main/output_example/mexico_city_postcard.png)  | ![output](https://raw.githubusercontent.com/Li-Yan/gemini-auto-travel-postcard/main/output_example/paris_postcard.png)  |

# Details

The app does the following:
 1. Use Gemini API to identify the city where the image is taken.
 2. Use Gemini API to identify the country color of the country the city belongs to.
 3. Use Gemini API to generate a poetry of the city.
 4. Add postcard title with the country color fetched in step #2.
 5. Add text to the postcard with the poetry of the city.
 6. Export the postcard to an image.

# Usage

## Step1: Get Google AI Studio API Key

Go to link to get the API key: https://aistudio.google.com/app/apikey

In terminal
```bash
export API_KEY=<YOUR_API_KEY>
```

## Step 2: Google Cloud Login

Interminal
```bash
gcloud init
gcloud auth application-default login
```

## Step 3: Run the python app
```bash
python ./auto_travel_postcard.py
```
