def Query(skin_type, rating, price):
    if price == '25-to-70':
        query = f'''select * from {skin_type} 
            where (rating >= {rating}) 
            and (max_amount between {price.split('-to-', 1)[0]} 
            and {price.split('-to-',1)[1]});'''
    elif price == '70':
        query = f'''select * from {skin_type}
                where (rating >= {rating})
                and max_amount >= 70;'''
    elif price == '25':
        query = f'''select * from {skin_type}
                where (rating >= {rating})
                and max_amount <= 25;'''
    return query