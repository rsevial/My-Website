from flask import Flask, render_template, request
from math import pi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def areaofcircle():
    result = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        area = pi * (radius ** 2)
        result = area
    return render_template('circle.html', result=result)

@app.route('/triangle', methods=['GET', 'POST'])
def areaoftriangle():
    result = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        result = (base * height) / 2
    return render_template('triangle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
