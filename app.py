# Main Flask App

from src.hybrid_waf.routes.main import app

if __name__ == '__main__':
    app.run(debug=True)