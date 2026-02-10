import os
import joblib
import sys

# Construct the path to the ML model relative to this file
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'ml_model.pkl')
ml_model = None
model_load_error = None

def _load_model():
    """Lazily load the ML model on first use"""
    global ml_model, model_load_error
    if ml_model is None and model_load_error is None:
        try:
            ml_model = joblib.load(MODEL_PATH)
        except FileNotFoundError:
            model_load_error = f"Model file not found at {MODEL_PATH}"
            print(f"Warning: {model_load_error}", file=sys.stderr)
        except Exception as e:
            model_load_error = f"Failed to load ML model: {e}"
            print(f"Warning: {model_load_error}", file=sys.stderr)
            # Try to continue without the model - default to valid (0)
    return ml_model

def check_ml_prediction(features: list) -> int:
    """
    Takes a list of eight features and returns the ML prediction.
    Assumes the model outputs 1 for malicious and 0 for valid.
    Returns 0 (valid/safe) if model is unavailable.
    """
    model = _load_model()
    if model is None:
        # If model can't be loaded, default to safe prediction (0)
        return 0
    
    try:
        prediction = model.predict([features])[0]  # Pass as a 2D array
        return prediction
    except Exception as e:
        print(f"Error during prediction: {e}", file=sys.stderr)
        return 0  # Default to safe prediction if error occurs
