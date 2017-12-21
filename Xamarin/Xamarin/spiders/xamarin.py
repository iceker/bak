# -*- coding: utf-8 -*-
import scrapy
import re


class XamarinSpider(scrapy.Spider):
    name = 'xamarin'
    allowed_domains = ['blog.chinaunix.net']
    start_urls = ['http://blog.chinaunix.net/uid-78707-id-5773361.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773362.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773363.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773364.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773365.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773366.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773367.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773368.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773369.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773370.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773372.html/',
                  'http://blog.chinaunix.net/uid-78707-id-5773373.html/'
                 ]

    def parse(self, response):
        input = open('head.txt','r')
        head = input.read()
        input.close()
        title = response.xpath('/html/head/title').extract_first("")
        article = response.xpath("//div[@class='Blog_right1_1 Blog_right1_11']").extract_first("")
        martch_re = re.match(".*-id-(\d+).*",response.url)
        file_name = martch_re.group(1)
        output = open(file_name+".html",'w')
        output.write(head+title+'</head><body>'+article+'</body>')
        output.close()
        pass


