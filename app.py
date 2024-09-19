"""Ejemplo de Flask con docker y kubernetes y github actions"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """ Retornando un saludo Simple"""
    return "Hello, World! This is a simple Python app running in Docker and Kubernetes."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
