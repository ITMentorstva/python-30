
import numpy as np
import matplotlib.pyplot as plt

# 5 - neko je dao 5 zvezdica za neki film
# 0 - neko nije dao nijednu zvezdicu za film

ratings = np.array([
    [5,4,0,0,3], # 0 - Toma
    [3,2,0,3,1], # 1 - Petar
    [5,1,3,3,2], # 2 - Marko
])

#        toma=0   Petar=1   Marko=2
users = ['Toma', 'Petar', 'Marko']

#           0           1           2           3                  4
movies = ['LOTR', 'Harry Potter', 'Titanic', 'Fast & Furious', 'Batman']

movie_ratings_sum = np.sum(ratings, axis=0)

most_liked_movie_index = np.argmax(movie_ratings_sum) # [13, 7, ...]


print(f"Movie with most views {movies[most_liked_movie_index]}, it's rating is: {movie_ratings_sum[most_liked_movie_index]} ")

plt.pie(movie_ratings_sum, labels=movies, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors) # 35.0%
# plt.show()


ratings_monthly = np.array([
    [5, 3, 2, 1, 1],  # January
    [2, 3, 1, 0, 4],  # February
    [3, 2, 4, 1, 0],  # March
    [4, 4, 3, 2, 1],  # April
    [1, 2, 2, 3, 4],  # May
    [0, 1, 3, 4, 2],  # June
    [5, 5, 4, 3, 2],  # July
    [3, 2, 1, 0, 4],  # August
    [2, 3, 4, 1, 0],  # September
    [4, 3, 2, 1, 5],  # October
    [1, 0, 2, 3, 4],  # November
    [3, 4, 1, 2, 0],  # December
])

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

plt.figure(figsize=(15, 6))

for i, movie in enumerate(movies):
    movie_ratings = ratings_monthly[:, i] # [0,0], [1,0], [2,0]....[9,0] === [0, 1], [1,1], [2,1]...
    plt.plot(months, movie_ratings, marker='o', label=movie)

plt.title("Movie ratings over the year")
plt.xlabel('Month')
plt.ylabel('Ratings')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()