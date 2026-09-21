from src.item import Item
from src.constants import MAX_QUALITY

class AgedBrieItem(Item):
    def update(self):
        self.sell_in -= 1
        
        if self.quality < MAX_QUALITY:
            self.quality += 1
            
        if self.sell_in < 0 and self.quality < MAX_QUALITY:
            self.quality += 1