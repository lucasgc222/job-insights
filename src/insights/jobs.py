from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, filepath: str) -> List[Dict]:
        with open(filepath, "r") as file:
            self.jobs_list = list(csv.DictReader(file))

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            job_type = job.get('job_type')
            if job_type:
                job_types.add(job_type)
        return job_types

    def filter_by_multiple_criteria(
            self, jobs: List[dict], filter_criteria: dict) -> List[dict]:
        if type(filter_criteria) != dict:
            raise TypeError("filter_criteria must be a dict")

        filtered = []

        for key, value in filter_criteria.items():
            for job in jobs:
                if job.get(key) == value and job not in filtered:
                    filtered.append(job)

        return filtered
