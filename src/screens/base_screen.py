from abc import abstractmethod, ABC


class BaseScreen(ABC):
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.game_state_manager = game_state_manager

    @abstractmethod
    def run(self):
        pass


if __name__ == "__main__":
    pass
