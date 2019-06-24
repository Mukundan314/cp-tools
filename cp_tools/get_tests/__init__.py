from . import atcoder, codeforces


def get_tests(provider, **kwargs):
    if provider == "atcoder":
        return atcoder.get_tests(kwargs["contest"], kwargs["task"])
    if provider == "codeforces":
        return codeforces.get_tests(kwargs["contest"], kwargs["index"])

    raise ValueError("Unknown provider {}".format(provider))
