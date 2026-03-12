#Jakub Novak
#create your playlist dictionary / name of song, length, category
songs = {
"Blinding Lights": {"artist": "The Weeknd", "length": "3:20"},
"Shape of You": {"artist": "Ed Sheeran", "length": "3:53"},
"Bad Guy": {"artist": "Billie Eilish", "length": "3:14"},
"Levitating": {"artist": "Dua Lipa", "length": "3:23"},
"Uptown Funk": {"artist": "Mark Ronson ft. Bruno Mars", "length": "4:30"},
"Rolling in the Deep": {"artist": "Adele", "length": "3:48"},
"Stay": {"artist": "The Kid LAROI & Justin Bieber", "length": "2:21"},
"As It Was": {"artist": "Harry Styles", "length": "2:47"},
"Old Town Road": {"artist": "Lil Nas X ft. Billy Ray Cyrus", "length": "2:37"},
"HUMBLE.": {"artist": "Kendrick Lamar", "length": "2:57"},
"Thinking Out Loud": {"artist": "Ed Sheeran", "length": "4:41"},
"Shake It Off": {"artist": "Taylor Swift", "length": "3:39"},
"Sunflower": {"artist": "Post Malone & Swae Lee", "length": "2:38"},
"Closer": {"artist": "The Chainsmokers ft. Halsey", "length": "4:04"},
"Counting Stars": {"artist": "OneRepublic", "length": "4:17"},
"Someone Like You": {"artist": "Adele", "length": "4:45"},
"Roar": {"artist": "Katy Perry", "length": "3:43"},
"Firework": {"artist": "Katy Perry", "length": "3:48"},
"Royals": {"artist": "Lorde", "length": "3:10"},
"Radioactive": {"artist": "Imagine Dragons", "length": "3:06"},
"Believer": {"artist": "Imagine Dragons", "length": "3:24"},
"Thunder": {"artist": "Imagine Dragons", "length": "3:07"},
"Demons": {"artist": "Imagine Dragons", "length": "2:57"},
"Love Yourself": {"artist": "Justin Bieber", "length": "3:53"},
"Sorry": {"artist": "Justin Bieber", "length": "3:20"},
"Peaches": {"artist": "Justin Bieber ft. Daniel Caesar & Giveon", "length": "3:18"},
"Watermelon Sugar": {"artist": "Harry Styles", "length": "2:54"},
"Adore You": {"artist": "Harry Styles", "length": "3:27"},
"Drivers License": {"artist": "Olivia Rodrigo", "length": "4:02"},
"Good 4 U": {"artist": "Olivia Rodrigo", "length": "2:58"},
"Vampire": {"artist": "Olivia Rodrigo", "length": "3:40"},
"Anti-Hero": {"artist": "Taylor Swift", "length": "3:21"},
"Blank Space": {"artist": "Taylor Swift", "length": "3:51"},
"Style": {"artist": "Taylor Swift", "length": "3:51"},
"Lose Yourself": {"artist": "Eminem", "length": "5:26"},
"Without Me": {"artist": "Eminem", "length": "4:50"},
"Rap God": {"artist": "Eminem", "length": "6:04"},
"God's Plan": {"artist": "Drake", "length": "3:18"},
"Hotline Bling": {"artist": "Drake", "length": "4:27"},
"One Dance": {"artist": "Drake", "length": "2:54"},
"Sicko Mode": {"artist": "Travis Scott", "length": "5:12"},
"Goosebumps": {"artist": "Travis Scott", "length": "4:03"},
"Industry Baby": {"artist": "Lil Nas X & Jack Harlow", "length": "3:32"},
"Montero": {"artist": "Lil Nas X", "length": "2:17"},
"Heat Waves": {"artist": "Glass Animals", "length": "3:58"},
"Take Me to Church": {"artist": "Hozier", "length": "4:02"},
"Pompeii": {"artist": "Bastille", "length": "3:34"},
"Feel It Still": {"artist": "Portugal. The Man", "length": "2:43"},
"Riptide": {"artist": "Vance Joy", "length": "3:24"},
"Budapest": {"artist": "George Ezra", "length": "3:20"},
"Shotgun": {"artist": "George Ezra", "length": "3:21"},
"Happy": {"artist": "Pharrell Williams", "length": "3:53"},
"Get Lucky": {"artist": "Daft Punk ft. Pharrell Williams", "length": "4:08"},
"Can't Stop the Feeling": {"artist": "Justin Timberlake", "length": "3:56"},
"Cry Me a River": {"artist": "Justin Timberlake", "length": "4:48"},
"Seven Nation Army": {"artist": "The White Stripes", "length": "3:52"},
"Mr. Brightside": {"artist": "The Killers", "length": "3:43"},
"Somebody Told Me": {"artist": "The Killers", "length": "3:17"},
"Yellow": {"artist": "Coldplay", "length": "4:29"},
"Fix You": {"artist": "Coldplay", "length": "4:55"},
"Viva La Vida": {"artist": "Coldplay", "length": "4:02"},
"Adventure of a Lifetime": {"artist": "Coldplay", "length": "4:23"},
"Numb": {"artist": "Linkin Park", "length": "3:07"},
"In the End": {"artist": "Linkin Park", "length": "3:36"},
"Breaking the Habit": {"artist": "Linkin Park", "length": "3:16"},
"Smells Like Teen Spirit": {"artist": "Nirvana", "length": "5:01"},
"Come As You Are": {"artist": "Nirvana", "length": "3:39"},
"Bohemian Rhapsody": {"artist": "Queen", "length": "5:55"},
"Don't Stop Me Now": {"artist": "Queen", "length": "3:29"},
"Another One Bites the Dust": {"artist": "Queen", "length": "3:35"},
"Billie Jean": {"artist": "Michael Jackson", "length": "4:54"},
"Beat It": {"artist": "Michael Jackson", "length": "4:18"},
"Thriller": {"artist": "Michael Jackson", "length": "5:57"},
"Take On Me": {"artist": "a-ha", "length": "3:46"},
"Africa": {"artist": "Toto", "length": "4:55"},
"Sweet Child O' Mine": {"artist": "Guns N' Roses", "length": "5:56"},
"November Rain": {"artist": "Guns N' Roses", "length": "8:57"},
"Hotel California": {"artist": "Eagles", "length": "6:30"},
"Stairway to Heaven": {"artist": "Led Zeppelin", "length": "8:02"},
"Imagine": {"artist": "John Lennon", "length": "3:03"},
"Hey Jude": {"artist": "The Beatles", "length": "7:11"},
"Let It Be": {"artist": "The Beatles", "length": "4:03"},
"Here Comes the Sun": {"artist": "The Beatles", "length": "3:06"},
"Yesterday": {"artist": "The Beatles", "length": "2:05"},
"I Wanna Dance with Somebody": {"artist": "Whitney Houston", "length": "4:52"},
"My Heart Will Go On": {"artist": "Celine Dion", "length": "4:40"},
"Rolling in the Deep (Live)": {"artist": "Adele", "length": "4:10"},
"Chandelier": {"artist": "Sia", "length": "3:36"},
"Elastic Heart": {"artist": "Sia", "length": "4:17"},
"Titanium": {"artist": "David Guetta ft. Sia", "length": "4:05"},
"Wake Me Up": {"artist": "Avicii", "length": "4:09"},
"Levels": {"artist": "Avicii", "length": "3:18"},
"The Nights": {"artist": "Avicii", "length": "2:56"},
"Animals": {"artist": "Martin Garrix", "length": "5:03"},
"Scared to Be Lonely": {"artist": "Martin Garrix & Dua Lipa", "length": "3:41"},
"Don't You Worry Child": {"artist": "Swedish House Mafia", "length": "3:32"},
"Lean On": {"artist": "Major Lazer & DJ Snake", "length": "2:56"},
"Faded": {"artist": "Alan Walker", "length": "3:32"},
"Alone": {"artist": "Alan Walker", "length": "2:42"},
"Spectre": {"artist": "Alan Walker", "length": "3:12"}
}
#function to add songs to playlist
#add a song to the playlist
def addSong():
    name = input("Enter song name: ")
    artist = input("Enter artist: ")
    length = input("Enter length: ")
    songs[name] = {"artist": artist, "length": length}


