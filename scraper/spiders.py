import os

from scrapy import Spider
from .items import SBROddsItem


class SBROddsSpider(Spider):
    name = "sbr_odds_spider"
    allowed_domains = ["sportsbookreview.com"]
    start_urls = ["http://www.sportsbookreview.com/betting-odds/mlb-baseball/"]

    def parse(self, res):
        scheduled = "event-holder holder-scheduled"

        events    = "//div[@class='" + scheduled + "']/div[1]/@id"
        events    = res.xpath(events).extract()

        teams    = "//div[@class='" + scheduled + "']/div[1]" + \
                   "//span[@class='team-name']/@rel"
        teams    = res.xpath(teams).extract()
        teams    = [[teams[x], teams[x+1]]
                    for x in range(0,len(teams),2)]

        pitchers = "//div[@class='" + scheduled + "']/div[1]" + \
                   "//span[@class=' player']/text()"
        pitchers = res.xpath(pitchers).extract()
        pitchers = [p.strip() for p in pitchers]
        pitchers = [[pitchers[x], pitchers[x+1]]
                    for x in range(0,len(pitchers),2)]

        data =   list(zip(events, zip(teams, pitchers)))
        print(data)
        #
        # for d in data:
        #     item = SBROddsItem()
        #     item['id'] = event
        #     yield item
