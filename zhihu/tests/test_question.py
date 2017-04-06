from unittest import TestCase
from zhihu.questions import Question

class TestQuestion(TestCase):
    def test_title(self):
        "docstring"
        _url = "https://www.zhihu.com/question/47647183"
        que = Question(_url)
        assert que.get_topics == "beijing"
    
