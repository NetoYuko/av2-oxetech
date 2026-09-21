class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

MIN_QUALITY = 0
MAX_QUALITY = 50

BACKSTAGE_FIRST_LIMIT = 11
BACKSTAGE_SECOND_LIMIT = 6

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                continue
            
            if item.name == AGED_BRIE:
                item.sell_in = item.sell_in - 1
                if item.quality < MAX_QUALITY:
                    item.quality = item.quality + 1
                if item.sell_in < 0 and item.quality < MAX_QUALITY:
                    item.quality = item.quality + 1
                continue
            
            if item.name == BACKSTAGE_PASS:
                if item.quality < MAX_QUALITY:
                    item.quality += 1
                if item.sell_in < BACKSTAGE_FIRST_LIMIT and item.quality < MAX_QUALITY:
                    item.quality += 1
                if item.sell_in < BACKSTAGE_SECOND_LIMIT and item.quality < MAX_QUALITY:
                    item.quality += 1
                    
                item.sell_in -= 1
                
                if item.sell_in < 0:
                    item.quality = MIN_QUALITY
                
                continue
            
            item.sell_in -= 1
            
            if item.quality > MIN_QUALITY:
                item.quality -= 1
                
            if item.sell_in < 0 and item.quality > MIN_QUALITY:
                item.quality -= 1