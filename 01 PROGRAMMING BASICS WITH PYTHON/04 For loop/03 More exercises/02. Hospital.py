period = int(input())

medics = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period + 1):
    if day % 3 != 0:
        new_patients = int(input())
        if new_patients <= medics:
            treated_patients += new_patients
        else:
            treated_patients += medics
            untreated_patients += new_patients - medics
    else:
        if untreated_patients > treated_patients:
            medics += 1
            new_patients = int(input())
            if new_patients <= medics:
                treated_patients += new_patients
            else:
                treated_patients += medics
                untreated_patients += new_patients - medics
        else:
            new_patients = int(input())
            if new_patients <= medics:
                treated_patients += new_patients
            else:
                treated_patients += medics
                untreated_patients += new_patients - medics

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')