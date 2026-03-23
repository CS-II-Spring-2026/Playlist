#Riley Cooper


#Create your playlist dictonary / name of song, length, category

#functions
#add a song
#def addSong():
#delete a song
#search for a song
#extenion - add to favorites list

# add
# search
# delete 
# update
# show all songs
# add to favs (ext)
# remove from favs (ext)
# show favs (ext)
# quit

#All the songs in the playlist with their details (artist, length, genre)
song_list = {
    "Blinding Lights": {"Artist": "The Weeknd", "Length": "3:20", "Genre": "Pop"},
    "Lose Yourself": {"Artist": "Eminem", "Length": "5:26", "Genre": "Hip-Hop"},
    "Shape of You": {"Artist": "Ed Sheeran", "Length": "3:53", "Genre": "Pop"},
    "Smells Like Teen Spirit": {"Artist": "Nirvana", "Length": "5:01", "Genre": "Rock"},
    "Bad Guy": {"Artist": "Billie Eilish", "Length": "3:14", "Genre": "Alternative Pop"},
    "Uptown Funk": {"Artist": "Mark Ronson ft. Bruno Mars", "Length": "4:30", "Genre": "Funk/Pop"},
    "Levitating": {"Artist": "Dua Lipa", "Length": "3:23", "Genre": "Dance Pop"},
    "Old Town Road": {"Artist": "Lil Nas X", "Length": "2:37", "Genre": "Country Rap"},
    "Bohemian Rhapsody": {"Artist": "Queen", "Length": "5:55", "Genre": "Classic Rock"},
    "HUMBLE.": {"Artist": "Kendrick Lamar", "Length": "2:57", "Genre": "Hip-Hop"}
}
#Favorites list - starts empty, user can add songs from the main playlist to this list
fav_list = {}
    
#Adds a song to the playlist with user input for the song name, artist, length, and genre
def addSong():
    song_name = input("Enter the name of the song you want to add: ")
    artist = input("Enter the artist of the song: ")
    length = input("Enter the length of the song (mm:ss): ")
    genre = input("Enter the genre of the song: ")
    song_list[song_name] = {"Artist": artist, "Length": length, "Genre": genre}
    print(f"{song_name} by {artist} has been added to the playlist.")


#Searches for a song and gives details about the song
def searchSong():
    target = input("Enter the name of the song you want to search for: ")

    def searchFunction(name, song_list):
        if name in song_list:
            return song_list[name]
        else:
            return "Song not found."
    results = searchFunction(target, song_list)
    if results:
        for key, info in song_list.items():
            if song_list[key] == results:
                print(f"{key} by {info['Artist']}  Length: {info['Length']} Genre: {info['Genre']}")
    else:        print("Song not found.")


#Deletes a song 
def deleteSong():
    delete_name = input("Enter the name of the song you want to delete: ")
    if delete_name in song_list:
        del song_list[delete_name]
        print(f"{delete_name} has been deleted from the playlist.")
    else:
        print(f"{delete_name} was not found in the playlist.")


#Update a song - change the artist, length, genre
def updateSong():
    update_song = input("Enter the name of the song you want to update: ")
    if update_song in song_list:
        new_artist = input("Enter the new artist of the song: ")
        new_length = input("Enter the new length of the song (mm:ss): ")
        new_genre = input("Enter the new genre of the song: ")
        song_list[update_song] = {"Artist": new_artist, "Length": new_length, "Genre": new_genre}
        print(f"{update_song} has been updated in the playlist.")
    else:
        print(f"{update_song} was not found in the playlist.")


#Show all songs in the playlist
def showSongs():
    for key, info in song_list.items():
        print(f"{key} by {info['Artist']} - Length: {info['Length']}, Genre: {info['Genre']}")


#Add a song to the favorites list
def addFavs():
    fav_song = input("Enter the name of the song you want to add to favorites: ")
    if fav_song in song_list:
        if fav_song not in fav_list:
            fav_list[fav_song] = song_list[fav_song]
            print(f"{fav_song} has been added to your favorites.")
        else:
            print(f"{fav_song} is already in your favorites.")


#Remove a song from the favorites list
def removeFavs():
    fav_song = input("Enter the name of the song you want to remove from favorites: ")
    if fav_song in fav_list:
        del fav_list[fav_song]
        print(f"{fav_song} has been removed from your favorites.")
    else:
        print(f"{fav_song} is not in your favorites.")


#Show the songs in the favorites list
def showFavs():
    if fav_list:
        for key, info in fav_list.items():
            print(f"{key} by {info['Artist']} - Length: {info['Length']}, Genre: {info['Genre']}")
    else:
        print("Your favorites list is empty.")


#menu (Reprints each time until the user quits)
flag = True
while flag == True:
    print("----Playlist Menu----")
    print("----Make a selection----")
    print("1. Add a song")
    print("2. Search for a song")
    print("3. Delete a song")
    print("4. Update a song")
    print("5. Show all songs")
    print("6. Add to favorites")
    print("7. Remove from favorites")
    print("8. Show favorites")
    print("9. Quit")
    selection = input("Enter your selection: ")

    #Selections and what they go to
    if selection == "1":
        addSong()       #Starts on line 36
    elif selection == "2":
        searchSong()    #Starts on line 46
    elif selection == "3":
        deleteSong()    #Starts on line 63
    elif selection == "4":
        updateSong()    #Starts on line 73
    elif selection == "5":
        showSongs()     #Starts on line 86
    elif selection == "6":
        addFavs()       #Starts on line 96
    elif selection == "7":
        removeFavs()    #Starts on line 103
    elif selection == "8":
        showFavs()      #Starts on line 113
    elif selection == "9":
        flag = False
        print("Goodbye!")

