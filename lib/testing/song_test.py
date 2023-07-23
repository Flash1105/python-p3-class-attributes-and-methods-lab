import pytest
from song import Song

class TestSong:
    def setup_method(self):
        # Reset class attributes before each test
        Song.count = 0
        Song.genres = []
        Song.artists = []
        Song.genre_count = {}
        Song.artist_count = {}

    def test_song_instantiation(self):
        song = Song("99 Problems", "Jay Z", "Rap")
        assert song.name == "99 Problems"
        assert song.artist == "Jay Z"
        assert song.genre == "Rap"

    def test_song_count(self):
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert Song.count == 3

    def test_genres_list(self):
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert "Rap" in Song.genres
        assert "Pop" in Song.genres
        assert "Rock" in Song.genres

    def test_genre_count(self):
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.genre_count["Rap"] == 1
        assert Song.genre_count["Pop"] == 2
        assert Song.genre_count["Rock"] == 1

    def test_artists_list(self):
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert "Jay Z" in Song.artists
        assert "Beyonce" in Song.artists
        assert "Nirvana" in Song.artists

    def test_artist_count(self):
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.artist_count["Jay Z"] == 1
        assert Song.artist_count["Beyonce"] == 1
        assert Song.artist_count["Nirvana"] == 1
        assert Song.artist_count["Hall and Oates"] == 1
