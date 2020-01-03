def int_roman(num):
    roman_list = ["X","IX","V","IV","I"]
    num_list = [10,9,5,4,1]
    roman_str = ""
    i = 0
    while num > 0:
        for value in range(num//num_list[i]):
            roman_str += roman_list[i]
            num -= num_list[i]
        i+=1
    return roman_str
 
