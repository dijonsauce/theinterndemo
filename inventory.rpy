#label  inventory:
    $config..rollback.enabled = False
    $quick_menu = False
    $environment_SM = SpriteManager(event = environmentEvents)
    $inventory-SM = spriteManager(update = inventoryUpdate, event = inventoryEvents)
    $environment_sprites = []
    $inventory_sprites = []
    $environment_items = []
    $inventory_items = []

#Invotry items, phone ot contact byrne
#contact cards
