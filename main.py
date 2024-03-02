import streamlit as st
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load spaCy model
nlp = spacy.load('en_core_web_lg')

# Mapping of full country names to their codes
country_mapping = {
    "United States": "US",
    "United Kingdom": "UK",
    "India": "IN",
    "Canada": "CA",
    "Australia": "AU",
    "France": "FR",
    "Germany": "DE",
    "Japan": "JP",
    "Italy": "IT",
    "Brazil": "BR",
    "Mexico": "MX",
    "Spain": "ES",
    "Netherlands": "NL",
    "Russia": "RU",
    "China": "CN",
    "South Korea": "KR",
    "Singapore": "SG",
    "Saudi Arabia": "SA",
    "United Arab Emirates": "AE",
    "New Zealand": "NZ"
}

# Transform country names into spaCy vectors
country_vectors = np.array([nlp(name).vector for name in country_mapping.keys()])

def find_closest_match(user_input, country_vectors, country_mapping):
    user_vector = nlp(user_input).vector
    similarities = cosine_similarity([user_vector], country_vectors)
    closest_idx = np.argmax(similarities)
    closest_country = list(country_mapping.values())[closest_idx]
    return closest_country

# Streamlit UI
st.title('Closest Match')

user_input = st.text_input('Enter a String:')
if user_input:
    closest_country = find_closest_match(user_input, country_vectors, country_mapping)
    st.write(f'Closest match to "{user_input}" is "{closest_country}"')
