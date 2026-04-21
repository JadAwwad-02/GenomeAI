# 02 – DNA Storage Simulation 🧬

This project is part of my **GenomeAI** learning journey where I explore bioinformatics concepts using Python. This module focuses on understanding how digital data can be encoded into DNA sequences.

## Overview

DNA data storage is an emerging field where binary data is converted into nucleotide sequences (A, T, G, C). In this exercise, I implemented a simple encoding algorithm that converts text into a simulated DNA sequence.

## Encoding Method

The program uses a 2-bit encoding scheme:

00 → A  
01 → T  
10 → G  
11 → C  

## Algorithm Process

The script performs the following steps:

1. Takes text input from the user
2. Converts each character into its ASCII value
3. Converts the ASCII value into 8-bit binary
4. Splits the binary into 2-bit segments
5. Maps each segment into a DNA base
6. Outputs the final DNA sequence

## Example

Input:
JAD

Binary representation:
J → 01001010  
A → 01000001  
D → 01000100  

DNA sequence output:
TAGGTAATTATA

## Learning Goals

This exercise helped me practice:

- Python programming fundamentals
- Working with binary data
- Understanding data encoding concepts
- Introduction to DNA data storage ideas
- Computational biology basics

## Notes

This is a simplified computational model created for learning purposes. It does not represent real laboratory DNA synthesis or biological storage systems.

## How to Run

```bash
py dna_storage.py
```

Follow the prompts to encode text to DNA or decode DNA back to text.

## Author

Jad Awwad