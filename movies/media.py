""" allows access to webbrowser function in python library"""
import webbrowser

"""defines movie class and data structure"""
class Movie():
    def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

"""calls python webbrower function to open movie trailer in web browser"""
    def show_trailer (self):
        webbrowser.open(self.trailer_youtube_url)
