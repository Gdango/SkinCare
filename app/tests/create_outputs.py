Skin_type = ["Combination", "Dry", "Oily"]
Rating = [2, 3, 4]
Price = ['25', '25-to-75', '70']

query = f'''select * from {skin_type}
    where (rating >= {rating})
    and (max_amount between {price.split('-to-', 1)[0]}
    and {price.split('-to-', 1)[1]});'''

