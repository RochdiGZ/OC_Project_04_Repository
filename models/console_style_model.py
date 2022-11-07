from rich.console import Console


class Style:
    def __init__(self):
        self.style_b = "bold white on blue"
        self.style_g = "bold white on green"
        self.style_r = "bold white on red"
        self.style_y = "bold white on yellow"
        self.console = Console(width=119)
