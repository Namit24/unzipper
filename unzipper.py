import streamlit as st
import zipfile
import io
from PIL import Image

st.set_page_config(page_title="Image Zip Viewer", layout="wide")
st.title("📂 Zip Image Viewer")

uploaded_zip = st.file_uploader("Upload a ZIP file with images", type="zip")

if uploaded_zip is not None:
    with zipfile.ZipFile(uploaded_zip) as zip_file:
        image_files = [f for f in zip_file.namelist() if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        if not image_files:
            st.warning("No image files found in the zip.")
        else:
            st.success(f"Found {len(image_files)} image(s) in the zip.")
            cols = st.columns(3)

            for i, file_name in enumerate(image_files):
                with zip_file.open(file_name) as file:
                    image = Image.open(file).convert("RGB")
                    cols[i % 3].image(image, caption=file_name, use_column_width=True)
