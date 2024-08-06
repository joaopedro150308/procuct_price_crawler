from varredor_de_sites.spiders.shopee_spider import bot, ShopeeProductSpider
from selenium_functions import driver, wait, logar_shopee


logar_shopee(driver, wait)
input('')
driver.quit()
# bot.crawl(ShopeeProductSpider)
# bot.start()
