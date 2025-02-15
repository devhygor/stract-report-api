from flask import Flask
from routes.reports import reports_bp

app = Flask(__name__)

# Registrando os blueprints das rotas
app.register_blueprint(reports_bp)

@app.route("/")
def home():
    return {
        "name": "Hygor Melo Rocha",
        "email": "hygor.k92@gmail.com.br",
        "linkedin": "https://www.linkedin.com/in/devhygor/"
    }

if __name__ == "__main__":
    app.run(debug=True)
