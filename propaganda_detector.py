import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from sentence_transformers import SentenceTransformer, util

# Load pre-trained models
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

# Mock database of known propaganda narratives
known_narratives = {
    "climate_change_hoax": "Climate change is a hoax invented by scientists for funding.",
    "vaccine_microchip": "COVID-19 vaccines contain microchips for population control.",
    "flat_earth": "The Earth is flat, and space agencies are hiding the truth.",
}

# Function to detect potential propaganda
def detect_propaganda(text):
    sentiment = sentiment_pipeline(text)[0]
    if sentiment['label'] == 'NEGATIVE' and sentiment['score'] > 0.8:
        return True
    return False

# Function to link text to known narratives
def link_to_narratives(text):
    text_embedding = sentence_model.encode(text, convert_to_tensor=True)
    linked_narratives = []
    for name, narrative in known_narratives.items():
        narrative_embedding = sentence_model.encode(narrative, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(text_embedding, narrative_embedding)
        if similarity > 0.5:
            linked_narratives.append((name, narrative, similarity.item()))
    return sorted(linked_narratives, key=lambda x: x[2], reverse=True)

# Function to generate explanation
def generate_explanation(text, linked_narratives):
    if not linked_narratives:
        return "No known propaganda narratives detected."
    
    explanation = "This text contains elements similar to known propaganda narratives:\n\n"
    for name, narrative, similarity in linked_narratives:
        explanation += f"- {name.replace('_', ' ').title()}:\n"
        explanation += f"  Similarity: {similarity:.2f}\n"
        explanation += f"  Known narrative: {narrative}\n\n"
    explanation += "These narratives are known to be false or misleading. Always verify information from reliable sources."
    return explanation

# Streamlit UI
st.title("Propaganda Detection and Analysis Prototype")

user_input = st.text_area("Enter text to analyze:")

if st.button("Analyze"):
    if user_input:
        is_propaganda = detect_propaganda(user_input)
        if is_propaganda:
            st.warning("Potential propaganda detected!")
            linked_narratives = link_to_narratives(user_input)
            explanation = generate_explanation(user_input, linked_narratives)
            st.write(explanation)
        else:
            st.success("No potential propaganda detected.")
    else:
        st.error("Please enter some text to analyze.")
