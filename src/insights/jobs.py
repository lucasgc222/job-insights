from typing import List, Dict
import csv

class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, filepath: str) -> List[Dict]:
        with open(filepath, "r") as file:
            self.jobs_list = list(csv.DictReader(file))

    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
