from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == "POST":
        skin_type = request.form.get("skin_type")
        rating = request.form.get("Rating")
        price = request.form.get("Price")

        print(skin_type, rating, price)
    return render_template('index.html')

@app.route('/Result', methods=['POST', 'GET'])

def result():
    return render_template('result.html')



if __name__ == "__main__":
    app.run(debug=True)