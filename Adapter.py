class MediaPlayer:
    def play(self, filename):
        raise NotImplementedError

class MP4Player(MediaPlayer):
    def play(self, filename):
        print(f"Playing MP4 file: {filename}")

class MP3Player(MediaPlayer):
    def play(self, filename):
        print(f"Playing MP3 file: {filename}")

class AVIPlayer:
    def play_avi(self, filename):
        print(f"Playing AVI file: {filename}")

class AVIAdapter(MediaPlayer):
    def __init__(self, avi_player):
        self.avi_player = avi_player

    def play(self, filename):
        self.avi_player.play_avi(filename)


def play_media(player, filename):
    player.play(filename)

mp4_player = MP4Player()
mp3_player = MP3Player()
avi_player = AVIAdapter(AVIPlayer())

play_media(mp4_player, "video.mp4")
play_media(mp3_player, "audio.mp3")
play_media(avi_player, "movie.avi")
