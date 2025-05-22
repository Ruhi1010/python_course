#8.7
def make_album(artist, title, num_songs=None):
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

album_1 = make_album("The Beatles", "Abbey Road")
album_2 = make_album("Adele", "25", 11)
album_3 = make_album("Pink Floyd", "The Dark Side of the Moon", 10)

print(album_1)
print(album_2)
print(album_3)



