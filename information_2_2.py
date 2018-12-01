import csv
import re


def func():
    file = open("i_must_be_late.txt", "r")
    read_buffer = ""
    for line in file:
        read_buffer += line

    read_buffer.replace("\n", " ")

    i = 0
    for char in read_buffer:
        if not char.isalpha() and char != "\n":
            read_buffer = read_buffer.replace(char, " ")
        i += 1

    array = read_buffer.split(" ")

    i = 0
    for word in array:
        if word == "":
            array.remove("")
            i += 0
            continue
        if word == '':
            array.remove('')
            i += 0
            continue

    file = open("text.csv", "w+")
    writer = csv.writer(file)
    # temp_word_with_n = []
    temp_line = []
    changes = False
    if file:
        for word in array:
            if word == "\n\n":
                writer.writerow("\n")
                writer.writerow("\n")
                continue
            for char in word:
                if char == "":
                    continue
                if char == "\n":
                    temp_word_with_n = word.split("\n")
                    if temp_word_with_n[0] != "":
                        temp_line.append(temp_word_with_n[0])
                    writer.writerow(temp_line)
                    temp_line.clear()
                    if temp_word_with_n[1] != "":
                        temp_line.append(temp_word_with_n[1])
                        changes = True
            if changes:
                changes = False
                continue
            else:
                if word == "\n\n":
                    continue
                temp_line.append(word)

    read_buffer = read_buffer.replace("\n\n", "\n")

    array_stats = read_buffer.split(" ")
    file_stat = open("text_statistics.csv", "w+")
    writer_stat = csv.writer(file_stat)
    temp_line = []
    vocab_letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                     'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                     'y': 0, 'z': 0}

    vocab_words = {"and": 0, "in": 0, "that": 0, "so": 0, "as": 0, "if": 0}
    changes = False
    if file:
        for word in array_stats:
            if word == "":
                continue
            for char in word:
                if char == "" or (not char.isalpha() and char != '\n'):
                    continue
                if char == "\n":
                    temp_word_with_n = word.split("\n")
                    if temp_word_with_n[0] != "":
                        temp_line.append(temp_word_with_n[0])

                    for word in temp_line:
                        if word in vocab_words:
                            vocab_words[word] += 1
                        for char in word:
                            if char in vocab_letters:
                                vocab_letters[char] += 1
                    writer_stat.writerow(["Line:"])
                    if temp_line == "came":
                        continue
                    writer_stat.writerow(temp_line)
                    writer_stat.writerow(["Letters:"])
                    for letter in vocab_letters:
                        if vocab_letters[letter] != 0:
                            temp = [letter, vocab_letters[letter]]
                            writer_stat.writerow(temp)

                    temp_line.clear()
                    for val in vocab_letters:
                        vocab_letters[val] = 0

                    if temp_word_with_n:
                        if temp_word_with_n.__len__() > 1:
                            if temp_word_with_n[1] != "":
                                temp_line.append(temp_word_with_n[1])
                                changes = True
                        if temp_word_with_n.__len__() > 2:
                            if temp_word_with_n[2] != "":
                                temp_line.append(temp_word_with_n[2])
                    temp_word_with_n.clear()
                    continue

            if changes:
                changes = False
                continue
            else:
                if word == "\n\n":
                    continue
                temp_line.append(word)

    writer_stat.writerow(["Special words:"])
    for special_letter in vocab_words:
        if vocab_words[special_letter] != 0:
            temp = [special_letter, vocab_words[special_letter]]
            writer_stat.writerow(temp)

    file_stat.close()
    file.close()


func()