#delete a song from the playlist
def deleteSong():
    name = input("Enter song name to delete: ")
    if name in songs:
        del songs[name]
        print(f"{name} has been deleted from your playlist.")
    else:
        print(f"{name} is not in your playlist.")

#search for a song in the playlist
def searchSong():
    name = input("Enter song name to search: ")
    if name in songs:
        print(f"{name} is in your playlist.")
    else:
        print(f"{name} is not in your playlist.")
#modify a song in the playlist
def modifySong():
    name = input("Enter song name to modify: ")
    if name in songs:
        artist = input("Enter new artist: ")
        length = input("Enter new length: ")
        songs[name] = {"artist": artist, "length": length}
        print(f"{name} has been modified.")
    else:
        print(f"{name} is not in your playlist.")
flag = True
#menu
while flag == True:
    print("----Playlist Menu----")
    print("----Make a selection----")
    print("1. Add a song")
    print("2. Delete a song")
    print("3. Search for a song")
    print("4. View playlist")
    print("5. Modify a song")
    print("6. Exit")
    selection = input("What would you like to do? Select a number: ")

    #by typing 1, you can add a song
    if selection == "1":
        addSong()
    #by typing 2, you can delete a song
    elif selection == "2":
        deleteSong()
    #by typing 3, you can search for a song
    elif selection == "3":
        searchSong()
    #by typing 4, you can view the playlist
    elif selection == "4":
        for song, details in songs.items():
            print(f"{song} - Artist: {details['artist']}, Length: {details['length']}")
    #by typing 5, you can modify a song
    elif selection == "5":
        modifySong()
    #by typing 6, it will print goodbye and end the program
    elif selection == "6":
        flag = False
        print("Goodbye!")
        break