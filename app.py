from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def table():
    return render_template('tables.html')

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    