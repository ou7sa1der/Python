command = input()
free_seats_for_projection = int(input())
ticket_command = input()

all_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0
total_student_ticket_percentage_count = 0
total_standard_ticket_percentage_count = 0
total_kid_ticket_percentage_count = 0
movies_count = 0

while True:
    while ticket_command != "Finish":
        if ticket_command == "student":
            student_count += 1
            total_student_ticket_percentage_count += 1
            ticket_command = input()
            continue
        elif ticket_command == "standard":
            standard_count += 1
            total_standard_ticket_percentage_count += 1
            ticket_command = input()
            continue
        elif ticket_command == "kid":
            kid_count += 1
            total_kid_ticket_percentage_count += 1
            ticket_command = input()
            continue
        else:
            all_tickets_count = student_count + kid_count + standard_count
            all_tickets += all_tickets_count
            hall_percentage = (all_tickets_count / free_seats_for_projection) * 100
            student_count = 0
            standard_count = 0
            kid_count = 0
            print(f"{command} - {hall_percentage:.2f}% full.")
            command = input()
            free_seats_for_projection = int(input())
            ticket_command = input()
            continue
    break

all_tickets_count = student_count + kid_count + standard_count
all_tickets += all_tickets_count
hall_percentage = (all_tickets_count / free_seats_for_projection) * 100
total_student_ticket_percentage = total_student_ticket_percentage_count / all_tickets * 100
total_standard_ticket_percentage = total_standard_ticket_percentage_count / all_tickets * 100
total_kid_ticket_percentage = total_kid_ticket_percentage_count / all_tickets * 100
print(f"{command} - {hall_percentage:.2f}% full.")
print(f"Total tickets: {all_tickets}")
print(f"{total_student_ticket_percentage:.2f}% student tickets.")
print(f"{total_standard_ticket_percentage:.2f}% standard tickets.")
print(f"{total_kid_ticket_percentage:.2f}% kids tickets.")