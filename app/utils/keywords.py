import spacy
from collections import Counter
from string import punctuation

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, num_keywords=10):
    # Process the text with spaCy
    doc = nlp(text.lower())
    
    # Filter out stop words and punctuation
    keywords = [token.text for token in doc if not token.is_stop and token.text not in punctuation]
    
    # Get the most common keywords
    keyword_freq = Counter(keywords)
    common_keywords = keyword_freq.most_common(num_keywords)
    
    # Return only the keywords (without frequencies)
    return [keyword for keyword, freq in common_keywords]