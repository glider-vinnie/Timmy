from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
CORS(app)

# Sample training data
training_data = [
    ("I love this product!", "positive"),
    ("This is amazing!", "positive"),
    ("Great experience!", "positive"),
    ("I hate this!", "negative"),
    ("This is terrible!", "negative"),
    ("Worst experience ever!", "negative"),
    ("The product is okay.", "neutral"),
    ("It's fine, I guess.", "neutral"),
    ("Not bad, not great.", "neutral")
]

# Preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Prepare training data
X_train = [preprocess_text(text) for text, _ in training_data]
y_train = [label for _, label in training_data]

# Create and train the model
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Response templates based on sentiment
response_templates = {
    "positive": [
        "I'm glad you're feeling positive!",
        "That's great to hear!",
        "I'm happy to hear that!"
    ],
    "negative": [
        "I'm sorry to hear that.",
        "That doesn't sound good.",
        "I understand your frustration."
    ],
    "neutral": [
        "I see.",
        "Interesting.",
        "I understand."
    ]
}

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Preprocess and predict
    processed_message = preprocess_text(message)
    X_message = vectorizer.transform([processed_message])
    sentiment = model.predict(X_message)[0]
    
    # Get a random response based on sentiment
    response = np.random.choice(response_templates[sentiment])
    
    return jsonify({
        'sentiment': sentiment,
        'response': response
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000) 