import re
import urllib.parse
import urllib.request
import imdbpie
import fresh_tomatoes
import media

movies = []

imdb = imdbpie.Imdb()

"""Get movie info and build the movie list
search youtube for the movie trailer and get it's URL'
create instance of Movie class
Populate movies list
Create HTML page with the movies
"""
for i in range(0, 6):
        title = imdb.get_title_by_id(imdb.top_250()[i]['tconst'])
        name = title.title
        storyline = title.plot_outline
        poster_image_url = title.poster_url
# search youtube for the movie trailer and get it's URL'
        query_string = urllib.parse.urlencode({"search_query": name})
        html_content = urllib.request.urlopen(
                        "http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\\', html_content.read().decode())
        trailer_youtube_url = "http://www.youtube.com/watch?v=" + \
                              search_results[0]
# create instance of Movie class
        movie = media.Movie(name, storyline, poster_image_url,
                            trailer_youtube_url)
# Populate movies list
        movies.append(movie)
# Create HTML page with the movies
fresh_tomatoes.open_movies_page(movies)
