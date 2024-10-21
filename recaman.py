length = int(input("Input length of Recaman Sequence: "))
sequence = [0]
for i in range(1, length):
        if sequence[i - 1] - i > 0 and (sequence[i - 1] - i) not in sequence:
            sequence.append(sequence[i - 1] - i)
        else:
            sequence.append(sequence[i - 1] + i)
print(sequence) 
