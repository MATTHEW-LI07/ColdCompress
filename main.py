'''Your new cellphone plan charges you for every character you send from your phone. Since you
tend to send sequences of symbols in your messages, you have come up with the following compression technique: for each symbol, write down the number of times it appears consecutively,
followed by the symbol itself. This compression technique is called run-length encoding.
More formally, a block is a substring of identical symbols that is as long as possible. A block will
be represented in compressed form as the length of the block followed by the symbol in that block.
The encoding of a string is the representation of each block in the string in the order in which they
appear in the string.
Given a sequence of characters, write a program to encode them in this format.
Input Specification
The first line of input contains the number N, which is the number of lines that follow. The next
N lines will contain at least one and at most 80 characters, none of which are spaces.
'''



N = int(input())

for i in range(N):
    line = input()
    encoded = ""
    count = 1
    for j in range(1, len(line)):
        if line[j] == line[j - 1]:
            count += 1
        else:
            encoded += str(count) + " " + line[j - 1] + " "
            count = 1
    encoded += str(count) + " " + line[-1] + " "
    print(encoded)