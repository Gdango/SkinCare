
from flask import Flask, render_template, url_for, request, redirect, flash
import get_info
import Query

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    Warning = ""

    if request.method == "POST":

        skin_type = request.form.getlist("skin_type")
        rating = request.form.getlist("Rating")
        price = request.form.getlist("Price") 
        print(skin_type, rating, price)
        try:
            # covers cases when user entered more than one requirements for each category
                user_input = {'skin-type': skin_type[0], 'rating': rating[0], 'price': price[0]}
                return redirect(url_for('result', user_input=user_input))
        except IndexError:
            # covers cases when user did not check all the requirements
            Warning = 'You must enter all parameters!'

    return render_template('index.html', Warning=Warning)

@app.route('/Result', methods=['POST', 'GET'])

def result():

    user_input = request.args.get('user_input', type=str)

    dict_user_input = eval(user_input)

    query = Query.Query(dict_user_input['skin-type'], dict_user_input['rating'], dict_user_input['price'], 'brand ASC')
    info = get_info.get_info(query)
    return render_template('result.html', length=len(info[0]), Brand=info[0], Product=info[1],  Price=info[3], Rating=info[2])

@app.route('/SortResult', methods=['POST', 'GET'])

def sortresult():
    info = request.args.get('info', type=str)

    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)

