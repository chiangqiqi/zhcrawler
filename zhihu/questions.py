"""
question 模块
"""

import requests
import re
from bs4 import BeautifulSoup
import http
from .config import headers

session = requests.Session()
session.cookies = http.cookiejar.LWPCookieJar('cookies')

class Question:
    def __init__(self, url, title=None):
        if not re.compile(r"(http|https)://www.zhihu.com/question/\d{8}").match(url):
            raise ValueError("\"" + url + "\"" + " : it isn't a question url.")
        else:
            self.url = url
        
        r = session.get(self.url,headers=headers, verify=False)
        self.soup = BeautifulSoup(r.content, "lxml")
        
        if title != None: self.title = title

    def parser(self):
        r = session.get(self.url,headers=headers, verify=False)
        self.soup = BeautifulSoup(r.content, "lxml")

    def get_title(self):
        return self.soup.title.text

    def get_detail(self):
        soup = self.soup
        detail = soup.find("div", id="zh-question-detail").div.get_text()
        return detail

    def get_answers_num(self):
        soup = self.soup
        answers_num = 0
        if soup.find("h3", id="zh-question-answer-num") != None:
            answers_num = int(soup.find("h3", id="zh-question-answer-num")["data-num"])
        return answers_num

    def get_followers_num(self):
        soup = self.soup
        followers_num = int(soup.find("div", class_="zg-gray-normal").a.strong.string)
        return followers_num

    def get_topics(self):
        soup = self.soup
        topic_list = soup.find_all("a", class_="zm-item-tag")
        topics = []
        for i in topic_list:
            topics.append(topic)

        return topics

    def get_all_answers(self):
        pass

    def get_top_i_answers(self, n):
        # if n > self.get_answers_num():
        # n = self.get_answers_num()
        j = 0
        answers = self.get_all_answers()
        for answer in answers:
            j = j + 1
            if j > n:
                break
            yield answer

    def get_top_answer(self):
        for answer in self.get_top_i_answers(1):
            return answer

    def get_visit_times(self):
        soup = self.soup
        return int(soup.find("meta", itemprop="visitsCount")["content"])
