# Movie Trailer Website

## Overview

**Project**: Movie Trailer Website using Python

**Nanodegree**: Full Stack Developer

**Purpose**: The site displays a list of movies with applicable information. When a movie is selected its trailer will play.

The website consists of three python (py) files:
- media.py
- entertainment_center.py
- fresh_tomatos.py


## Running the Website
To run the website open and run the **entertainment_center.py** file
## Adding or Editing a Movie's information
To **add** a movie, a new instance of the **Movie** class must me instantiated in the
**entertainment_center.py** file.

To **edit** information of a movie, modify the necessary argument(s) in the desired instance. Below is a sample snippet of a movie:

```
braveheart = media.Movie("Braveheart",
             "W. Wallace led the Scots in war against the English.",
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
```
Arguments of a movie must be passed in a certain order and type as seen in the following list:
- Movie Title
- Movie Storyline: Storyline of the movie
- Movie Duration: Length of the movie..
- Movie Poster: A URL of the movie's poster.
- Movie Rating: Specified by an array item from the **_media.Movie.VALID_RATINGS_** array.
- Movie Stars: A string array of star names. Even if there is one star it should be a string array.
- Movie Release Date: The date the movie was released.
- Movie Categories: An array of the **_media.Movie.VALID_CATEGORIES_** array to specify the movies categories.

After the movie is instantiated, it must be added to the **movies** array in **enteratinment_center.py**

## Movie Class Variables
**File**: media.py
Class **Movie** is a child class of **Video**. Below are the variables the **Movie** class accpets.

- movie_title (instantiated in Video)
- duration (instantiated in Video)
- storyline
- poster_image_url
- trailer_youtube_url
- rating
- stars
- release
- category

## Video Class Variables
**File**: media.py
The **Video** class is the parent class of *Movie** which assigns the _title_ and _duration_ of a video.
- title
- duration

## Contributions
If you have comments/suggestions/questions please contact jadeskins3@gmail.com.


