from flask import Flask, render_template, url_for, request, redirect, after_this_request
from flask_table import Table, Col
import get_info

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == "POST":

        skin_type = request.form.get("skin_type")
        rating = request.form.get("Rating")
        price = request.form.get("Price")

        query = 'select * from ' + skin_type + ' where (rating >= ' + rating + ')' +' and (max_amount between ' + price.split('-to-', 1)[0] + ' and ' + price.split('-to-',1)[1] + ');'
        global info
        
        info = get_info.get_info(query)

        return redirect(url_for('result'))

    return render_template('index.html')


@app.route('/Result', methods=['POST', 'GET'])

def result():

    return render_template('result.html', info=info)



if __name__ == "__main__":
    app.run(debug=True)