from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type, filename):
        pass

class Mp4Player:
    def play_mp4(self, filename):
        print(f"Воспроизводим MP4 файл: {filename}")


class VlcPlayer:
    def play_vlc(self, filename):
        print(f"Воспроизводим VLC файл: {filename}")


class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type == "mp4":
            self.player = Mp4Player()
        elif audio_type == "vlc":
            self.player = VlcPlayer()
        else:
            self.player = None

    def play(self, audio_type, filename):
        if audio_type == "mp4":
            self.player.play_mp4(filename)
        elif audio_type == "vlc":
            self.player.play_vlc(filename)
        else:
            print(f"Формат {audio_type} не поддерживается")


class AudioPlayer(MediaPlayer):
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            print(f"Воспроизводим MP3 файл: {filename}")

        elif audio_type in ["mp4", "vlc"]:
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, filename)
        else:
            print(f"Формат {audio_type} не поддерживается")


if __name__ == "__main__":

    player = AudioPlayer()

    print("Тестируем разные форматы")
    player.play("mp3", "song.mp3")
    player.play("mp4", "video.mp4")
    player.play("vlc", "movie.vlc")
    player.play("avi", "clip.avi")