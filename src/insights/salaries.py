from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = []
        for job in self.jobs_list:
            if job["max_salary"].isdigit():
                salaries.append(int(job["max_salary"]))
        return max(salaries)

    def get_min_salary(self) -> int:
        salaries = []
        for job in self.jobs_list:
            if job["min_salary"].isdigit():
                salaries.append(int(job["min_salary"]))
        return min(salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
