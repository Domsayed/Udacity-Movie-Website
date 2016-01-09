Project: Movie Trailer Website  - [Ibrahim Abdallah]
================================

this application generates HTML web page that contain a movie trailer website with short storyline
where users can see the first six movies in the imdb website top 250 rated movie.

    http://www.imdb.com/chart/top	Top 250 as voted by IMDb Users

the number of movies can be changed and also a user interaction can be added to determine the number of movies of choice.

The Zip folder contain following fles,
--------------------------------------
1 - movie_website.py
    it contains the instances of Movie Class and imdb code.
2 - media.py
    it contains the Movie Class.
3 - fresh_tomatoes.py
    it generates the HTML document and it is provided by Udacity.
4 - fresh_tomatoes.html
    this is the generated HTML file where you can watch the movie trailers.
5 - README.txt

Required Libraries and Dependencies
-----------------------------------
The application requires Python 3.5.0 be installed
The imdbpie library is used in the application
    https://pypi.python.org/pypi/imdbpie

Installation of imdpie

To install imdbpie, simply:

pip install imdbpie

How To Use

Create an instance of ImdbPie

from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests

# Creating an instance with caching enabled
# Note that the cached responses expire every 2 hours or so.
# The API response itself dictates the expiry time)
imdb = Imdb(cache=True)
Search for a title by its title

>>> imdb.search_for_title("The Dark Knight")
[{'title': "The Dark Knight", 'year':  "2008", 'imdb_id': "tt0468569"},{'title' : "Batman Unmasked", ...}]

Find a title by its imdb_id

>>> title = imdb.get_title_by_id("tt0468569")
>>> title.title
"The Dark Knight"
>>> title.rating
8.1
>>> title.certification
"PG-13"

Find a person by their imdb_id

>>> person = imdb.get_person_by_id("nm0000151")
>>> person.name
"Morgan Freeman"
>>> person.imdb_id
"nm0000151"

Find a title trailer poster

>>> title = imdb.get_title_by_id("tt1210166")
>>> title.trailer_image_urls
["http://ia.media-imdb.com/images/M/MV5BODM1NDMxMTI3M15BMl5BanBnXkFtZTcwMDAzODY1Ng@@._V1_.jpg",...]

Find the top 250 movies

>>> imdb.top_250()
[{'title': 'The Shawshank Redemption', 'year': '1994', 'type': 'feature', 'rating': 9.3,...}, ...]


How to Run Project
------------------
1 - install imdbpie
    in cmd execute pip install imdbpie
2 - in terminal or cmd go to the directory where the files are located,
    in cmd execute python movie_website.py

Extra Credit Description
------------------------
the application has been modified :
1 - post a short storyline for each movie tile,
 <h3>{movie_title}</h3>
    <h5>{movie_storyline}</h5>

2 - edited HTML to change the background and font colours.
   body {

                padding-top: 40px;
                background-color:lightgrey;
                color: black;
                text-align: center;
        }

3 - instead of just showing my favorite movies I am getting the top rated movies from imdb website using external python library.

4 - I checked all the files againist PEP8 and all of thm passed without any errors.