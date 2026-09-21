from src.item import Item
from src.constants import (
    MAX_QUALITY, 
    MIN_QUALITY, 
    BACKSTAGE_FIRST_LIMIT, 
    BACKSTAGE_SECOND_LIMIT
)

class BackstagePassItem(Item):
    """Representa um passe de backstage com qualidade variável.

    A qualidade aumenta à medida que o concerto se aproxima e cai para zero
    após a data de venda.
    """

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
