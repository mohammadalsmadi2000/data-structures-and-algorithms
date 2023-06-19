from sorting import Movie, sort_movies_by_year, sort_movies_alphabetically

def test_sort_movies_by_year():
    movies = [
        Movie("The Shawshank Redemption", 1994, ["Drama"]),
        Movie("The Godfather", 1972, ["Crime", "Drama"]),
        Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    ]

    sorted_movies = sort_movies_by_year(movies)
    assert sorted_movies[0].title == "The Dark Knight"
    assert sorted_movies[1].title == "The Shawshank Redemption"
    assert sorted_movies[2].title == "Pulp Fiction"
    assert sorted_movies[3].title == "The Godfather"


def test_sort_movies_alphabetically():
    movies = [
        Movie("The Shawshank Redemption", 1994, ["Drama"]),
        Movie("The Godfather", 1972, ["Crime", "Drama"]),
        Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    ]

    sorted_movies = sort_movies_alphabetically(movies)
    assert sorted_movies[0].title == "The Dark Knight"
    assert sorted_movies[1].title == "The Godfather"
    assert sorted_movies[2].title == "Pulp Fiction"
    assert sorted_movies[3].title == "The Shawshank Redemption"


