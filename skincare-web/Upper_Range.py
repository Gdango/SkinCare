query = f'''select * from {skin_type} 
        where (rating >= {rating}) 
        and (max_amount between {price.split('-to-', 1)[0]} 
        and {price.split('-to-',1)[1]})'''