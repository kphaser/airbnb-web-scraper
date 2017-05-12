# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbItem(scrapy.Item):
    rev_count = scrapy.Field()
    amenities = scrapy.Field()
    host_id = scrapy.Field()
    hosting_id = scrapy.Field()
    room_type = scrapy.Field()
    price = scrapy.Field()
    bed_type = scrapy.Field()
    person_capacity = scrapy.Field()
    cancel_policy = scrapy.Field()
    rating_communication = scrapy.Field()
    rating_cleanliness = scrapy.Field()
    rating_checkin = scrapy.Field()
    satisfaction_guest = scrapy.Field()
    instant_book = scrapy.Field()
    accuracy_rating = scrapy.Field()
    response_time = scrapy.Field()
    response_rate = scrapy.Field()
    nightly_price = scrapy.Field()
    url = scrapy.Field()
    