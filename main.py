#Задача №1
def get_sum(num1, num2):
    return num1 + num2

#Задача №2
def count_capital_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count

#Задача №3
def decode_string(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        char_count[char] = char_count.get(char, 0) + 1
    

    result = []
    for char in text_lower:
        if char_count[char] == 1:
            result.append('(')
        else:
            result.append(')')
    
    return ''.join(result)

#Задача №4
def get_odd_count(numbers):
    count = 0
    for digit_char in numbers:
        if int(digit_char) % 2 == 0 and int(digit_char) != 0:
            count += 1
    return count

#Задача №5
def check_access(has_keycard, has_fingerprint, is_alarm, is_daylight):
    if is_alarm:
        return False
    
    if has_fingerprint:
        return True
    
    if has_keycard and is_daylight:
        return True

    return False