import webbrowser
__author__ = 'Ibrahim.Abdallah'


class Movie():
    """this class provide movie trailer instances
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # method to show trailer of the selected movie

    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
