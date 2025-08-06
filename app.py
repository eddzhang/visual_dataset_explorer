import streamlit as st
import pandas as pd
from PIL import Image
from itertools import islice
import os

LABELS_CSV = "flowerLabels.csv"
IMAGE_FOLDER = "flowerImages"

st.set_page_config(layout = "wide")
st.title("Visual Dataset Explorer")

# load labels
try:
    df = pd.read_csv(LABELS_CSV)
except FileNotFoundError:
    st.error("labels.csv not found.")
    st.stop()


# sidebar: filter by label
labels = df['label'].dropna().unique()
selected_label = st.sidebar.selectbox("Filter by label", options=["All"] + sorted(labels.tolist()))

# applying filter
if selected_label != "All":
    filtered_df = df[df['label'] == selected_label]
else:
    filtered_df = df

st.write(f"Displaying {len(filtered_df)} images")

# Display images
rows = list(filtered_df.iterrows())
for i in range(0, len(rows), 4):
    cols = st.columns(4)
    for col, (_, row) in zip(cols, rows[i:i+4]):
        img_path = os.path.join(IMAGE_FOLDER, row['filename'])
        try:
            img = Image.open(img_path)
            col.image(img, caption=row['label'], use_container_width=True)
        except FileNotFoundError:
            col.warning(f"Image not found: {row['filename']}")
