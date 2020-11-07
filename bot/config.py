import os


def extract_namespace(namespace='BOT'):
    namespace += '_'
    keys = filter(lambda k: k.startswith(namespace), os.environ.keys())
    return dict(map(lambda k: (k[len(namespace):], os.environ.get(k, None)), keys))


SETTINGS = extract_namespace()
