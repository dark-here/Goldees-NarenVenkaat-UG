# Request feature extraction utilities

def extract_features(request_data: dict) -> list:
    """
    Extract features from request data for ML model.
    Currently a placeholder that returns a default feature vector.
    """
    # TODO: Implement actual feature extraction logic
    # Should return a list of 8 features for ML model
    return [0] * 8

def preprocess_payload(payload: str) -> str:
    """
    Preprocess request payload for signature checking.
    """
    # TODO: Add payload normalization and preprocessing
    return payload