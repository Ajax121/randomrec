import random

class Recommender:
    """_summary_

    Args:
        list_of_movies (_type_): _description_
    """
    def __init__(self,list_of_movies):
        self.list_of_movies = list_of_movies

    def random_recommendation(self):
        return random.choice(self.list_of_movies)
        
