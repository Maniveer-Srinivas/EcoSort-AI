import streamlit as st
from transformers import pipeline
from PIL import Image

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="EcoSort AI",
    page_icon="♻️",
    layout="centered"
)

# --------------------------------------------------
# Load AI Vision Model
# --------------------------------------------------

@st.cache_resource
def load_model():
    return pipeline(
        "image-classification",
        model="google/vit-base-patch16-224"
    )

classifier = load_model()

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("♻️ EcoSort AI")

st.subheader(
    "AI-Powered Smart Waste Segregation Assistant"
)

st.write(
    "Upload an image or enter the name of a waste item. "
    "EcoSort AI provides a waste category and responsible "
    "disposal guidance."
)

# --------------------------------------------------
# User Input
# --------------------------------------------------

uploaded_image = st.file_uploader(
    "📷 Upload an image of the waste:",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:
    st.image(
        uploaded_image,
        caption="Uploaded Waste Image",
        width=300
    )

waste_item = st.text_input(
    "📝 Enter the waste item:",
    placeholder="Example: plastic bottle"
)

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("🔍 Analyze Waste"):

    # ----------------------------------------------
    # IMAGE ANALYSIS
    # ----------------------------------------------

    if uploaded_image is not None:

        with st.spinner("🤖 AI is analyzing the image..."):

            image = Image.open(uploaded_image)

            predictions = classifier(image)

            top_prediction = predictions[0]

            detected_object = top_prediction["label"]
            confidence = top_prediction["score"]

        # Display AI Vision Result
        st.success("✅ Image analysis completed!")

        st.write("### 🤖 AI Vision Result")

        st.write(
            f"**Detected Object:** {detected_object}"
        )

        st.write(
            f"**Vision Model Confidence:** "
            f"{confidence * 100:.2f}%"
        )

        st.progress(confidence)

        # Confidence warning
        if confidence < 0.50:
            st.warning(
                "⚠️ Low AI confidence. Please verify the "
                "waste category before disposal."
            )
        else:
            st.success(
                "✅ The vision model has relatively high "
                "confidence in this detection."
            )

        # ------------------------------------------
        # Convert detected object to waste category
        # ------------------------------------------

        detected = detected_object.lower()

        if any(word in detected for word in [
            "banana",
            "apple",
            "orange",
            "vegetable",
            "fruit"
        ]):

            category = "Wet / Organic Waste"

            reason = (
                "The detected item is generally biodegradable "
                "and can decompose naturally."
            )

            disposal = (
                "Place it in the wet-waste or organic-waste bin."
            )

            tip = (
                "Composting organic waste can help reduce "
                "landfill waste."
            )

        elif any(word in detected for word in [
            "bottle",
            "plastic",
            "can",
            "container",
            "carton"
        ]):

            category = "Dry / Recyclable Waste"

            reason = (
                "The detected item is commonly made from "
                "materials that may be recyclable."
            )

            disposal = (
                "Clean it and place it in the "
                "dry/recyclable waste stream."
            )

            tip = (
                "Recycling can reduce the need for new "
                "raw materials."
            )

        elif any(word in detected for word in [
            "cellular telephone",
            "mobile phone",
            "telephone",
            "laptop",
            "computer",
            "keyboard",
            "mouse"
        ]):

            category = "E-Waste"

            reason = (
                "Electronic devices contain components "
                "that require specialized recycling."
            )

            disposal = (
                "Take it to an authorized e-waste "
                "collection or recycling facility."
            )

            tip = (
                "Do not put electronic waste in regular "
                "household bins."
            )

        else:

            category = "Needs Verification"

            reason = (
                "The vision model detected an object, but "
                "the prototype could not confidently map "
                "it to a supported waste category."
            )

            disposal = (
                "Verify the item using local "
                "waste-management guidelines."
            )

            tip = (
                "When uncertain, verify the correct "
                "disposal method before throwing it away."
            )

        # ------------------------------------------
        # EcoSort Classification
        # ------------------------------------------

        st.write("### ♻️ EcoSort Classification")
        st.caption(
            "The category is generated by mapping the vision model's "
            "detected object to EcoSort's waste-management categories. "
            "For uncertain predictions, users should verify local guidelines."
        )
        st.write(
            f"**Waste Category:** {category}"
        )

        st.write(
            f"**Why this category?** {reason}"
        )

        st.write(
            f"**Recommended Disposal:** {disposal}"
        )

        st.info(
            f"🌱 **Sustainability Tip:** {tip}"
        )

    # ----------------------------------------------
    # TEXT ANALYSIS
    # ----------------------------------------------

    elif waste_item.strip() != "":

        item = waste_item.lower()

        if any(word in item for word in [
            "banana",
            "food",
            "vegetable",
            "fruit",
            "leaves",
            "organic",
            "peel"
        ]):

            category = "Wet / Organic Waste"

            reason = (
                "The item is biodegradable and can generally "
                "decompose naturally."
            )

            disposal = (
                "Place it in the wet-waste or organic-waste bin."
            )

            tip = (
                "Composting organic waste can help reduce "
                "landfill waste."
            )

            confidence = 95

        elif any(word in item for word in [
            "plastic",
            "bottle",
            "paper",
            "cardboard",
            "glass",
            "can",
            "metal"
        ]):

            category = "Dry / Recyclable Waste"

            reason = (
                "The item is commonly made from materials "
                "that may be recyclable."
            )

            disposal = (
                "Clean it and place it in the "
                "dry/recyclable waste stream."
            )

            tip = (
                "Recycling can reduce the need for "
                "new raw materials."
            )

            confidence = 92

        elif any(word in item for word in [
            "phone",
            "mobile",
            "laptop",
            "battery",
            "charger",
            "computer",
            "keyboard",
            "mouse",
            "electronic"
        ]):

            category = "E-Waste"

            reason = (
                "Electronic devices contain components "
                "that require specialized recycling."
            )

            disposal = (
                "Take it to an authorized e-waste "
                "collection or recycling facility."
            )

            tip = (
                "Do not put electronic waste in "
                "regular household bins."
            )

            confidence = 96

        elif any(word in item for word in [
            "medicine",
            "medical",
            "syringe",
            "chemical",
            "paint"
        ]):

            category = "Hazardous Waste"

            reason = (
                "This type of waste may contain substances "
                "that can be harmful if handled incorrectly."
            )

            disposal = (
                "Use an appropriate hazardous-waste "
                "collection facility."
            )

            tip = (
                "Never mix hazardous waste with "
                "regular household waste."
            )

            confidence = 94

        else:

            category = "General Waste"

            reason = (
                "The item could not be confidently matched "
                "to the supported waste categories."
            )

            disposal = (
                "Check local waste-management guidelines "
                "before disposal."
            )

            tip = (
                "Proper segregation helps improve "
                "recycling and waste management."
            )

            confidence = 75

        # ------------------------------------------
        # Text Results
        # ------------------------------------------

        st.success("✅ Waste analysis completed!")

        st.write("### 🔎 Waste Analysis")

        st.write(
            f"**Waste Item:** {waste_item}"
        )

        st.write(
            f"**Waste Category:** {category}"
        )

        st.write(
            f"**Rule-Based Classification Confidence:** "
            f"{confidence}%"
        )

        st.progress(confidence / 100)

        st.write(
            f"**Why this category?** {reason}"
        )

        st.write(
            f"**Recommended Disposal:** {disposal}"
        )

        st.info(
            f"🌱 **Sustainability Tip:** {tip}"
        )

    # ----------------------------------------------
    # No Input
    # ----------------------------------------------

    else:

        st.warning(
            "Please upload a waste image or enter "
            "the name of a waste item."
        )

# --------------------------------------------------
# About Section
# --------------------------------------------------

st.divider()

st.write("### 🌍 About EcoSort AI")

st.write(
    "**Primary SDG:** SDG 12 – Responsible Consumption "
    "and Production"
)

st.write(
    "EcoSort AI helps users identify everyday waste "
    "and provides responsible disposal guidance using "
    "AI-based image recognition and decision support."
)

st.write(
    "**Target Users:** Students, households, offices "
    "and communities"
)

st.write(
    "**AI Role:** Image classification, waste categorization "
    "and disposal decision support"
)

st.write(
    "**Responsible AI:** The system displays model confidence "
    "and warns users when the vision model is uncertain. "
    "Users should verify local disposal rules, especially "
    "for hazardous and electronic waste."
)