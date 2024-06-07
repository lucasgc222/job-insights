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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
