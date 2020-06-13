from flask import Flask, render_template, url_for, request, redirect, g
import requests
import get_info

def Query(skin_type, rating, price):
    if price == '25-to-70':
        query = 'select * from ' + skin_type + ' where (rating >= ' + rating + ')' +' and (max_amount between ' + price.split('-to-', 1)[0] + ' and ' + price.split('-to-',1)[1] + ');'
    elif price == '70':
        query = 'select * from ' + skin_type + ' where (rating >= ' + rating + ')' +' and max_amount >= 70;'
    elif price == '25':
        query = 'select * from ' + skin_type + ' where (rating >= ' + rating + ')' +' and max_amount <= 25;'

    info = get_info.get_info(query)

    return info

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    Warning= " "
    if request.method == "POST":

        skin_type = request.form.getlist("skin_type")
        rating = request.form.getlist("Rating")
        price = request.form.getlist("Price")
        
        if max(len(skin_type), len(rating), len(price)) != 1:
            Warning="Please enter 1 Parameter Only"
            return render_template('index.html', Warning=Warning)
        
        user_input = {'skin-type': skin_type[0], 'rating': rating[0], 'price': price[0]}
        '''skin_type = skin_type[0]
        rating = rating[0]
        price = price[0]'''

        # covers cases when user entered more than one requirements for each category
        
        try:
            #(url_for('result', skin_type=skin_type, rating=rating, price=price))
            print(url_for('result', user_input=user_input))
            return redirect(url_for('result', user_input=user_input))

        except UnboundLocalError:
            # covers cases when user did not check all the requirements
            Warning = 'You must enter all parameters!'

    return render_template('index.html', Warning=Warning)


@app.route('/Result', methods=['POST', 'GET'])

def result():
    print(requests.get(url_for('result', user_input)))
    info = requests.get('result')
    print(info.json())

    return render_template('result.html', Brand=info[0], Product=info[1],  Rating=info[2], Price=info[3])



if __name__ == "__main__":
    app.run(debug=True)

