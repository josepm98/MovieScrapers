import re
import requests
import json
from bs4 import BeautifulSoup


class PutLockerScraper:

    print()
    print("Let's find a movie/show!")
    print("If a link doesn' work try anotherone")
    print()

    movie = input("Movie/Show: ").lower()
    # season = input("Season: ")
    # episode = input("Episode: ")

    print("------------------")
    print("-- putlocker.kz --")
    print("------------------")

    # Required variable for the search request
    url = "https://putlocker.kz/search?keyword=" + movie  # url de la petición post
    getPostsURL = "https://putlocker.kz/get-links/" # url para obtener los links

    # Search request
    searchResults = requests.post(url).content
    soup = BeautifulSoup(searchResults, "html.parser")

    # We search for the link of the first result
    # This is not the best way I'll change it later so it finds the exact show/movie
    srcMovie = soup.find("a", attrs={"class": "ml-mask"})["href"]

    # We get the HTML of the movie/show
    page = requests.get(srcMovie)

    # We search for the variables to make a post request to putlocker's server
    # They store two variables in a script that are later used to make a request to get the links
    soup = BeautifulSoup(page.content, "html.parser")
    scripts = str(soup.find_all("script"))

    # We search for the variable id on the script
    movie_id = re.compile("var id = (.*?);")
    search = movie_id.search(scripts)
    # We get the first result(since there's only one) and remove the quotation marks
    movie_id = str(search.groups()[0].replace("'", ""))

    # Repeat the same step with variable e
    e = re.compile("var e = (.*?);")
    search = e.search(scripts)
    e = str(search.groups()[0].replace("'", ""))

    # Required parameters for the request
    body = {"id": movie_id, "e": e}
    enlaces = requests.post(getPostsURL, data=body).content  # .replace("[", "").replace("]", "")

    enlaces = json.loads(enlaces)
    for enlace in enlaces:
        print(enlace['src'])
