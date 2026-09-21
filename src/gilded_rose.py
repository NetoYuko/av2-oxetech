from constants import SULFURAS, AGED_BRIE, BACKSTAGE_PASS
from sulfuras_item import SulfurasItem
from normal_item import NormalItem
from aged_brie_item import AgedBrieItem
from backstage_pass_item import BackstagePassItem

class GildedRose(object):
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
            else:
                updater = NormalItem(item.name, item.sell_in, item.quality)
            
            updater.update()
            
            item.sell_in = updater.sell_in
            item.quality = updater.quality