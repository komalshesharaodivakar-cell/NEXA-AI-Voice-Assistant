import streamlit as st
import os
import json
from datetime import datetime
from huggingface_hub import InferenceClient
from PIL import ImageEnhance, ImageFilter

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨"
)

st.title("🎨 AI Image Generator")

st.write("Enter a description and generate an image using AI.")

prompt = st.text_input(
    "Enter your image prompt:",
    placeholder="Example: A beautiful futuristic city at sunset, cinematic, highly detailed"
)
style = st.selectbox(
                "Choose an image style:",
                ["Realistic", "Cinematic", "Anime", "Digital Art", "3D"]
)
steps = st.slider(
                "Inference Steps",
                min_value=1,
                max_value=10,
                value=4,
                step=1
)
guidance_scale = st.slider(
                "Guidance Scale",
                min_value=1.0,
                max_value=15.0,
                value=7.5,
                step=0.5
)
seed = st.number_input(
                "Seed",
                min_value=0,
                value=42,
                step=1
)
negative_prompt = st.text_input("Negative prompt (optional):", "")

if st.button("Generate Image"):
    if not prompt.strip():
        st.warning("Please enter an image prompt.")
    else:
        try:
            token = st.secrets["HF_TOKEN"]

            client = InferenceClient(
                provider="auto",
                api_key=token
            )

            final_prompt = (
                f"{prompt}, {style} style, "
                "high quality, highly detailed, professional artwork, "
                "beautiful composition, excellent lighting."
            )

            if negative_prompt.strip():
                final_prompt += f". Avoid: {negative_prompt}"

            with st.spinner("🎨 Generating your image... Please wait..."):

                image = client.text_to_image(
                    prompt=final_prompt,
                    model="black-forest-labs/FLUX.1-schnell",
                    num_inference_steps=steps,
                    guidance_scale=guidance_scale,
                    seed=seed
                )

            st.success("🟩 Image generated successfully!")

            st.image(
                image,
                caption="Generated Image",
                use_container_width=True
            )

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_filename = f"generated_{timestamp}.png"

            image_path = os.path.join(
                "generated_images",
                image_filename
            )

            image.save(image_path)

            st.success("Image and metadata saved successfully!")

        except Exception as e:
            st.error("❌ Something went wrong.")
            st.code(str(e))