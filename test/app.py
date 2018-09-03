# coding: utf-8
import flask
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()
