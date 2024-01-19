# Task 8-7
def make_album(artist, title, songs=None):
    album = {"artist": artist.title(), "title": title.title()}
    if songs:
        album["songs"] = songs
    return album

# Make three dictionaries representing different albums
album1 = make_album("artist1", "album1", 10)
album2 = make_album("artist2", "album2", 15)
album3 = make_album("artist3", "album3")

# Print each return value to show that the dictionaries are storing the album information correctly
print(album1)
print(album2)
print(album3)

