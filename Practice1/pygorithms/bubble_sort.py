import inspect


def sort(_list):
    for i in range(len(_list)):
        stop = True
        for j in range(len(_list) - 1, i, -1):
            if _list[j] < _list[j - 1]:
                stop = False
                _list[j], _list[j - 1] = _list[j - 1], _list[j]
        if stop:
            return _list
    return _list

