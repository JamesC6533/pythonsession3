from personclass import Person


# The Employee class is defined, which inherits from the Person class.
# It represents a person with a job.
class Employee(Person):
    '''
    A person with a job
    '''

    # The __init__ method is overridden to include an additional parameter,
    # has_job (with a default value of True).
    def __init__(self, nationality, name, language, has_job=True):
        # The super().__init__(nationality, name, language) is called to invoke the constructor,
        # of the base class (Person) and initialize the inherited attributes.
        super().__init__(nationality, name, language)
        # The instance variable self._has_job is set to the provided value of has_job.
        self._has_job = has_job

    # The has_job method is defined as a property,
    # allowing access to the _has_job instance variable as if it were an attribute.
    @property
    def has_job(self):
        return self._has_job


# This block of code is executed only when the script is run directly (not imported).
# Two instances of the Employee class (tom and mary) are created,
# with different values passed to the constructor.
if __name__ == '__main__':
    tom = Employee('England', 'Tom', 'Hello', False)
    mary = Employee('Italy', 'Mary', 'Ciao', True)

    # A loop iterates over tom and mary, the created Employee instances
    for employee in tom, mary:
        # The has_job property is accessed to determine the job status (True or False).
        job_status = 'have a' if employee.has_job else "don't have a"
        print("Hi! I am {} from {} and I {} job!".format(employee.name, employee.nationality, job_status))
        employee.what_language()
        print()

    # The head_count method is called on the Person class,
    # to print the total number of instances,created (count).
    print(Person.head_count())
