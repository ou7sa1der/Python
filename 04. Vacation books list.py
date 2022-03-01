pages_count = int(input())
pages_for_hour = int(input())
days_count_for_a_book = int(input())

total_time_for_book = pages_count / pages_for_hour
needed_hours_a_day = total_time_for_book / days_count_for_a_book

print(needed_hours_a_day)