import threading
from Queue import Queue
from Spider import Spider
from GeneralInfo import *
import urllib2
from bs4 import BeautifulSoup
from shutil import copyfile
import os

QUEUE_FILE = settings.PATH + '/HistoryForensics/Chrome_Hist.csv'
CRAWLED_FILE = settings.PATH + '/HistoryForensics/CrawledUrls.txt'
NUMBER_OF_THREADS = 2
Queue = Queue()
Spider()
keywords = ''


class MainSpider:

    def work(self):
        while True:
            url = Queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            Queue.task_done()

    def create_workers(self):
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()

    def create_jobs(self):
        for link in file_to_set(QUEUE_FILE):
            Queue.put(link)
        Queue.join()
        self.crawl()

    def crawl(self):
        queued_links = file_to_set(QUEUE_FILE)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the queue')
            self.create_jobs()

    @staticmethod
    def get_keywords():

        common_words = open('FileStorage/common.txt', 'r').readlines()
        keywords = open('HistoryForensics/keywords.txt', 'r').read().split('\n')
        f = open('HistoryForensics/keywords.txt', 'a')
        urls = file_to_set(QUEUE_FILE)
        user_agent = 'Mozilla/4.0 (compatible; 5.5; Windows NT)'
        head = {'User-Agent': user_agent}
        for i in urls:
            print urls
            request = urllib2.Request(i[1:-1], headers=head)
            try:
                html_content = urllib2.urlopen(request).read()
            except ValueError as e:
                print 'Error while loading page at', i, 'continuing...'
                continue
            soup = BeautifulSoup(html_content)
            for script in soup(["script", "style"]):
                script.extract()
                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
                text = '\n'.join(chunk for chunk in chunks if chunk)
                (text.encode('utf-8'))
                visible_text = soup.getText()
                words = visible_text.split(' ')
                for word in words:
                    if word not in common_words and word not in keywords and word.isalnum():
                        f.write(word.encode('utf-8') + '\n')
                        keywords.append(word)
                    else:
                        continue
