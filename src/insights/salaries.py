from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = self.get_salary_by_column_type("max_salary")
        return max(salaries)

    def get_min_salary(self) -> int:
        salaries = self.get_salary_by_column_type("min_salary")
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
        filtered = []
        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    filtered.append(job)
            except ValueError:
                continue

        return filtered

    def get_salary_by_column_type(self, type: str) -> List:
        if type not in ['min_salary', 'max_salary']:
            raise TypeError("Invalid type")

        salaries = []
        for job in self.jobs_list:
            if job[type].isdigit():
                salaries.append(int(job[type]))
        return salaries
