

def func():
    file = open("i_must_be_late.txt", "r")
    read_buffer = ""
    for line in file:
        read_buffer += line

    read_buffer.replace("\n", " ")

    array = read_buffer.split(" ")
    index = 0
    for word in array:
        i = 0
        for char in word:
            if not char.isalpha():
                array[index] = array[index].replace(char, "")
            i += 1
        index += 1
    print(array)


func()