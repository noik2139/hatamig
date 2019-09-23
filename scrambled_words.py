def file2text(file_inn):
    text_out = ''
    for word in file_inn:
        text_out += word
    return text_out


def file_read(description):
    file_name = input(description)
    file = open(file_name, "r")
    return file


def new_line2space(text_inn):
    text_out = ''
    for letter in text_inn:
        if letter == "\n":
            text_out += " "
        else:
            text_out += letter
    return text_out

def mix_letters(word_inn):
    word = word_inn.strip()
    f_letter = word[0]
    l_letter = word[-1]
    word_out = ''
    c = 0
    
    #skilgreinir miðju á orði
    word_center = ''
    for i in range(len(word)):
        if i != 0 and i

    #ruglar í miðju
    word_center_mix = ''
    word_half_2
    word_half_1
    for i in range(len(word_center)):
        if i%2 == 1:
            word_half_1 += word[i]
        else:
            word_half_2 += word[i]
        
    word_out = f_letter+word_center_mix+l_letter
    return word_out
    
    
    

    




file = file_read("enter name of file: ")
text = file2text(file)
text = new_line2space(text)

text_lok = ''
word = ""
for letter in text:
    if letter == " " or letter == "." or letter == ",":
        word = mix_letters(word)
        text_lok += word + " "
        word = ""
        
    word += letter





print(text_lok)

