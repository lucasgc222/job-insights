from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"

    jobs = read_brazilian_file(path)
    print(jobs)
    for job in jobs:
        assert "title" in job
        assert "salary" in job
        assert "type" in job
