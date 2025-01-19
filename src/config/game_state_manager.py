# manages all game states
class GameStateManager:
    # initialises game state
    def __init__(self, current_state):
        self.current_state = current_state

    # gets the current game state
    def get_state(self):
        return self.current_state

    # sets the next game state
    def set_state(self, state):
        self.current_state = state


if __name__ == "__main__":
    pass
