import requests
import os
from dotenv import load_dotenv

#This line is for loading the API Key from .env file 
load_dotenv()
API_KEY=os.getenv("TMDB_API_KEY")


#Connecting to TMDB API
url= f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}"
response = requests.get(url)
data = response.json()
# print(data)
#Printing Top 10 moives that are trending
movies = data["results"][:10]

for i, movie in enumerate(movies,1):
    print(f"{i}. {movie['title']} | Rating: {movie['vote_average']}")