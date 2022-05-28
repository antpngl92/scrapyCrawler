from .base_product_spider import BaseProductsSpider

DOMAIN = 'https://gplay.bg'

class PheripheralProductsSpider(BaseProductsSpider):
    name = 'pheripherials'

    start_urls = [
        DOMAIN + '/гейминг-периферия'
    ]

class HardwareProductsSpider(BaseProductsSpider):
    name = 'hardware'

    start_urls = [
        DOMAIN + '/гейминг-хардуер'
    ]






# TODO: delete

# class ProductSpider(scrapy.Spider):
#     name = 'pheripherials'

#     start_urls = [
#         'https://gplay.bg/urage-reaper-neo-1',
#         'https://gplay.bg/maxell-samurai-1200',
#         'https://gplay.bg/spartan-gear-talos',
#         'https://gplay.bg/maxell-samurai-mxg',
#         'https://gplay.bg/urage-reaper-ess',
#         'https://gplay.bg/spartan-gear-peltast',
#         'https://gplay.bg/spartan-gear-titan',
#         'https://gplay.bg/urage-reaper-320',
#         'https://gplay.bg/urage-reaper-900-morph',
#         'https://gplay.bg/x7-gaming-combo-x-7120',
#         'https://gplay.bg/spartan-gear-phalanx',
#         'https://gplay.bg/urage-reaper-310-unleashed',
#         'https://gplay.bg/bloody-v8m',
#         'https://gplay.bg/urage-reaper-500',
#         'https://gplay.bg/logitech-g102-lightsync',
#         'https://gplay.bg/logitech-g102-lightsync-1',
#         'https://gplay.bg/logitech-g102-lightsync-2',
#         'https://gplay.bg/logitech-g102-lightsync-3',
#         'https://gplay.bg/bloody-j90s',
#         'https://gplay.bg/bloody-w60',
#         'https://gplay.bg/bloody-w60-max',
#         'https://gplay.bg/logitech-pop-mouse-blast',
#         'https://gplay.bg/logitech-pop-mouse-daydream',
#         'https://gplay.bg/logitech-pop-mouse-heartbreaker',
#         'https://gplay.bg/aorus-m3',
#         'https://gplay.bg/urage-reaper-600',
#         'https://gplay.bg/asus-rog-strix-impact-ii',
#         'https://gplay.bg/xtrfy-m4-miami-blue',
#         'https://gplay.bg/xtrfy-m4-rgb-pink',
#         'https://gplay.bg/asus-tuf-gaming-m3',
#         'https://gplay.bg/hyperx-pulsefire-core-1',
#         'https://gplay.bg/aorus-m4',
#         'https://gplay.bg/ttesports-level-20-rgb',
#         'https://gplay.bg/bloody-r80',
#         'https://gplay.bg/bloody-b2500',
#         'https://gplay.bg/steelseries-rival-3',
#         'https://gplay.bg/cooler-master-devastator-3',
#         'https://gplay.bg/glorious-model-o--3',
#         'https://gplay.bg/glorious-model-o--2',
#         'https://gplay.bg/glorious-model-d-glossy-black',
#         'https://gplay.bg/glorious-model-o-matte-pink',
#         'https://gplay.bg/glorious-model-d-matte-black',
#         'https://gplay.bg/glorious-model-d-matte-white',
#         'https://gplay.bg/xtrfy-m1-rgb',
#         'https://gplay.bg/asus-rog-strix-impact-ii-electro-punk',
#         'https://gplay.bg/urage-reaper-700-unleashed',
#         'https://gplay.bg/xtrfy-m1-nip-edition',
#         'https://gplay.bg/xtrfy-m4-rgb-white',
#         'https://gplay.bg/xtrfy-m4-rgb-street',
#         'https://gplay.bg/xtrfy-m42-pink',
#         'https://gplay.bg/cooler-master-mm720-2',
#         'https://gplay.bg/cooler-master-mm730',
#         'https://gplay.bg/logitech-g305',
#         'https://gplay.bg/logitech-g305-1',
#         'https://gplay.bg/logitech-g305-lightspeed-wireless',
#         'https://gplay.bg/logitech-g305-lightspeed-wireless-1',
#         'https://gplay.bg/hyperx-pulsefire-haste-1',
#         'https://gplay.bg/hyperx-pulsefire-raid-1',
#         'https://gplay.bg/asus-tuf-gaming-m4-air',
#         'https://gplay.bg/hyperx-pulsefire-surge-1',
#         'https://gplay.bg/rapoo-ralemo-air-1',
#         'https://gplay.bg/rapoo-ralemo-air-1-2',
#         'https://gplay.bg/rapoo-ralemo-air-1-4',
#         'https://gplay.bg/rapoo-ralemo-air-1-6',
#         'https://gplay.bg/cherry-mc-31',
#         'https://gplay.bg/asus-rog-gladius-ii-origin-1',
#         'https://gplay.bg/xtrfy-m4-retro',
#         'https://gplay.bg/steelseries-rival-3-wireless',
#         'https://gplay.bg/hyperx-pulsefire-fps-pro-1',
#         'https://gplay.bg/asus-tuf-gaming-m4-wireless',
#         'https://gplay.bg/endgame-gear-xm1r-white',
#         'https://gplay.bg/endgame-gear-xm1r-black',
#         'https://gplay.bg/endgame-gear-xm1r-dark-frost',
#         'https://gplay.bg/steelseries-rival-5',
#         'https://gplay.bg/logitech-g305-kda',
#         'https://gplay.bg/steelseries-prime-mini',
#         'https://gplay.bg/asus-rog-strix-impact-ii-moonlight-white',
#         'https://gplay.bg/steelseries-prime-neo-noir-edition',
#         'https://gplay.bg/steelseries-aerox-3-2022-edition',
#         'https://gplay.bg/ducky-feather',
#         'https://gplay.bg/aorus-m5',
#         'https://gplay.bg/cherry-mc-9620-fps',
#         'https://gplay.bg/xtrfy-m42-black',
#         'https://gplay.bg/xtrfy-m42-white',
#         'https://gplay.bg/xtrfy-m42-retro',
#         'https://gplay.bg/xtrfy-m42-miami-blue',
#         'https://gplay.bg/hyperx-pulsefire-haste-3',
#         'https://gplay.bg/hyperx-pulsefire-haste-5',
#         'https://gplay.bg/cooler-master-mm711-rgb-glossy',
#         'https://gplay.bg/cooler-master-mm711-rgb-glossy-1',
#         'https://gplay.bg/xtrfy-m4-black',
#         'https://gplay.bg/steelseries-sensei-ten',
#         'https://gplay.bg/steelseries-rival-5-destiny-2-edition',
#         'https://gplay.bg/glorious-model-o',
#         'https://gplay.bg/glorious-model-o-1',
#         'https://gplay.bg/glorious-model-o-3',
#         'https://gplay.bg/glorious-model-o-',
#         'https://gplay.bg/glorious-model-o--1',
#         'https://gplay.bg/glorious-model-d',
#         'https://gplay.bg/glorious-model-d-glossy-white',
#         'https://gplay.bg/glorious-model-o-matte-pink-1',
#         'https://gplay.bg/endgame-xm1-rgb-1',
#         'https://gplay.bg/endgame-gear-xm1r-dark-reflex',
#         'https://gplay.bg/zowie-s1',
#         'https://gplay.bg/zowie-s2',
#         'https://gplay.bg/zowie-ec2',
#         'https://gplay.bg/zowie-fk2-b',
#         'https://gplay.bg/zowie-za12-b',
#         'https://gplay.bg/zowie-za13-b',
#         'https://gplay.bg/zowie-za11-b',
#         'https://gplay.bg/zowie-s2-c',
#         'https://gplay.bg/logitech-g403',
#         'https://gplay.bg/asus-rog-gladius-ii-core',
#         'https://gplay.bg/steelseries-aerox-3',
#         'https://gplay.bg/steelseries-prime',
#         'https://gplay.bg/steelseries-prime-1',
#         'https://gplay.bg/steelseries-aerox-3-2022-edition-2',
#         'https://gplay.bg/xtrfy-m4-tokyo',
#         'https://gplay.bg/endgame-xm1-rgb',
#         'https://gplay.bg/xtrfy-mz1',
#         'https://gplay.bg/logitech-g502-hero',
#         'https://gplay.bg/steelseries-aerox-3-wireless-2022-edition-2',
#         'https://gplay.bg/steelseries-rival-600',
#         'https://gplay.bg/steelseries-aerox-5',
#         'https://gplay.bg/glorious-model-d-wireless-matte-black',
#         'https://gplay.bg/glorious-model-d-wireless-matte-white',
#         'https://gplay.bg/logitech-g-pro-wireless-league-of-legends-edition',
#         'https://gplay.bg/xtrfy-m4-wireless-black',
#         'https://gplay.bg/xtrfy-m4-rgb-wireless-white',
#         'https://gplay.bg/hyperx-pulsefire-haste-7'
#     ]


#     def parse(self, response):
#         products = ProductItem()

#         title = response.css('h1.large-title::text').extract()[0].strip('\n')
#         breadcrum_paths = response.css('div.path a::attr(href)').extract()
#         category = breadcrum_paths[1].strip(DOMAIN + '/')
#         sub_category = breadcrum_paths[2].strip(DOMAIN + '/')
#         subtitle = response.css('.product-subtitle::text').get().strip('\n')
#         product_number = response.css('div.product-ref-number strong::text').extract()[0]
#         price_element = response.css('div.normal-price price').extract()[0]
#         price = round(float(price_element.split("\"")[1]),2)

#         products['title'] = title
#         products['category'] = category
#         products['sub_category']= sub_category
#         products['subtitle'] = subtitle
#         products['product_number'] = product_number
#         products['price'] = price

#         yield products
