import urllib.request

from bs4 import BeautifulSoup


def get_tests(task):
    url = "https://cses.fi/problemset/task/{}".format(task)

    with urllib.request.urlopen(url) as res:
        soup = BeautifulSoup(res.read(), "html.parser")
        code_tags = soup.find_all("code")

        inputs = map(lambda x: x.string, code_tags[::2])
        outputs = map(lambda x: x.string, code_tags[1::2])

    return zip(inputs, outputs)
