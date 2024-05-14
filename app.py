from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/proyects')
def proyects():
    return render_template('proyects.html')

if __name__ == '__main__':
    app.run(debug=True)