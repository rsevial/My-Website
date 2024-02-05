from flask import Flask, render_template, request
from mergelinkedlist import merge_sorted_lists, print_linked_list, create_linked_list
from math import pi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/profilemore')
def profilemore():
    return render_template('profilemore.html')

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

@app.route('/mergelist', methods=["GET", "POST"])
def merge():
    result_values = None
    error = None
    list1 = None
    list2 = None

    if request.method == 'POST':
        try:
            size1 = int(request.form.get('size1', 0))
            values1 = [val.strip() for val in request.form.get('values1', '').split(',')]
            if size1 != len(values1):
                raise ValueError("Size should be equal to the number of values for Linked List 1.")
            list1 = create_linked_list(size1, values1)

            size2 = int(request.form.get('size2', 0))
            values2 = [val.strip() for val in request.form.get('values2', '').split(',')]
            if size2 != len(values2):
                raise ValueError("Size should be equal to the number of values for Linked List 2.")
            list2 = create_linked_list(size2, values2)

            result_values = merge_sorted_lists(list1, list2)

        except ValueError as e:
            error = str(e)

    return render_template('mergelist.html', result_values=result_values, error=error, print_linked_list=print_linked_list, list1=list1, list2=list2)


if __name__ == "__main__":
    app.run(debug=True)

