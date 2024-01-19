# Task 8-8
def user_album_input():
    while True:
        artist = input("Enter the artist's name (or 'quit' to exit): ")
        if artist.lower() == 'quit':
            break
        title = input("Enter the album title: ")
        songs_input = input("Enter the number of songs (press enter if unknown): ")
        
        if songs_input:
            songs = int(songs_input)
            album = make_album(artist, title, songs)
        else:
            album = make_album(artist, title)
        
        print(album)

# Call the function for user input
user_album_input()