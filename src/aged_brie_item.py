from src.item import Item
from src.constants import MAX_QUALITY

class AgedBrieItem(Item):
    """Representa o Aged Brie, cuja qualidade aumenta com o tempo.

    A qualidade aumenta duas vezes mais depois da data de venda e nunca
    ultrapassa o limite máximo permitido.
    """

    def update(self):
        self.sell_in -= 1
        
        if self.quality < MAX_QUALITY:
            self.quality += 1
            
        if self.sell_in < 0 and self.quality < MAX_QUALITY:
            self.quality += 1
