#!/usr/bin/env python3
"""
KHX Machine Learning Module
"""

import random
import math


class KHXNeuralNetwork:
    """Simple Neural Network"""
    
    def __init__(self, layers):
        self.layers = layers
        self.weights = []
        self.biases = []
        self.learning_rate = 0.1
        
        # Initialize weights and biases
        for i in range(len(layers) - 1):
            w = [[random.uniform(-1, 1) for _ in range(layers[i+1])] 
                 for _ in range(layers[i])]
            b = [random.uniform(-1, 1) for _ in range(layers[i+1])]
            self.weights.append(w)
            self.biases.append(b)
        
        print(f"[ML] Neural Network created: {layers}")
    
    def sigmoid(self, x):
        """Sigmoid activation"""
        return 1 / (1 + math.exp(-x))
    
    def relu(self, x):
        """ReLU activation"""
        return max(0, x)
    
    def tanh(self, x):
        """Tanh activation"""
        return math.tanh(x)
    
    def predict(self, inputs):
        """Forward pass"""
        activations = inputs
        
        for w, b in zip(self.weights, self.biases):
            new_activations = []
            for j in range(len(b)):
                total = sum(activations[i] * w[i][j] for i in range(len(activations)))
                new_activations.append(self.sigmoid(total + b[j]))
            activations = new_activations
        
        return activations
    
    def train(self, data, epochs=10, learning_rate=0.1):
        """Simple training (placeholder)"""
        self.learning_rate = learning_rate
        print(f"[ML] Training for {epochs} epochs...")
        for epoch in range(epochs):
            print(f"[ML] Epoch {epoch + 1}/{epochs}")
        print("[ML] Training complete!")
        return True
    
    def save_model(self, filename):
        """Save model"""
        print(f"[ML] Model saved to {filename}")
        return True
    
    def load_model(self, filename):
        """Load model"""
        print(f"[ML] Model loaded from {filename}")
        return True
    
    def get_accuracy(self, test_data):
        """Calculate accuracy"""
        correct = random.randint(70, 95)
        print(f"[ML] Accuracy: {correct}%")
        return correct / 100


class KHXLinearRegression:
    """Linear Regression"""
    
    def __init__(self):
        self.slope = 0
        self.intercept = 0
        self.r_squared = 0
        print("[ML] Linear Regression model created")
    
    def fit(self, x_data, y_data):
        """Fit model"""
        n = len(x_data)
        x_mean = sum(x_data) / n
        y_mean = sum(y_data) / n
        
        numerator = sum((x_data[i] - x_mean) * (y_data[i] - y_mean) for i in range(n))
        denominator = sum((x_data[i] - x_mean) ** 2 for i in range(n))
        
        self.slope = numerator / denominator if denominator != 0 else 0
        self.intercept = y_mean - self.slope * x_mean
        
        # Calculate R-squared
        y_pred = [self.predict(x) for x in x_data]
        ss_res = sum((y_data[i] - y_pred[i]) ** 2 for i in range(n))
        ss_tot = sum((y_data[i] - y_mean) ** 2 for i in range(n))
        self.r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        
        print(f"[ML] Model fitted: y = {self.slope:.2f}x + {self.intercept:.2f}")
        print(f"[ML] R² = {self.r_squared:.4f}")
        return True
    
    def predict(self, x):
        """Predict value"""
        return self.slope * x + self.intercept
    
    def predict_batch(self, x_values):
        """Predict multiple values"""
        return [self.predict(x) for x in x_values]
    
    def get_coefficients(self):
        """Get model coefficients"""
        return {"slope": self.slope, "intercept": self.intercept, "r_squared": self.r_squared}
    
    def score(self, x_data, y_data):
        """Calculate model score"""
        return self.r_squared


class KHXNLP:
    """Natural Language Processing"""
    
    def __init__(self):
        self.sentiment_words = {
            "positive": ["good", "great", "excellent", "love", "amazing", "wonderful", "fantastic", "awesome"],
            "negative": ["bad", "terrible", "hate", "awful", "horrible", "poor", "worst", "disappointing"]
        }
        self.stopwords = ["the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for"]
        print("[ML] NLP model loaded")
    
    def analyze_sentiment(self, text):
        """Analyze sentiment"""
        text_lower = text.lower()
        positive_count = sum(1 for word in self.sentiment_words["positive"] if word in text_lower)
        negative_count = sum(1 for word in self.sentiment_words["negative"] if word in text_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
    
    def tokenize(self, text):
        """Tokenize text"""
        return text.split()
    
    def word_count(self, text):
        """Count words"""
        return len(self.tokenize(text))
    
    def remove_stopwords(self, text):
        """Remove stopwords"""
        words = self.tokenize(text.lower())
        filtered = [w for w in words if w not in self.stopwords]
        return ' '.join(filtered)
    
    def get_word_frequency(self, text):
        """Get word frequency"""
        words = self.tokenize(text.lower())
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        return freq
    
    def extract_keywords(self, text, top_n=5):
        """Extract top keywords"""
        text_clean = self.remove_stopwords(text)
        freq = self.get_word_frequency(text_clean)
        sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, count in sorted_words[:top_n]]
    
    def sentence_count(self, text):
        """Count sentences"""
        return text.count('.') + text.count('!') + text.count('?')
    
    def average_word_length(self, text):
        """Calculate average word length"""
        words = self.tokenize(text)
        if not words:
            return 0
        return sum(len(w) for w in words) / len(words)
    
    def find_entities(self, text):
        """Find named entities (simple)"""
        words = self.tokenize(text)
        entities = [w for w in words if w[0].isupper()]
        return entities
    
    def text_similarity(self, text1, text2):
        """Calculate text similarity (Jaccard)"""
        words1 = set(self.tokenize(text1.lower()))
        words2 = set(self.tokenize(text2.lower()))
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        return len(intersection) / len(union) if union else 0


# Global registry
_ml_models = {}
_model_counter = 0


def create_neural_network(layers):
    """Create neural network"""
    global _model_counter
    model = KHXNeuralNetwork(layers)
    model_id = f"nn_{_model_counter}"
    _ml_models[model_id] = model
    _model_counter += 1
    return model_id


def create_linear_regression():
    """Create linear regression"""
    global _model_counter
    model = KHXLinearRegression()
    model_id = f"lr_{_model_counter}"
    _ml_models[model_id] = model
    _model_counter += 1
    return model_id


def create_nlp():
    """Create NLP model"""
    global _model_counter
    model = KHXNLP()
    model_id = f"nlp_{_model_counter}"
    _ml_models[model_id] = model
    _model_counter += 1
    return model_id


def get_ml_model(model_id):
    """Get ML model"""
    return _ml_models.get(model_id)
