import tqdm
import tqdm.auto as auto


def test_tqdm():
    assert tqdm.tqdm((1, 2, 3), "more", "args") == (1, 2, 3)


def test_tqdm_auto():
    assert auto.tqdm((1, 2, 3), "more", "args") == (1, 2, 3)
