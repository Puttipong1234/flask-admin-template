from flask import Flask , render_template , request

app = Flask(__name__)


@app.route('/')
def table():
    return render_template('tables.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/api/sendmail/<userid>')
def sending(userid):
    req = request.form
    print(req)

if __name__ == '__main__':
    app.run(debug=True)
    