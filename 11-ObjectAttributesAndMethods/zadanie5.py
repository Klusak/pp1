class Song():
    def ___init__(self,performer,song,album,year):
        self.performer=performer
        self.song=song
        self.album=album
        self.year=year
    def __str__(self):
        return f"Performer: {self.performer}\nSong:{self.song}\nAlbum: {self.album}\nYear: {self.year}"

song1=Song("Ed Sheeran","Hearts Don't Break Around Here","Divide","2017")
song2=Song("Metallica","The Unforgiven","album","2006")
print(song1)
print(song2)

class Song():
    def __init__(self,performer,song,album,year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year

    def __str__(self):
        return f"Performer: {self.performer}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}"

song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
song2 = Song("Metallica"," The Unforgiven", "Album", "2006")
print(song1)
print(song2)
