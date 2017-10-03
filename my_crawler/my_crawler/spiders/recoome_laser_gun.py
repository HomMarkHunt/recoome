# -*- coding: utf-8 -*-
import scrapy
import boto3
from bs4 import BeautifulSoup
from scrapy.http import Request

class RecoomeLaserGunSpider(scrapy.Spider):
    name = 'recoome-laser-gun'
    start_urls = ['http://ozeki.digimu.jp/sel_shop_DB/sel_shop.php?code=0012_0026']

    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        url = response.url[:22]
        imageList = []
        for link in soup.findAll("a"):
            if "pdf" in link.get("href"):
                path = link.get("href")[2:]
                uri = url + path
                print("######url#######")
                print(uri)

                yield Request(
                    url=uri,
                    callback=self.upload_pdf
                )

    def upload_pdf(self, response):
        s3_client = boto3.client('s3')
        print("Saving PDF " + response.url)
        path = response.url.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(response.body)
        s3_client.upload_file(path, 'tirashi', path)
