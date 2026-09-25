# AI Image Generator

## Project Overview

AI Image Generator is a Generative AI application that creates images from text prompts. It uses the Hugging Face Inference API and provides a simple Streamlit web interface.

## Objective

The objective of this project is to generate creative images from natural language descriptions using a diffusion-based text-to-image model.

## Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- Hugging Face InferenceClient
- FLUX.1-schnell
- Pillow (PIL)

## Features

- Text-to-image generation
- Multiple image styles
- Negative prompt input
- Generation settings
- Image quality enhancement
- Generation history
- Image download
- Simple user interface

## Workflow

1. User enters an image description.
2. User selects an image style.
3. User enters a negative prompt.
4. The prompt is sent to the Hugging Face API.
5. The AI model generates an image.
6. Pillow is used for image quality enhancement.
7. The generated image is displayed.
8. Generation history is maintained and the image can be downloaded.

## Post-Processing

The generated image is enhanced using Pillow by applying:

- Sharpness enhancement
- Contrast enhancement
- Color enhancement
- Unsharp masking

## Testing

The application was tested using different prompts and styles:

| Test | Prompt | Style | Result |
|---|---|---|---|
| 1 | Futuristic city at sunset with flying cars | Realistic | Successful |
| 2 | Cute robot in a futuristic garden | Anime | Successful |
| 3 | Fantasy castle on a mountain with waterfalls | Fantasy | Successful |

## Project Structure

```text
PythonProject/
├── AI_Image_Generator.py
├── AI_Image_Generator_backup.py
├── generated_images/
├── images/
├── metadata/
├── .streamlit/
│   └── secrets.toml
└── README.md

## How It Works

1. The user enters a text prompt.
2. The user selects an image style.
3. An optional negative prompt can be entered.
4. The application creates the final prompt.
5. The prompt is sent to the Hugging Face Inference API.
6. The FLUX.1-schnell model generates the image.
7. The generated image is enhanced and displayed in the Streamlit app.

## Features

- Text-to-image generation
- Multiple image styles
- Optional negative prompt
- AI-generated images using FLUX.1-schnell
- Simple Streamlit interface
- Image sharpness enhancement

## Setup and Installation

Install the required Python libraries:

```bash
pip install streamlit huggingface_hub pillow

## How to Run

Run the following command in the terminal:

```bash
streamlit run AI_Image_Generator.py

## Example Prompts

- A beautiful futuristic city at night, cinematic lighting, highly detailed.
- A peaceful mountain landscape during sunset, realistic photography.
- A cute robot exploring a colorful futuristic world, digital art style.

## Testing Results

The AI Image Generator was tested with different text prompts and image styles. The application successfully generated and displayed AI images using the FLUX.1-schnell model.

## Future Improvements

- Add more image generation models.
- Add image download functionality.
- Add more style options.
- Add image history and gallery.
- Add resolution and aspect-ratio controls.

## Testing Results

The application was tested with different prompts and image styles.

1. Futuristic city at night - Realistic style
2. Cute robot in a futuristic garden - Anime style
3. Fantasy castle in a magical landscape - Digital Art style

All tests successfully generated and displayed AI images.