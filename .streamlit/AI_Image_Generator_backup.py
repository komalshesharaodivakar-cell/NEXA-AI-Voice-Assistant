import streamlit as st
from huggingface_hub import InferenceClient
from io import BytesIO
from PIL import ImageEnhance, ImageFilter

# ---------- PAGE ----------
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 AI Image Generator")
st.write("✨ Turn your imagination into beautiful AI-generated images.")

# ---------- HISTORY ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- INPUT ----------
prompt = st.text_area(
    "📝 Describe your image",
    placeholder="Example: A futuristic city at sunset with flying cars...",
    height=120
)

style = st.selectbox(
    "🎨 Choose an image style",
    [
        "Realistic",
        "Cinematic",
        "Anime",
        "Digital Art",
        "Fantasy",
        "3D Render",
        "Watercolor"
    ]
)
negative_prompt = st.text_area(
    "🚫 Negative Prompt",
    placeholder="Example: blurry, low quality, distorted face, extra fingers, text",
    height=80
)
st.subheader("⚙️ Generation Settings")

col1, col2 = st.columns(2)

with col1:
    steps = st.slider(
        "Inference Steps",
        min_value=10,
        max_value=50,
        value=30,
        step=1
    )

with col2:
    guidance = st.slider(
        "Guidance Scale",
        min_value=1.0,
        max_value=15.0,
        value=7.5,
        step=0.5
    )

seed = st.number_input(
    "Seed",
    min_value=0,
    max_value=999999999,
    value=42,
    step=1
)
generate = st.button(
    "✨ Generate Image",
    width="stretch"
)


# ---------- GENERATE ----------
if generate:

    if not prompt.strip():
        st.warning("⚠️ Please enter an image description first.")

    else:
        try:
            token = st.secrets["HF_TOKEN"]

            client = InferenceClient(
                provider="auto",
                api_key=token
            )

            final_prompt = (
                f"{prompt}. "
                f"Style: {style}, "
                "High quality, highly detailed, professional artwork, "
                "beautiful composition, excellent lighting, sharp details."
            )

            with st.spinner("🎨 Creating your image... Please wait..."):
                if negative_prompt.strip():
                    final_prompt += f", Avoid: {negative_prompt}"
            image = client.text_to_image(
                final_prompt,
                model="black-forest-labs/FLUX.1-schnell"
            )
            image = ImageEnhance.Sharpness(image).enhance(1.3)
            image = ImageEnhance.Contrast(image).enhance(1.1)
            image = ImageEnhance.Color(image).enhance(1.05)
            image = image.filter(
                ImageFilter.UnsharpMask(radius=1, percent=100, threshold=3)
            )

            # Save image in history
            st.session_state.history.insert(
                0,
                {
                    "image": image,
                    "prompt": prompt,
                    "style": style
                }
            )

            st.success("✅ Image generated successfully!")

        except Exception as e:
            st.error("❌ Something went wrong.")
            st.code(str(e))


# ---------- CURRENT IMAGE ----------
if st.session_state.history:

    latest = st.session_state.history[0]

    st.subheader("🖼️ Latest Image")

    st.image(
        latest["image"],
        caption=f"{latest['style']} style",
        width="stretch"
    )

    image_bytes = BytesIO()
    latest["image"].save(image_bytes, format="PNG")
    image_bytes.seek(0)

    st.download_button(
        "⬇️ Download Latest Image",
        data=image_bytes,
        file_name="AI_Generated_Image.png",
        mime="image/png",
        width="stretch"
    )

# ---------- CLEAR HISTORY ----------
if st.session_state.history:
    if st.button("🗑️ Clear Generation History"):
        st.session_state.history = []
        st.rerun()
# ---------- HISTORY ----------
if len(st.session_state.history) > 1:

    st.divider()
    st.subheader("📚 Generation History")

    for index, item in enumerate(st.session_state.history[1:], start=1):

        st.markdown(f"### 🖼️ Image {index}")

        st.image(
            item["image"],
            caption=f"{item['style']} style",
            width="stretch"
        )

        st.write(f"📝 **Prompt:** {item['prompt']}")

        history_bytes = BytesIO()
        item["image"].save(history_bytes, format="PNG")
        history_bytes.seek(0)

        st.download_button(
            "⬇️ Download",
            data=history_bytes,
            file_name=f"AI_Generated_Image_{index}.png",
            mime="image/png",
            key=f"download_{index}",
            width="stretch"
        )