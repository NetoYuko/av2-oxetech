from src.constants import SULFURAS, AGED_BRIE, BACKSTAGE_PASS, CONJURED_MANA_CAKE
from src.sulfuras_item import SulfurasItem
from src.normal_item import NormalItem
from src.aged_brie_item import AgedBrieItem
from src.backstage_pass_item import BackstagePassItem
from src.conjured_item import ConjuredItem

class GildedRose(object):
    """Gerencia o inventário e atualiza a qualidade dos itens diariamente.

    Args:
        items (list[Item]): Itens do inventário que terão seus valores
            atualizados.
    """

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                updater = SulfurasItem(item.name, item.sell_in, item.quality)
            elif item.name == AGED_BRIE:
                updater = AgedBrieItem(item.name, item.sell_in, item.quality)
            elif item.name == BACKSTAGE_PASS:
                updater = BackstagePassItem(item.name, item.sell_in, item.quality)
            elif item.name == CONJURED_MANA_CAKE:
                updater = ConjuredItem(item.name, item.sell_in, item.quality)
            else:
                updater = NormalItem(item.name, item.sell_in, item.quality)
            
            updater.update()
            
            item.sell_in = updater.sell_in
            item.quality = updater.quality
