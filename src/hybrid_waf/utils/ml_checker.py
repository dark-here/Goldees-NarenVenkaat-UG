import os
import joblib

# Construct the path to the ML model relative to this file
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'ml_model.pkl')

# Load the model with error handling
ml_model = None
try:
    if os.path.exists(MODEL_PATH):
        ml_model = joblib.load(MODEL_PATH)
    else:
        print(f"Warning: ML model not found at {MODEL_PATH}")
except Exception as e:
    print(f"Error loading ML model: {e}")

def check_ml_prediction(features: list) -> int:
    """
    Takes a list of eight features and returns the ML prediction.
    Assumes the model outputs 1 for malicious and 0 for valid.
    Returns 0 (valid) if model is not available.
    """
    if ml_model is None:
        print("Warning: ML model not available, returning 0 (valid)")
        return 0
    
    try:
        prediction = ml_model.predict([features])[0]  # Pass as a 2D array
        return int(prediction)
    except Exception as e:
        print(f"Error in ML prediction: {e}")
        return 0
