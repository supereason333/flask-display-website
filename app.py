from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/process', methods=['POST'])
def process():
    return ''

@app.route('/testing', methods=['GET', 'POST'])
def testing():
    return render_template('testing.html', randomNum = random.randint(1, 10))

# gallary pages

@app.route('/gallery/photography')
def photography():
    return render_template('gallery/photography.html')

@app.route('/gallery/traditionalart')
def traditionalart():
    return render_template('gallery/traditionalart.html')

@app.route('/gallery/digitalart')
def digitalart():
    return render_template('gallery/digitalart.html')

if __name__ == '__main__':
    app.run(debug=True)