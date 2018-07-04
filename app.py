from connexion.resolver import RestyResolver
from flask import Flask
from flask import render_template
import connexion


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    app.add_api('api.yaml', resolver=RestyResolver('api'))
    app.run(host='127.0.0.1', port=9090)
