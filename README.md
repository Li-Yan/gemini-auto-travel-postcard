# Desctiption
Given an image, this python tool will use Gemini to get the city of this place and generate a postcard of the city.

Let us look at its **AMAZING** result!!!

| ![sample1](https://raw.githubusercontent.com/Li-Yan/gemini-auto-travel-postcard/main/input_examples/Shanghai.jpg) | ![output](https://raw.githubusercontent.com/Li-Yan/gemini-auto-travel-postcard/main/output_example/Shanghai%2C%20China_postcard.png)  |
|:--:|:--:|
| input image  | output image  |

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
