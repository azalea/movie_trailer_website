import webbrowser

class Movie():
    def __init__(self, title, storyline, poster, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_url
    def show_trailer(self):
        webbrowser.open(self.trailer_url)

        
        
