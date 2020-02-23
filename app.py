from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
    import pdb; pdb.set_trace()
    return redirect(url_for('index'))


app.run(host="0.0.0.0", port="8000", debug=True)
