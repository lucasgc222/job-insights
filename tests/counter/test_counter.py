from src.pre_built.counter import count_ocurrences

JOBS_DATAPATH = "data/jobs.csv"


def test_counter():
    assert count_ocurrences(JOBS_DATAPATH, "Python") == 1639
    assert count_ocurrences(JOBS_DATAPATH, "Javascript") == 122
