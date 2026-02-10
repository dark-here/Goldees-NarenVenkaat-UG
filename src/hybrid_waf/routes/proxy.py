# Proxy route for WAF functionality

from flask import request, jsonify
from src.hybrid_waf.utils.ml_checker import check_ml_prediction
from src.hybrid_waf.utils.signature_checker import check_signatures
from src.hybrid_waf.utils.preprocessor import extract_features, preprocess_payload

def process_request(request_obj):
    """
    Process incoming request and determine if it's malicious.
    Uses both signature-based and ML-based detection.
    """
    try:
        # Get request data
        payload = request_obj.get_data(as_text=True) or ""
        
        # Signature-based check
        if check_signatures(payload):
            return {
                "status": "blocked",
                "reason": "Malicious signature detected",
                "detection_type": "signature"
            }
        
        # ML-based check
        features = extract_features({
            "payload": payload,
            "method": request_obj.method,
            "path": request_obj.path
        })
        
        if check_ml_prediction(features) == 1:
            return {
                "status": "blocked",
                "reason": "ML model flagged as malicious",
                "detection_type": "ml"
            }
        
        return {
            "status": "allowed",
            "reason": "Request passed all checks",
            "detection_type": "none"
        }
    
    except Exception as e:
        return {
            "status": "error",
            "reason": str(e),
            "detection_type": "error"
        }