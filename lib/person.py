APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self):
        self._name = None  # Private attribute to store the name
        self._job = None   # Private attribute to store the job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) < 25:
            self._name = new_name.title()
        else:
            print("Name must be a string under 25 characters.")
            self._name = None  # Setting name to None if invalid

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

# Example usage:
person = Person()

person.name = "john doe"  # Valid name
print(person.name)  # Output: John Doe

person.name = "this is a very long name for a person"  # Invalid name
# Output: Name must be a string under 25 characters.

person.job = "vdvdvdvd"
print(person.job)  # Output: Job must be in list of approved jobs.
