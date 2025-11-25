#write a program that  prints out the numbers of second in a year
seconds_in_a_minute = 60
minutes_in_an_hour = 60
hours_in_a_day = 24
days_in_a_year = 365
seconds_in_a_year = seconds_in_a_minute * minutes_in_an_hour * hours_in_a_day * days_in_a_year
print(seconds_in_a_year)

# write a function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 