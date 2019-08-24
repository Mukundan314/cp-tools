import urllib.request

from bs4 import BeautifulSoup


def get_tests(contest, problem):
    url = "https://codeforces.com/contest/{}/problem/{}".format(
        contest, problem)

    with urllib.request.urlopen(url) as res:
        soup = BeautifulSoup(res.read(), "html.parser")

        inputs = map(lambda x: x.pre.get_text("\n").lstrip(),
                     soup.find_all(class_="input"))
        outputs = map(lambda x: x.pre.get_text("\n").lstrip(),
                      soup.find_all(class_="output"))

    return zip(inputs, outputs)
