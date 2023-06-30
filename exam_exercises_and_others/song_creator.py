def add_songs(*args):
    dict_songs_lyrics = {}
    for name, lyrics in args:
        if name not in dict_songs_lyrics:
            dict_songs_lyrics[name] = []
        dict_songs_lyrics[name].append(lyrics)
    output_string = ''
    for k, v in dict_songs_lyrics.items():
        output_string += f"- {k}" + '\n'

        for el in v:
            for item in el:
                if len(item) == 0:
                    item = ''
                output_string += item + '\n'
    return output_string


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
