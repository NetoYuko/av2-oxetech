from src.item import Item
from src.constants import MIN_QUALITY

class NormalItem(Item):
    """Representa um item comum cuja qualidade diminui com o tempo.

    A deterioração dobra após a data de venda, sem reduzir a qualidade abaixo
    do limite mínimo permitido.
    """

    def update(self):
        self.sell_in -= 1
        
        if self.quality > MIN_QUALITY:
            self.quality -= 1
            
        if self.sell_in < 0 and self.quality > MIN_QUALITY:
            self.quality -= 1
