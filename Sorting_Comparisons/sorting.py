class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

def sort_movies_by_year(movies):
    return sorted(movies, key=lambda movie: movie.year, reverse=True)

def remove_common_prefix(title):
    prefixes = ["A ", "An ", "The "]
    for prefix in prefixes:
        if title.startswith(prefix):
            return title[len(prefix):]
    return title

def sort_movies_alphabetically(movies):
    return sorted(movies, key=lambda movie: remove_common_prefix(movie.title).lower())

