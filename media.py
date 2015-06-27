import webbrowser

class Movie():
    '''
    A class for movie objects.
    title: movie title
    storyline: brief plot of the movie
    poster_image_url: the url of the movie's poster image
    trailer_youtube_url: the url of the movie's trailer on YouTube
    '''
    def __init__(self, title, storyline, poster, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_url
    def show_trailer(self):
        '''
        Open the movie trailer webpage in web browser.
        '''
        webbrowser.open(self.trailer_url)

        
        
