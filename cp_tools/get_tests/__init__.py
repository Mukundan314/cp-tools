from . import atcoder, codeforces, cses, usaco


def get_tests(provider, **kwargs):
    if provider == "atcoder":
        return atcoder.get_tests(kwargs["contest"], kwargs["task"])
    if provider == "codeforces":
        return codeforces.get_tests(kwargs["contest"], kwargs["index"])
    if provider == "cses":
        return cses.get_tests(kwargs["task"])
    if provider == "usaco":
        return usaco.get_tests(kwargs["problem"])

    raise ValueError("Unknown provider {}".format(provider))
