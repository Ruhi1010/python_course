#8.7
def make_album(artist, title, num_songs=None):
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

album_1 = make_album("Arijit Singh", "Tum Hi Ho")
album_3 = make_album("Shreya Ghoshal", "Aashiqui 2", 10)

print(album_1)
print(album_2)
print(album_3)



