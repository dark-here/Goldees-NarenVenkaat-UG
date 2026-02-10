# Main Flask App

import sys
import os

# Add the current directory to the path to ensure imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.hybrid_waf.routes.main import app

if __name__ == '__main__':
    print("Starting Hybrid WAF Application...")
    print(f"Running on http://localhost:5000")
    app.run(debug=True)