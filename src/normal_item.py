from item import Item
from constants import MIN_QUALITY

class NormalItem(Item):
    def update(self):
        self.sell_in -= 1
        
        if self.quality > MIN_QUALITY:
            self.quality -= 1
            
        if self.sell_in < 0 and self.quality > MIN_QUALITY:
            self.quality -= 1