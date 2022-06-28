input_string = input('Digite alguma palavra:')

new_string = ''
count = len(input_string) - 1
while count >= 0:
    new_string = new_string + input_string[count]
    count = count - 1
    print(new_string)
