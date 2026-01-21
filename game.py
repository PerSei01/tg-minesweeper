class Board:
    def __init__(self, width: int = 8, height: int = 8, mines_count: int = 10):
        self.width: int = width
        self.height: int = height
        self.mines_count: int = mines_count

        # Game state
        self.generated: bool = False
        self.game_over: bool = False
        self.win: bool = False

        #F ield data
        self.mines = [[False for _ in range(width)] for _ in range(height)]
        self.numbers = [[0 for _ in range(width)] for _ in range(height)]
        self.opened = [[False for _ in range(width)] for _ in range(height)]
        self.flags = [[False for _ in range(width)] for _ in range(height)]

    # Check if cell lies inside the field
    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height
        
    def reset(self):
        self.generated = False
        self.game_over = False
        self.win = False

        self.mines = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.numbers = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.opened = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.flags = [[False for _ in range(self.width)] for _ in range(self.height)]