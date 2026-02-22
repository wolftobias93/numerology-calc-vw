from datetime import datetime
import math

char_map = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 1, 
    'k': 2,
    'l': 3,
    'm': 4,
    'n': 5,
    'o': 6,
    'p': 7,
    'q': 8,
    'r': 9,
    's': 1,
    't': 2,
    'u': 3,
    'v': 4,
    'w': 5,
    'x': 6,
    'y': 7,
    'z': 8,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0
}

master_numbers = [11, 22, 33]

vowels = set('aeiou')

def reduce(value):
    while value > 9:
        value = sum(int(digit) for digit in str(value))
        if value in master_numbers:
            break
    return value

def num_sum(value):
    # print(f"Calculating num_sum for: {value}")
    value = str(value)
    # print(f"Value as string: {value}")
    result = sum(char_map.get(char, 0) for char in value)
    # print(f"Result of num_sum for {value} is: {result}")
    return result

def extract_vowels(string):
    vowels_in_string = [char for char in string if char in vowels]
    return ''.join(vowels_in_string)

def extract_consonants(string):
    consonants_in_string = [char for char in string if char not in vowels and char.isalpha()]
    return ''.join(consonants_in_string)

def remove_zeros(value):
    return int(str(value).replace('0', ''))

# sheet 1
def name_number(name, surname):
    name_value = num_sum(name)
    surname_value = num_sum(surname)

    res_name_value = reduce(name_value)
    res_surname_value = reduce(surname_value)

    print(f"Name Value from '{name}' is: {name_value}|{res_name_value}")
    print(f"Surname Value from '{surname}' is: {surname_value}|{res_surname_value}")

    return res_name_value, res_surname_value

def life_path_number(dob_day, dob_month, dob_year):
    # print(f"{dob_day} {dob_month} {dob_year}")
    sum_day = num_sum(dob_day)
    sum_month = num_sum(dob_month)
    sum_year = num_sum(dob_year)

    # print(f"{sum_day} {sum_month} {sum_year}")

    total = sum_day + sum_month + sum_year
    res = reduce(total)
    
    print(f"Life Path Number from {dob_day}/{dob_month}/{dob_year} is: {total}|{res}")
    return res

def attitude_number(dob_day, dob_month):
    total = dob_day + dob_month
    res = reduce(total)
    print(f"Attitude Number from {dob_day}/{dob_month} is: {total}|{res}")
    return res

def personal_year_number(dob_day, dob_month):
    current_year = datetime.now().year
    year = remove_zeros(current_year)
    total = num_sum(dob_day) + num_sum(dob_month) + num_sum(year)
    res = reduce(total)
    print(f"Personal Year Number from {dob_day}/{dob_month}/{current_year} is: {total}|{res}")
    return res

def challenge_numbers(dob_day, dob_month, dob_year):
    reduced_day = reduce(num_sum(dob_day))
    reduced_month = reduce(num_sum(dob_month))
    reduced_year = reduce(num_sum(dob_year))
    first = abs(reduced_month - reduced_day)
    second = abs(reduced_day - reduced_year)
    third = abs(first - second)
    fourth = abs(reduced_month - reduced_year)
    print(f"Challenge Number from {dob_day}/{dob_month}/{dob_year} is: {first}|{second}|{third}|{fourth}")
    return first, second, third, fourth

def pinnacle_numbers(dob_day, dob_month, dob_year):
    reduced_day = reduce(num_sum(dob_day))
    reduced_month = reduce(num_sum(dob_month))
    reduced_year = reduce(num_sum(dob_year))

    first = num_sum(reduced_day + reduced_month)
    second = num_sum(reduced_day + reduced_year)
    third = num_sum(first + second)
    fourth = num_sum(reduced_month + reduced_year)
    print(f"Pinnacle Number from {dob_day}/{dob_month}/{dob_year} is: {first}|{second}|{third}|{fourth}")
    return first, second, third, fourth


def destiny_number(value_1, value_2):
    total = value_1 + value_2
    res = reduce(total)
    print(f"Destiny Number from {value_1} and {value_2} is: {total}|{res}")
    return res

def heart_number(name):
    vowels_in_name = extract_vowels(name)
    total = num_sum(vowels_in_name)
    res = reduce(total)
    print(f"Heart Number from '{name}' is: {total}|{res}")
    return res

def personality_number(name):
    consonants_in_name = extract_consonants(name)
    total = num_sum(consonants_in_name)
    res = reduce(total)
    print(f"Personality Number from '{name}' is: {total}|{res}")
    return res

def might_number(life_path, destiny_number):
    total = life_path + destiny_number
    res = reduce(total)
    print(f"Might Number from {life_path} and {destiny_number} is: {total}|{res}")
    return res

def karmic_line(name, surname):
    full_name = name + surname
    # conver to numbers
    numbers = [char_map.get(char, 0) for char in full_name]
    
    # count occurrences of each number
    count = {i: numbers.count(i) for i in range(1, 10)}
    print(f"Karmic Line: {count}")
    
    # highest count is the karmic talent
    max_count = max(count.values())
    karmic_talents = [num for num, cnt in count.items() if cnt == max_count]
    # print(f"Karmic Talents: {karmic_talents} with count: {max_count}")    
    print(f"Karmic Talent: {karmic_talents[0]}") 
    
    # numbers that are missing are the karmic lessons
    karmic_lessons = [num for num, cnt in count.items() if cnt == 0]
    karmic_lessons_sum = sum(karmic_lessons)
    karmic_lessons_reduced = reduce(karmic_lessons_sum)
    print(f"Karmic Lessons: {karmic_lessons}: {karmic_lessons_sum} | {karmic_lessons_reduced}")
    
    # mentos (sum of 1 and 8)
    print(f"Mentos: {count[1] + count[8]}")
    
    # physis (sum of 4 and 5
    print(f"Physis: {count[4] + count[5]}")
    
    # emotion (sum of 2, 3 and 6)
    print(f"Emotion: {count[2] + count[3] + count[6]}")
    
    # intuition (sum of 7 and 9)
    print(f"Intuition: {count[7] + count[9]}")
    
    return count

def calculate_sheet_one(name, surname, dob_day, dob_month, dob_year):

    life_path = life_path_number(dob_day, dob_month, dob_year)
    attitude = attitude_number(dob_day, dob_month)
    personal_year = personal_year_number(dob_day, dob_month)
    challenge = challenge_numbers(dob_day, dob_month, dob_year)
    pinnacle = pinnacle_numbers(dob_day, dob_month, dob_year)

    name_value, surname_value = name_number(name, surname)
    destiny = destiny_number(name_value, surname_value)
    heart = heart_number(name + surname)
    personality = personality_number(name + surname)
    might = might_number(life_path, destiny)
    karmic_line(name, surname)

def main():
    name = "ILONA"
    surname = "PERMADINGER"
    dob_day = 22
    dob_month = 9
    dob_year = 1983

    # Convert to lowercase and remove spaces
    name = name.replace(" ", "").lower()
    surname = surname.replace(" ", "").lower()

    calculate_sheet_one(name, surname, dob_day, dob_month, dob_year)

if __name__ == "__main__":
    main()
