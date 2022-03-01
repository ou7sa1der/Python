days = int(input())

treated_patients = 0
untreated_patients = 0
treated_patients_sum = 0
untreated_patients_sum = 0
doctors_count = 7
days_count = 0

for patients in range(1, days + 1):
    days_count += 1
    if days_count % 3 == 0 and untreated_patients > treated_patients:
        doctors_count += 1
    patients = int(input())
    if patients >= 7:
        untreated_patients = patients - doctors_count
        treated_patients = patients - untreated_patients
    else:
        untreated_patients = 0
        treated_patients = patients
    treated_patients_sum += treated_patients
    untreated_patients_sum += untreated_patients

print(f"Treated patients: {treated_patients_sum}.")
print(f"Untreated patients: {untreated_patients_sum}.")