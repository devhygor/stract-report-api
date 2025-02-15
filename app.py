from flask import Flask
from routes.reports import reports_bp

app = Flask(__name__, template_folder='templates')

app.register_blueprint(reports_bp)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
