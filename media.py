#  The Movie Base Class
class Movie():
	#  Movie class stores title, year, storyline, image url and trailer url of a provided movie
    def __init__(self, movie_title, movie_year, movie_storyline, poster_image,
                 trailer_youtube):
    	#  set the Movie class variables to the input parameter
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
