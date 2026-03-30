encoding = {
    "00": "A",
    "01": "T",
    "10": "G",
    "11": "C"
}

def text_to_dna(text):
    dna = ""
    
    for char in text:
        binary = format(ord(char), '08b')
        dna += ''.join(encoding[binary[i:i+2]] for i in range(0,8,2))
    
    return dna


sequence = input("Input text: ")

print("DNA:", text_to_dna(sequence))