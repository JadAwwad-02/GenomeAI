encoding = {
    "00": "A",
    "01": "T",
    "10": "G",
    "11": "C"
}

reverse_encoding = {
    "A": "00",
    "T": "01",
    "G": "10",
    "C": "11"
}


def text_to_dna(text):
    dna = ""
    for char in text:
        binary = format(ord(char), '08b')
        dna += ''.join(encoding[binary[i:i+2]] for i in range(0, 8, 2))
    return dna


def dna_to_text(dna_sequence):
    result = ""
    for i in range(0, len(dna_sequence), 4):
        group = dna_sequence[i:i+4]
        if len(group) < 4:
            break
        binary = ''.join(reverse_encoding[nuc] for nuc in group)
        result += chr(int(binary, 2))
    return result


sequence = input("Input text: ")
print("DNA:", text_to_dna(sequence))

dna_input = input("Input DNA: ")
print("Text:", dna_to_text(dna_input))
