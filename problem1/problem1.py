#from urllib.parse import urlencode, quote_plus
import requests
import pandas as pd
from bs4 import BeautifulSoup
import bs4
import json

key = 'f6f6d3ca2bfad2b49f0e64e0bc14fa5a'
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=" + key
parameter = {"directorNm": "봉준호"}
req = requests.get(url, parameter)

html= req.json()
html
DF = pd.DataFrame(html['movieListResult']["movieList"])

DF = DF.sort_values("prdtYear")


DF['directors'] = DF['directors'].apply(lambda x : x[0]['peopleNm'])
DF['companys'] = DF['companys'].apply(lambda x : x[0]['companyNm'] if x else x)

DF
