from flask import Flask, render_template, url_for, request, redirect, after_this_request
import get_info

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    Warning= None
    if request.method == "POST":

        skin_type = request.form.get("skin_type")
        rating = request.form.get("Rating")
        price = request.form.get("Price")
        # covers cases when user did not check all the requirements
        # covers cases when user entered more than one requirements for each category
        

        # Combination, Oily, Dry
        # 4 Stars & Up
        # 3 Stars & Up
        # 2 Stars & Up
        '''Price: 
        $70 & Above
        $25 & Above
        $25 & Below '''
        try:
            if price == '25-to-70':
                query = 'select * from ' + skin_type + ' where (rating >= ' + rating + ')' +' and (max_amount between ' + price.split('-to-', 1)[0] + ' and ' + price.split('-to-',1)[1] + ');'
            elif price == '70':
                query = 'select * from ' + skin_type + ' where (rating >= ' + rating + ')' +' and max_amount >= 70;'
            elif price == '25':
                query = 'select * from ' + skin_type + ' where (rating >= ' + rating + ')' +' and max_amount <= 25;'
            global info
            info = get_info.get_info(query)
            return redirect(url_for('result'))


        except:
            Warning = 'You must enter all parameters!'

    return render_template('index.html', Warning=Warning)


@app.route('/Result', methods=['POST', 'GET'])

def result():

    return render_template('result.html', length=len(info[0]), Brand=info[0], Product=info[1],  Rating=info[2], Price=info[3])



if __name__ == "__main__":
    app.run(debug=True)

