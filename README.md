# ♻️ EcoSort AI

## AI-Powered Smart Waste Segregation and Disposal Assistant

EcoSort AI is an AI-powered sustainability application designed to help users identify everyday waste and understand how it should be segregated and disposed of responsibly.

The system accepts either an image of a waste item or a text description. For image input, a pretrained Vision Transformer (ViT) model identifies the most likely object. EcoSort AI then maps the detected object to a waste-management category and provides disposal guidance and a sustainability tip.

---

## 🌍 Sustainable Development Goal

### SDG 12 – Responsible Consumption and Production

EcoSort AI supports responsible waste segregation and disposal by helping users make better decisions about everyday waste.

---

## 🎯 Problem Statement

Improper waste segregation is a common sustainability challenge. People may not always know whether an item belongs to wet/organic waste, dry/recyclable waste, e-waste, hazardous waste, or general waste.

Incorrect segregation can reduce recycling efficiency and may result in inappropriate disposal of materials.

EcoSort AI aims to make waste identification and disposal guidance easier and more accessible using AI-based image recognition and decision support.

---

## 💡 Solution

EcoSort AI provides two ways to analyze waste:

### 1. Image-Based Analysis
Users can upload an image of a waste item.

The application:

1. Processes the uploaded image.
2. Uses a pretrained Vision Transformer (ViT) model for image classification.
3. Identifies the most likely object.
4. Maps the detected object to a waste category.
5. Provides disposal guidance.
6. Displays a sustainability tip.
7. Shows model confidence and provides a warning when confidence is low.

### 2. Text-Based Analysis

Users can enter the name of a waste item, such as:

- Plastic bottle
- Banana peel
- Old mobile phone
- Battery
- Paper
- Glass

The application identifies the corresponding waste category and provides disposal guidance.

---

## 🤖 AI Elements Used

- Vision Transformer (ViT)
- Image Classification
- Hugging Face Transformers
- PyTorch
- AI-based decision support
- Confidence-based uncertainty handling
- Rule-based waste categorization for text input

### Vision Model

The prototype uses:

`google/vit-base-patch16-224`

This is a pretrained image-classification model used to identify objects in uploaded images.

**Note:** The displayed vision confidence represents the confidence of the vision model in its detected object label. It is not a guarantee that the final waste category is correct.

---

## ♻️ Waste Categories

EcoSort AI currently supports categories such as:

- 🟢 Wet / Organic Waste
- 🔵 Dry / Recyclable Waste
- 🔴 E-Waste
- ⚠️ Hazardous Waste
- ⚪ General Waste
- 🔍 Needs Verification

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| Hugging Face Transformers | AI model integration |
| PyTorch | Machine learning framework |
| Vision Transformer (ViT) | Image classification |
| Pillow | Image processing |
| Git & GitHub | Version control and project hosting |

---

## 👥 Target Users

EcoSort AI is designed for:

- Students
- Households
- Office users
- Educational institutions
- Local communities

---

## 🔄 System Workflow

```text
User
  ↓
Upload Waste Image / Enter Waste Name
  ↓
AI Vision Model / Text Classification
  ↓
Object or Waste Item Identification
  ↓
Waste Category Mapping
  ↓
Disposal Recommendation
  ↓
Sustainability Tip
  ↓
Responsible AI Warning When Required
