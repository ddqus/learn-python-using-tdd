def chunks(lst, n):
    """
    Yield successive n-sized chunks from lst.
    https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def test():
    sut = [1, 2, 3, 4, 5, 6, 7]

    assert list(chunks(sut, 2)) == [[1, 2], [3, 4], [5, 6], [7]]
    assert list(chunks(sut, 3)) == [[1, 2, 3], [4, 5, 6], [7]]
    assert list(chunks(sut, 4)) == [[1, 2, 3, 4], [5, 6, 7]]
    assert list(chunks(sut, 5)) == [[1, 2, 3, 4, 5], [6, 7]]
