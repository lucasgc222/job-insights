from src.pre_built.counter import count_ocurrences

JOBS_DATAPATH = "data/jobs.csv"
WORDS_DATAPATH = "tests/mocks/words.csv"


def test_counter():
    assert count_ocurrences(JOBS_DATAPATH, "Python") == 1639
    assert count_ocurrences(JOBS_DATAPATH, "Javascript") == 122
    assert count_ocurrences(WORDS_DATAPATH, "Python") == 3
    assert count_ocurrences(WORDS_DATAPATH, "Javascript") == 2
