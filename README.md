Link to tutorial:  https://www.youtube.com/watch?v=ve_0h4Y8nuI&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=1 

In pycharm: start a new project with name ScrapyTutorial. At same time create env witht the same 
name

pip install scrapy

scrapy startproject quotetutorial

cd quotetutorial

scrapy crawl quotes

In terminal:

scrapy shell "http://quotes.toscrape.com/"

response.xpath("//title/text()").extract()

response.xpath("//span[@class='text']/text()").extract()   --> make sure to use different quote symbols

response.css("li.next a").xpath("@href").extract()

response.css("a").xpath("@href").extract()

scrapy crawl quotes -o items.json

scrapy crawl quotes -o items.csv

