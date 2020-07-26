def tracklist(**artists):
    for artist in artists:
        print(artist)
        for album in artists[artist]:
            print(f"ALBUM: {album} TRACK: {artists[artist][album]}")


# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love",
#                 "Seventeen Seconds": "A Forest"})
