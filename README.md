# Financial_News_Sentiment_Prediction
Financial News Sentiment Prediction using Deep Learning (RNN, LSTM, GRU) and FinBERT. This project analyzes finance-related tweets and classifies them as Bearish, Bullish, or Neutral using NLP and Machine Learning techniques.
## Overview
 
This project predicts the sentiment of financial news headlines and articles using a BERT-based deep learning model. Sentiment analysis helps investors and analysts understand market sentiment from news sources.
 
The application uses FinBERT, a domain-specific BERT model trained on financial texts.
 
---
 
## Features
 
- Financial news sentiment classification
- BERT-based NLP model
- Positive, Negative and Neutral sentiment detection
- Real-time prediction through Streamlit
- User-friendly web interface
 
---
 
## Technologies Used
 
- Python
- BERT (Bidirectional Encoder Representations from Transformers)
- FinBERT
- Hugging Face Transformers
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
 
---
 
## Project Structure
 
```text
Financial-News-Sentiment-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── notebook.ipynb
├── dataset/
└── model/
```
 
---
 
## Installation
 
### Clone Repository
 
```bash
git clone https://github.com/yourusername/financial-news-sentiment.git
```
 
### Move to Project Folder
 
```bash
cd financial-news-sentiment
```
 
### Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
---
 
## Running the Application
 
```bash
streamlit run app.py
```
 
Then open:
 
```text
http://localhost:8501
```
 
---
 
## Dataset
 
The dataset contains financial news headlines and corresponding sentiment labels:
 
- Positive
- Negative
- Neutral
 
Possible sources:
 
- Kaggle Financial News Dataset
- Financial PhraseBank Dataset
 
---
 
## Model
 
The model uses FinBERT, a variation of BERT specifically trained for financial sentiment classification.
 
Input:
- Financial headline
- Financial news article
 
Output:
- Positive
- Negative
- Neutral
 
---
 
## Example
 
Input:
 
```text
Company reports record quarterly profits and strong revenue growth.
```
 
Output:
 
```text
Positive
Confidence: 97%
```
 
---
 
## Future Improvements
 
- News scraping integration
- Market trend visualization
- Stock price correlation analysis
- Multi-language support
 
---
 
## Author
 
Hitesh Dagar
