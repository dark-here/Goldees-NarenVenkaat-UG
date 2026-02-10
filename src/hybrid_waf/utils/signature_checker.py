# Signature-based threat detection

def check_signatures(payload: str) -> bool:
    """
    Check payload against known malicious signatures.
    Returns True if malicious signature is found, False otherwise.
    """
    malicious_patterns = [
        "<script>",
        "javascript:",
        "onerror=",
        "onclick=",
        "union select",
        "drop table",
        "'; drop",
    ]
    
    payload_lower = payload.lower()
    for pattern in malicious_patterns:
        if pattern in payload_lower:
            return True
    
    return False

def get_signature_matches(payload: str) -> list:
    """
    Get list of signatures that match in the payload.
    """
    matches = []
    malicious_patterns = [
        "<script>",
        "javascript:",
        "onerror=",
        "onclick=",
        "union select",
        "drop table",
        "'; drop",
    ]
    
    payload_lower = payload.lower()
    for pattern in malicious_patterns:
        if pattern in payload_lower:
            matches.append(pattern)
    
    return matches