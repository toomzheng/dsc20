# Question 4

def doctests_go_here():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes long with 1220980 streams
    >>> track1.get_artist()
    'Cordae'
    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'
    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True
    
    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False
    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']
    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759
    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA
    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799
    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'
    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'
    >>> play3 = Playlist('test', 'ab')
    >>> play3.get_most_played_song()
    ''
    >>> play3.get_total_streams()
    0
    >>> play3.get_total_length()
    0
    >>> play3.sort_songs('length')
    >>> play3.songs
    []
    >>> play2.combine_playlists(play3)
    True

    >>> TS = Song('Shake it Off', 1.23, '1989', 'Taylor Swift', 12345)
    >>> BC = Song('Halo', 2.34, 'I Am... Sasha Fierce', 'Beyoncé', 23456)
    >>> JB = Song('Baby', 3.45, 'Okay', 'Justin Bieber', 34567)
    >>> LG = Song('Bad Romance', 4.53, 'Talk You Back', 'Lady Gaga', 45678)
    >>> AG = Song('Side to Side', 1.01, 'Dangerous Woman', 'Ariana Grande', 56432)
    >>> SG = Song('BiggieBig', 3.22, 'The Album', 'Selena Gomez', 987)
    >>> WG = Song('God is Fair', 32.43, 'GOD IS AROUND US', 'Windaco God', 99999999)
    >>> BM = Song('Talking to the Moon', 3.38, 'Doo-Wops & Hooligans', 'Bruno Mars', 2814901)
    >>> NB = Song('Long Song', 99999.99, 'Billy Boy', 'Nobody Billy', 7654321)
    >>> Playlist1 = Playlist('God Spoken!', 'Yes sir')
    >>> Playlist2 = Playlist('Do you still love me if I am DJ', 'Xiaozi')
    >>> Playlist3 = Playlist('Best Song', 'Ye')
    >>> lst = [TS,BC,JB,LG,AG,SG,WG,BM,NB]

    # Song
    >>> song1 = Song('Bohemian Rhapsody', 5.55, 'A Night at the Opera', 'Queen', 1000000)
    >>> song2 = Song('Stairway to Heaven', 8.02, 'Led Zeppelin IV', 'Led Zeppelin', 2000000)
    >>> song3 = Song('Purple Rain', 8.41, 'Purple Rain', 'Prince', 3000000)
    
    # Playlist
    >>> playlist1 = Playlist('Rock Classics', 'RockFan')
    >>> playlist2 = Playlist('80s Hits', 'RetroLover')
    >>> playlist3 = Playlist('All Time Greats', 'MusicBuff')

    # add_song()
    >>> playlist1.add_song(song1)
    True
    >>> playlist1.add_song(song1) 
    False
    >>> playlist1.add_song(song2)
    True

    # remove_song() 
    >>> playlist1.remove_song(song1) 
    True
    >>> playlist1.remove_song(song1) 
    False
    >>> playlist1.remove_song(song3) 
    False

    # sort_songs() 
    >>> playlist2.add_song(song1)
    True
    >>> playlist2.add_song(song2)
    True
    >>> playlist2.add_song(song3)
    True
    >>> playlist2.sort_songs('length')
    >>> [song.get_name() for song in playlist2.get_songs()]
    ['Bohemian Rhapsody', 'Stairway to Heaven', 'Purple Rain']
    >>> playlist2.sort_songs('streams')
    >>> [song.get_name() for song in playlist2.get_songs()]
    ['Bohemian Rhapsody', 'Stairway to Heaven', 'Purple Rain']
    >>> playlist2.sort_songs('name')
    >>> [song.get_name() for song in playlist2.get_songs()]
    ['Bohemian Rhapsody', 'Purple Rain', 'Stairway to Heaven']

    # play() 
    >>> print(playlist3.play()) 
    Empty
    >>> playlist3.add_song(song1)
    True
    >>> print(playlist3.play()) 
    Listening to 'Bohemian Rhapsody' by Queen
    >>> playlist3.add_song(song2)
    True
    >>> print(playlist3.play()) 
    Listening to 'Bohemian Rhapsody' by Queen
    Listening to 'Stairway to Heaven' by Led Zeppelin

    # combine_playlists() 
    >>> empty_playlist = Playlist('Empty', 'Nobody')
    >>> playlist1.combine_playlists(empty_playlist) 
    True
    >>> playlist2.combine_playlists(playlist3) 
    2
    >>> playlist3.combine_playlists(playlist2) 
    2

    # get_most_played_song() 
    >>> empty_playlist.get_most_played_song() 
    ''
    >>> playlist3.get_most_played_song() 
    'Purple Rain'
    >>> playlist3.add_song(song3)
    False
    >>> playlist3.get_most_played_song() 
    'Purple Rain'
    """
    return


class Song:
    """
    Implementation of a song
    """

    platform = 'Spotify'

    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song
        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        assert isinstance(name, str) and name
        self.name = name

        assert isinstance(length, float) and length > 0
        self.length = length

        assert isinstance(album, str) and album
        self.album = album

        assert isinstance(artist, str) and artist
        self.artist = artist

        assert isinstance(streams, int) and streams > 0
        self.streams = streams


    def get_name(self):
        """ Getter for name attribute """
        return self.name


    def get_length(self):
        """ Getter for length attribute """
        return self.length


    def get_album(self):
        """ Getter for album attribute """
        return self.album


    def get_artist(self):
        """ Getter for artist attribute """
        return self.artist


    def get_streams(self):
        """ Getter for streams attribute """
        return self.streams


    def __str__(self):
        """String representation of Song"""
        return f"'{self.name}' by {self.artist} on '{self.album}' \
is {self.length} minutes long with {self.streams} streams"


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        self.streams += 1
        return f"Listening to '{self.name}' by {self.artist}"


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(playlist, Playlist)
        for p in playlist.songs:
            if p == self:
                return False
        
        playlist.songs.append(self)
        return True


# Question 5

class Playlist: 
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist
        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist
        Attributes:
        songs (list): list used to store songs in playlist
        """
        assert isinstance(title, str) and title
        self.title = title

        assert isinstance(user, str) and user
        self.user = user
        self.songs = []


    def get_title(self):
        """ Getter for title attribute """
        return self.title


    def get_user(self):
        """ Getter for user attribute """
        return self.user
    

    def get_songs(self):
        """ Getter for songs attribute """
        return self.songs


    def __str__(self):
        """String representation of Playlist"""
        return f"Playlist '{self.title}' by {self.user} \
has {len(self.songs)} songs"


    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(song, Song)
        if song in self.songs:
            return False
        self.songs.append(song)
        return True


    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        assert isinstance(song, Song)
        if song in self.songs:
            self.songs.remove(song)
            return True
        return False
        


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        self.songs.sort(key=lambda song: getattr(song, sort_by))


    def get_total_streams(self):
        """Returns the total amount of streams of the songs in the playlist"""
        return sum(song.get_streams() for song in self.songs)

    def get_total_length(self):
        """Returns the total length of the playlist"""
        return sum(song.get_length() for song in self.songs)

    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that records all the songs played.
        If the playlist is empty, return "Empty"
        """
        if not self.songs:
            return "Empty"
        return "\n".join([song.listen() for song in self.songs])
    

    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        assert isinstance(other_playlist, Playlist)
        failed_adds = sum(1 for song in other_playlist.get_songs() \
                          if not self.add_song(song))
        return True if failed_adds == 0 else failed_adds
    

    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        if not self.songs:
            return ""
        return max(self.songs, key=lambda x: x.get_streams()).get_name()