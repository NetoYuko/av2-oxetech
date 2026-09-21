from src.constants import MIN_QUALITY
from src.item import Item


class ConjuredItem(Item):
    def update(self):
        self.sell_in -= 1

        quality_loss = 2
        if self.sell_in < 0:
            quality_loss *= 2

        self.quality = max(MIN_QUALITY, self.quality - quality_loss)
