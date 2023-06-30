def movie_organizer(*args):
    dict_movies = {}
    for el in args:
        movie_name = el[0]
        genre = el[1]
        if genre not in dict_movies:
            dict_movies[genre] = [0], []
        dict_movies[genre][0][0] += 1
        dict_movies[genre][1].append(movie_name)

    for k, v in dict_movies.items():
        dict_movies[k] = ''.join([str(x) for x in v[0]]), ', '.join(v[1])

    sorted_output = sorted(dict_movies.items(), key=lambda kvpt: (-int(kvpt[1][0]), kvpt[0]))

    info_for_exit = ""

    for item in sorted_output:
        genre_sorted = item[0]
        count = item[1][0]
        info_for_exit += f"{genre_sorted} - {''.join([str(x) for x in count])}" + '\n'
        ll = []
        splited = item[1][1].split(", ")
        for ite in sorted(splited):
            info_for_exit += "* " + f'{ite}' + '\n'
    return info_for_exit


# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
