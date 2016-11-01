class Movie():
    """This class creates the basic framework for particular instances
        of your favorite movies and their respective attributes

        Attributes:
        title (str): Provide the title of the movie with appropriate
                     capitalization
        storyline (str): Provide a brief synopsis of the movie
        poster_image_url (str): Provide a url link to the poster image
        trailer_youtube_url (str): Provide a url link to the trailer on YouTube
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
