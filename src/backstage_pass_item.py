from item import Item
from constants import (
    MAX_QUALITY, 
    MIN_QUALITY, 
    BACKSTAGE_FIRST_LIMIT, 
    BACKSTAGE_SECOND_LIMIT
)

class BackstagePassItem(Item):
    def update(self):
        if self.quality < MAX_QUALITY:
            self.quality += 1
            
        if self.sell_in < BACKSTAGE_FIRST_LIMIT and self.quality < MAX_QUALITY:
            self.quality += 1
            
        if self.sell_in < BACKSTAGE_SECOND_LIMIT and self.quality < MAX_QUALITY:
            self.quality += 1
            
        self.sell_in -= 1
        
        if self.sell_in < 0:
            self.quality = MIN_QUALITY