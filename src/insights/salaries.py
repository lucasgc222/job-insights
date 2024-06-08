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
        if 'max_salary' not in job or 'min_salary' not in job:
            raise ValueError("Must contain 'min_salary' and 'max_salary'")

        try:
            salary = int(salary)
            min_salary = int(job['min_salary'])
            max_salary = int(job['max_salary'])
        except (ValueError, TypeError):
            raise ValueError("Must be a numeric or string")

        if min_salary > max_salary:
            raise ValueError(
                "min_salary must be less than or equal to max_salary"
            )

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
