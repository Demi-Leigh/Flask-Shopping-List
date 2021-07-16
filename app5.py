from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def cart():
    return render_template('shopping_list.html')


@app.route('/showitems', methods=['POST', 'GET'])
def products():
    if request.method == 'POST':
        items = request.form
        return render_template('show_items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
