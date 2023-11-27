def increment_string(strng):
    if not strng:
        return '1'
    
    # Проверяем, заканчивается ли строка числом
    if strng[-1].isdigit():
        # Если да, то увеличиваем число на 1
        index = len(strng) - 1
        while index >= 0 and strng[index].isdigit():
            index -= 1
        num_str = strng[index+1:]
        incremented_num = str(int(num_str) + 1)
        
        # Обрабатываем случай, когда число увеличивается в длине
        if len(incremented_num) > len(num_str):
            return strng[:index+1] + incremented_num
        else:
            return strng[:index+1] + incremented_num.zfill(len(num_str))
    else:
        # Если строка не заканчивается числом, добавляем цифру 1 на конец
        return strng + '1'
