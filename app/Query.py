def Query(skin_type, rating, price, order_by):
    if price == '25-to-70':
        query = f'''select * from {skin_type} 
                where (rating >= {rating}) 
                and (max_amount between {price.split('-to-', 1)[0]} 
                and {price.split('-to-',1)[1]})
                order by {order_by};'''
    elif price == '70':
        query = f'''select * from {skin_type}
                where (rating >= {rating})
                and max_amount >= 70
                order by {order_by};'''

    elif price == '25':
        query = f'''select * from {skin_type}
                where (rating >= {rating})
                and max_amount <= 25
                order by {order_by};'''
    return query