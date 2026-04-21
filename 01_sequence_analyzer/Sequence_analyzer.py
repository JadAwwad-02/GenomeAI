def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    total = len(sequence)
    return (g + c) / total * 100

def at_per(seq):
    a = seq.count("A")
    t = seq.count("T")
    total = len(seq)
    return (a + t) / total * 100

def analyze_sequence(seq):
    gc = gc_content(seq)
    at = at_per(seq)
    print(f"Sequence length: {len(seq)}")
    print(f"GC content: {gc:.2f}%")
    print(f"AT content: {at:.2f}%")

sequence = input("Enter DNA sequence: ")
analyze_sequence(sequence)
