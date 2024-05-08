
import os

os.system("")
class HealthBar:
    symbolRemaining = "█"
    symbolLost = "_"
    barriers = "|"
    colors = {
            "red":"\033[91m",
            "blue": "\33[34m",
            "green":"\033[92m",
            "default":"\033[0m"
    }


    def __init__(self,
                 entity,
                 length,
                 is_colored: bool = True,
                 color:str = ""):
        self.entity = entity
        self.length = length
        self.currentValue = entity.health
        self.maxValue = entity.healthMax
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors.get("default")
    
    def update(self):
        self.currentValue = self.entity.health

    def draw(self):
        print(self.currentValue, self.maxValue)
        remainingBars = round(self.currentValue / self.maxValue * self.length)
        lostBars = self.length - remainingBars
        print(remainingBars)
        print(f"{self.entity.name}'s health: {self.entity.health}/{self.entity.healthMax}")
        print(f"{self.barriers}"
              f"{self.color if self.is_colored else ''}"
              f"{remainingBars * self.symbolRemaining}"
              f"{lostBars * self.symbolLost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barriers}")
        