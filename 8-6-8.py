# Task 8-6
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# Call the function with three city-country pairs
print(city_country("santiago", "chile"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))

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
