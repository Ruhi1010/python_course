#8.8
def make_album(artist, title, num_songs=None):
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

while True:
    print("\nPlease enter album information:")
    artist = input("Artist name (or 'quit' to stop): ")
    
    if artist.lower() == 'quit':
        break
    
    title = input("Album title: ")
  
    num_songs_input = input("Number of songs (optional, press Enter to skip): ")
    num_songs = None
    if num_songs_input:
        num_songs = int(num_songs_input)
   
    album = make_album(artist, title, num_songs)
    
    print("\nAlbum created:", album)
    
    
    
