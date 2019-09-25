import urllib.request

from bs4 import BeautifulSoup


def get_tests(problem):
    url = "http://www.usaco.org/index.php?page=viewproblem2&cpid={}".format(
        problem
    )

    with urllib.request.urlopen(url) as res:
        soup = BeautifulSoup(res.read(), "html.parser")

        inputs = map(lambda x: x.get_text("\n").lstrip(),
                     soup.find_all(class_="in"))
        outputs = map(lambda x: x.get_text("\n").lstrip(),
                      soup.find_all(class_="out"))

    return zip(inputs, outputs)
