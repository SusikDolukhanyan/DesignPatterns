
class State:
    def play(self, player):
        pass

    def pause(self, player):
        pass

    def stop(self, player):
        pass

class PlayingState(State):
    def play(self, player):
        print("Already playing.")

    def pause(self, player):
        print("Pausing playback.")
        player.set_state(PausedState())

    def stop(self, player):
        print("Stopping playback.")
        player.set_state(StoppedState())

class PausedState(State):
    def play(self, player):
        print("Resuming playback.")
        player.set_state(PlayingState())

    def pause(self, player):
        print("Already paused.")

    def stop(self, player):
        print("Stopping playback.")
        player.set_state(StoppedState())

class StoppedState(State):
    def play(self, player):
        print("Starting playback.")
        player.set_state(PlayingState())

    def pause(self, player):
        print("Can't pause, player is stopped.")

    def stop(self, player):
        print("Already stopped.")


class MediaPlayer:
    def __init__(self):
        self.state = StoppedState()  

    def set_state(self, state):
        self.state = state

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)


if __name__ == "__main__":
    player = MediaPlayer()

    print("\nInitial state: Stopped")
    player.play()

    print("\nCurrent state: Playing")
    player.pause()

    print("\nCurrent state: Paused")
    player.play()

    print("\nCurrent state: Playing")
    player.stop()

    print("\nCurrent state: Stopped")
    player.pause()
