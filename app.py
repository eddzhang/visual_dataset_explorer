import streamlit as st
import pandas as pd
from PIL import Image
import os

LABELS_CSV = "labels.csv"
IMAGE_FOLDER = "images"

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
selected_label = st.sidebar.selectbox("Filter by label", options["All"] + sorted(labels.tolist()))

# applying filter
if selected_label != "All":
    filtered_df = df[df['label'] == selected_label]
else:
    filtered_df = df

st.write(f"Displaying {len(filtered_df)} images")

# display images in grid
cols = st.columns(4)
for idx,row in filtered_df.iterrows():
    img_path = os.path.join(IMAGE_FOLDER, row['filename'])
    try:
        img = Image.open(img_path)
        with cols[idx % 4]:
            st.image(img, caption=row['label'], use_column_width=True)
    except FileNotFoundError:
        st.warning(f"Image not found: {row['filename']}")