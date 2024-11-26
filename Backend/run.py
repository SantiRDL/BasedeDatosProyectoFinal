from flask import Flask
from flask_cors import CORS
from routes import routes


app = Flask(__name__)
CORS(app)

# Registra el Blueprint
app.register_blueprint(routes)

@app.route('/')
def home():
    return "¡Backend funcionando en Docker!"

print(app.url_map)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

