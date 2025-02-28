architect_name: str = input('Enter the name of the architect: ')
project_number: int = int(input('Enter the project number: '))
projects_complete_time: int = project_number * 3

print(f'The architect {architect_name} will need {projects_complete_time} hours to complete {project_number} project/s.')
