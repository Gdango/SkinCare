from get_info import get_info
import unittest
from unittest.mock import Mock

class databaseinfo(unittest.TestCase):
    def SetUp(self):
        self.STcombo = "Combination"
        self.Stdry = "Dry"
        self.STOily = "Oily"
        self.RatingFour = 4
        self.RatingTwo = 2
        self.RatingThree = 3
        self.LowerPriceRange = '25'
        self.MediumPriceRange = '25-to-70'
        self.UpperPriceRange = '70'
        
    def test_get_info(self):
        skintypes = ["Combination", "Dry", "Oily"]
        rating = 4
        price = '25-to-70'
        for skin_type in skintypes:
            query = f'''select * from {skin_type} 
                where (rating >= {rating}) 
                and (max_amount between {price.split('-to-', 1)[0]} 
                and {price.split('-to-',1)[1]});'''
            mock_query = Mock()
            mock_query.get_info_assert_called_with(query)

if __name__ == "__main__":
    unittest.main()
