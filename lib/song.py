class Song:
    all = []
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.save()

    def save(self):
        Song.all.append(self)
        Song.count += 1

        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1

    @classmethod
    def get_all(cls):
        return cls.all

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count
