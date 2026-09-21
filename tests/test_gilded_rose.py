from gilded_rose import GildedRose
from gilded_rose import Item

# Teste para item normal

def test_item_normal_perde_qualidade_e_sell_in():
    item = Item("Item normal", 10, 20)
    loja = GildedRose([item])

    loja.att()

    assert item.sell_in == 9
    assert item.quality == 19
    
def test_item_normal_degrada_duas_vezes_mais_rapido_apos_vencimento():
    item = Item("Item normal", 0, 20)
    loja = GildedRose([item])

    loja.att()

    assert item.sell_in == -1
    assert item.quality == 18
    
def test_item_normal_nao_pode_ter_qualidade_negativa():
    item = Item("Item normal", 5, 0)
    loja = GildedRose([item])

    loja.att()

    assert item.quality == 0
    
# Teste para Aged Brie

def test_aged_brie_aumenta_qualidade():
    item = Item("Aged Brie", 5, 10)
    loja = GildedRose([item])
    
    loja.att()
    
    assert item.sell_in == 4
    assert item.quality == 11
    
def test_aged_brie_aumenta_qualidade_duas_vezes_apos_vencimento():
    item = Item("Aged Brie", 0, 10)
    loja = GildedRose([item])
    
    loja.att()
        
    assert item.sell_in == -1
    assert item.quality == 12
    
def test_aged_brie_nao_ultrapassa_qualidade_50():
    item = Item("Aged Brie", 10, 50)
    loja = GildedRose([item])

    loja.att()

    assert item.quality == 50
    
# Teste para Sulfuras

def test_sulfuras_nunca_muda():
    item = Item("Sulfuras, Hand of Ragnaros", 10, 80)
    loja = GildedRose([item])

    loja.att()

    assert item.sell_in == 10
    assert item.quality == 80
    
# Teste para Backstage

def test_backstage_aumenta_um_ponto_quando_faltam_mais_de_10_dias():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    loja = GildedRose([item])

    loja.att()

    assert item.sell_in == 14
    assert item.quality == 21
    
def test_backstage_aumenta_dois_pontos_quando_faltam_10_dias():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
    loja = GildedRose([item])

    loja.att()

    assert item.sell_in == 9
    assert item.quality == 22
    
def test_backstage_aumenta_tres_pontos_quando_faltam_5_dias():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20
    )
    loja = GildedRose([item])

    loja.att()

    assert item.sell_in == 4
    assert item.quality == 23
    
def test_backstage_perde_toda_qualidade_apos_o_show():
    item = Item(
        "Backstage passes to a TAFKAL80ETC concert",
        0,
        20
    )
    loja = GildedRose([item])

    loja.att()

    assert item.sell_in == -1
    assert item.quality == 0
