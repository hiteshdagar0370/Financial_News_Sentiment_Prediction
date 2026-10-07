import streamlit as st
from transformers import pipeline
 
# Load sentiment model
@st.cache_resource
def load_model():
return pipeline(
"sentiment-analysis",
model="ProsusAI/finbert"
)
 
classifier = load_model()
 
st.title("Financial News Sentiment Prediction using BERT")
 
st.write(
"Enter a financial news headline or article and predict its sentiment."
)
 
news_text = st.text_area(
"Financial News Text",
height=150
)
 
if st.button("Predict Sentiment"):
if news_text.strip():
result = classifier(news_text)
 
sentiment = result[0]["label"]
confidence = result[0]["score"]
 
st.success(f"Sentiment: {sentiment}")
st.write(f"Confidence Score: {confidence:.2%}")
else:
st.warning("Please enter some news text.")
