from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template('page/docs.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')