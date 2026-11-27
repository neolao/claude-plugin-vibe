import pickle


def encode(obj):
    return pickle.dumps(obj)


def decode(blob):
    return pickle.loads(blob)
