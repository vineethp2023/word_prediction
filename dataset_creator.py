from bs4 import BeautifulSoup
import pandas as pd
soup = BeautifulSoup('https://www.omdbapi.com/', "html.parser")

movie_data = []
for movie_element in soup.find_all("div", class_="movie-item"):  # Replace with the correct selector
    title = movie_element.find("h3").text.strip()
    actor = movie_element.find("span", class_="actor").text.strip()  # Adjust selectors as needed
    actress = movie_element.find("span", class_="actress").text.strip()
    release_year = movie_element.find("span", class_="year").text.strip()

    movie_data.append({
        "title": title,
        "actor": actor,
        "actress": actress,
        "release_year": release_year
    })
df = pd.DataFrame(movie_data)
df.to_csv("malayalam_movies.csv", index=False)