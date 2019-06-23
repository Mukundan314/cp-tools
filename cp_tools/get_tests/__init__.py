from . import atcoder


def get_tests(provider, **kwargs):
    if provider == "atcoder":
        return atcoder.get_tests(kwargs["contest"], kwargs["task"])

    raise ValueError("Unknown provider {}".format(provider))
