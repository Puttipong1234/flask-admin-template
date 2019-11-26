from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)


@app.route('/')
def table():
    return render_template('tables.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/api/sendmail' , methods=["POST"])
def sending():
    req = request.form
    print(req)
    return redirect(url_for('table'))

@app.route('/api/not_approve' , methods=["POST"])
def reject():
    req = request.form
    print(req)
    return redirect(url_for('table'))

if __name__ == '__main__':
    app.run(debug=True)
    