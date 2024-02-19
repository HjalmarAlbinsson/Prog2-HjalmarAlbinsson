input_string, correct_lst, new_string =  input("Enter numbers: ").split(" "), [1, 1, 2, 2, 2, 8], ""
for idx, x in enumerate(input_string):
    new_string += f"{correct_lst[idx]-int(input_string[idx])} "
print(new_string)

