from flask import Flask, render_template, url_for, request, redirect, after_this_request
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

    return render_template('result.html', length=len(info[0]), Brand=info[0], Product=info[1], Price=info[2], Rating=info[3])



if __name__ == "__main__":
    app.run(debug=True)

