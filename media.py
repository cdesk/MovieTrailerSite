import webbrowser


class Video():
    """This class is a parent class to store information that is applicable
        to all video types."""

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """This class provides a way to store movie related information."""

    # Movie Rating which are valid to set a movie to.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Categories which can be set for a specific movie.
    VALID_CATEGORIES = ["Action", "Adventure", "Biography", "Comedy",
                        "Crime", "Documentary", "Drama", "Family",
                        "Fantasy", "History", "Horror", "Romance",
                        "Thriller", "War"]

    # The method called with a new Movie is instantiated
    def __init__(self, movie_title, movie_storyline,
                 duration, poster_image, trailer_youtube,
                 rating, stars, release_date, categories):

        divider = " | "

        Video.__init__(self, movie_title, duration)

        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.stars = divider.join(stars)
        self.release_date = release_date
        self.category = divider.join(categories)

    # Opens the trailer when a movie is selected
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
