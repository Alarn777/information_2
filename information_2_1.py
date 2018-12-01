import base64
import codecs


def func():
    file = open("i_must_be_late.bin", "r")
    string = ""

    print("Raw file:")
    for line in file:
        string += line
        print(line)

    decoded_string = str(base64.standard_b64decode(string))
    rot_13_decoded_string = codecs.getencoder("rot-13")(decoded_string)[0]
    rot_13_decoded_string = rot_13_decoded_string.replace("\\a", "\n")
    rot_13_decoded_string = rot_13_decoded_string.replace("\\", "")
    inverted_string = ""

    while rot_13_decoded_string != "":
        inverted_string += rot_13_decoded_string[len(rot_13_decoded_string) - 1]
        rot_13_decoded_string = rot_13_decoded_string[:-1]
    print("\n")
    print("Decoded:")
    print(inverted_string)

    inverted_string = inverted_string.replace("\\", "")
    out_file = open("i_must_be_late.txt", "w+")
    if out_file:
        out_file.write(inverted_string)


func()


