import media
import fresh_tomatos

# each movie title instantiates the Movie class
braveheart = media.Movie("Braveheart",
                         "W. Wallace leads the Scots in war \
                            against the English.",
                         "2 hours 58 minutes",
                         "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=wj0I8xVTV18",
                         media.Movie.VALID_RATINGS[3],
                         ["Mel Gibson", "Sophie Marceau", "Patrick McGoohan"],
                         "05/24/1995",
                         [media.Movie.VALID_CATEGORIES[2],
                             media.Movie.VALID_CATEGORIES[6],
                             media.Movie.VALID_CATEGORIES[9],
                             media.Movie.VALID_CATEGORIES[13]])

highlander = media.Movie("Highlander",
                         "An epic battle until there is only \
                            one highlander left.",
                         "1 hours 56 minutes",
                         "http://img.soundtrackcollector.com/movie/large/Highlander_Alternate_Movie_Poster.jpg",
                         "https://www.youtube.com/watch?v=omOZyLmNMJs",
                         media.Movie.VALID_RATINGS[3],
                         ["Christopher Lambert",
                             "Sean Connery",
                             "Clancy Brown"],
                         "03/7/1986",
                         [media.Movie.VALID_CATEGORIES[0],
                             media.Movie.VALID_CATEGORIES[1],
                             media.Movie.VALID_CATEGORIES[8]])


boondock_saints = media.Movie("The Boondock Saints",
                              "Two Irish brothers set out to cleanse \
                                Boston of evil men.",
                              "1 hours 48 minutes",
                              "http://images.channeladvisor.com/Sell/SSProfiles/73000107/Images/17/The-Boondock-Saints-Poster-472.jpg",
                              "https://www.youtube.com/watch?v=ydXojYfCF3I",
                              media.Movie.VALID_RATINGS[3],
                              ["Willem Dafoe",
                                  "Sean Patrick Flanery",
                                  "Norman Reedus"],
                              "11/19/1999",
                              [media.Movie.VALID_CATEGORIES[0],
                                  media.Movie.VALID_CATEGORIES[4],
                                  media.Movie.VALID_CATEGORIES[12]])

apollo_thirteen = media.Movie("Apollo 13",
                              "Moon mission gone terribly wrong.",
                              "2 hours 20 minutes",
                              "http://4.bp.blogspot.com/_GIchwvJ-aNk/SlflD2y7UEI/AAAAAAAAJEM/vRYtCQrBP-w/s800/Apollo+13+movie+poster.jpg",
                              "https://www.youtube.com/watch?time_continue=2&v=KtEIMC58sZo",
                              media.Movie.VALID_RATINGS[1],
                              ["Tom Hanks", "Bill Paxton", "Kevin Bacon"],
                              "06/15/1995",
                              [media.Movie.VALID_CATEGORIES[1],
                                  media.Movie.VALID_CATEGORIES[6],
                                  media.Movie.VALID_CATEGORIES[9]])

elf = media.Movie("Elf",
                  "A human raised by elves travels to NYC to find his \
                    biological father.",
                  "1 hours 37 minutes",
                  "http://t3.gstatic.com/images?q=tbn:ANd9GcSt4AaH8aQNb6hrdHev-0J_xymlsy3aQDxGLXVDmU812etMBFRN",
                  "https://www.youtube.com/watch?v=gW9wRNqQ_P8",
                  media.Movie.VALID_RATINGS[1],
                  ["Will Farrell", "James Caan", "Bob Newhart"],
                  "11/7/2003",
                  [media.Movie.VALID_CATEGORIES[3],
                      media.Movie.VALID_CATEGORIES[7],
                      media.Movie.VALID_CATEGORIES[8],
                      media.Movie.VALID_CATEGORIES[11]])

forrest_gump = media.Movie("Forrest Gump",
                           "A man narrates his life.",
                           "2 hours 22 minutes",
                           "https://images-na.ssl-images-amazon.com/images/I/41sc8hx7VaL.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg",
                           media.Movie.VALID_RATINGS[2],
                           ["Tom Hanks"],
                           "07/6/1994",
                           [media.Movie.VALID_CATEGORIES[3],
                               media.Movie.VALID_CATEGORIES[6]])

# places the movies into an array
movies = [braveheart, highlander, boondock_saints,
          apollo_thirteen, elf, forrest_gump]

# displays the Movie Trailer website
fresh_tomatos.open_movies_page(movies)
