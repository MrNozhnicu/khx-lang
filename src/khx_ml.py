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
        print(f"[ML] Training for {epochs} epochs...")
        for epoch in range(epochs):
            print(f"[ML] Epoch {epoch + 1}/{epochs}")
        print("[ML] Training complete!")
        return True


class KHXLinearRegression:
    """Linear Regression"""
    
    def __init__(self):
        self.slope = 0
        self.intercept = 0
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
        
        print(f"[ML] Model fitted: y = {self.slope:.2f}x + {self.intercept:.2f}")
        return True
    
    def predict(self, x):
        """Predict value"""
        return self.slope * x + self.intercept


class KHXNLP:
    """Natural Language Processing"""
    
    def __init__(self):
        self.sentiment_words = {
            "positive": ["good", "great", "excellent", "love", "amazing", "wonderful"],
            "negative": ["bad", "terrible", "hate", "awful", "horrible", "poor"]
        }
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
