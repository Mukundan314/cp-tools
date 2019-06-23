import urllib.request

from bs4 import BeautifulSoup


def get_tests(contest, task):
    url = "https://atcoder.jp/contests/{0}/tasks/{0}_{1}".format(contest, task)

    with urllib.request.urlopen(url) as res:
        soup = BeautifulSoup(res.read(), "html.parser")
        pre_tags = soup.find_all("pre")

        inputs = map(lambda x: x.string, pre_tags[1:len(pre_tags) // 2:2])
        answers = map(lambda x: x.string, pre_tags[2:len(pre_tags) // 2:2])

    return zip(inputs, answers)
