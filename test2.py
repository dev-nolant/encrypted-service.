import convertName as cv

untapped_list = cv.pcallc("Digital")

tapped_list_vb1 = untapped_list[1].split(" ")
string = []
for n in tapped_list_vb1:
    print(n)
    letter_cc = int(n) - int(untapped_list[2])
    string.append(chr(letter_cc))
print(string)