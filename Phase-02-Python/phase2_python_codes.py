# =====================================================
# PHASE 2 - PYTHON FOR BIOINFORMATICS
# =====================================================

# =====================================================
# 1. HELLO WORLD
# =====================================================

print("Hello Bioinformatics")


# =====================================================
# 2. VARIABLES
# =====================================================

dna = "ATGCGTAA"

gene = "BRCA1"

length = 100

gc = 56.7

is_gene = True

print(dna)
print(gene)
print(length)
print(gc)
print(is_gene)


# =====================================================
# 3. DATA TYPES
# =====================================================

print(type(dna))
print(type(length))
print(type(gc))
print(type(is_gene))


# =====================================================
# 4. BASIC STRING OPERATIONS
# =====================================================

dna = "ATGCGTAA"

print(dna)

print(len(dna))

print(dna.upper())

print(dna.lower())


# =====================================================
# 5. STRING INDEXING
# =====================================================

print(dna[0])
print(dna[1])
print(dna[2])

print(dna[-1])

print(dna[-2])


# =====================================================
# 6. STRING SLICING
# =====================================================

print(dna[0:3])

print(dna[3:6])

print(dna[2:7])

print(dna[:4])

print(dna[4:])

print(dna[::-1])


# =====================================================
# 7. COUNTING NUCLEOTIDES
# =====================================================

print("A =", dna.count("A"))
print("T =", dna.count("T"))
print("G =", dna.count("G"))
print("C =", dna.count("C"))


# =====================================================
# 8. MEMBERSHIP TESTING
# =====================================================

print("ATG" in dna)

print("AAA" in dna)

print("CGT" in dna)


# =====================================================
# 9. USER INPUT
# =====================================================

user_dna = input("Enter DNA sequence: ")

print("You entered:", user_dna)

print("Length =", len(user_dna))


# =====================================================
# 10. ARITHMETIC OPERATIONS
# =====================================================

a = 10
b = 3

print(a + b)

print(a - b)

print(a * b)

print(a / b)

print(a % b)

print(a ** b)


# =====================================================
# 11. COMPARISON OPERATORS
# =====================================================

print(10 > 5)

print(10 < 5)

print(10 == 10)

print(10 != 10)

print(10 >= 5)

print(10 <= 5)


# =====================================================
# 12. IF STATEMENTS
# =====================================================

dna = "ATGCGTAA"

if len(dna) > 5:
    print("Long sequence")


# =====================================================
# 13. IF ELSE
# =====================================================

if len(dna) > 10:
    print("Long sequence")
else:
    print("Short sequence")


# =====================================================
# 14. IF ELIF ELSE
# =====================================================

length = len(dna)

if length < 5:
    print("Very Short")

elif length < 10:
    print("Medium")

else:
    print("Long")


# =====================================================
# 15. FOR LOOP
# =====================================================

for base in dna:
    print(base)


# =====================================================
# 16. COUNT A USING LOOP
# =====================================================

count_A = 0

for base in dna:

    if base == "A":
        count_A += 1

print(count_A)


# =====================================================
# 17. COUNT ALL NUCLEOTIDES USING LOOP
# =====================================================

count_A = 0
count_T = 0
count_G = 0
count_C = 0

for base in dna:

    if base == "A":
        count_A += 1

    elif base == "T":
        count_T += 1

    elif base == "G":
        count_G += 1

    elif base == "C":
        count_C += 1

print("A =", count_A)
print("T =", count_T)
print("G =", count_G)
print("C =", count_C)


# =====================================================
# 18. RANGE FUNCTION
# =====================================================

for i in range(5):
    print(i)


# =====================================================
# 19. LOOP THROUGH INDEXES
# =====================================================

for i in range(len(dna)):
    print(i, dna[i])


# =====================================================
# 20. LISTS
# =====================================================

genes = [
    "BRCA1",
    "TP53",
    "EGFR",
    "MYC"
]

print(genes)

print(genes[0])

print(genes[1])


# =====================================================
# 21. LOOP THROUGH LIST
# =====================================================

for gene in genes:
    print(gene)


# =====================================================
# 22. APPEND TO LIST
# =====================================================

genes.append("KRAS")

print(genes)


# =====================================================
# 23. LIST LENGTH
# =====================================================

print(len(genes))


# =====================================================
# 24. DICTIONARIES
# =====================================================

codon_table = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "GCU": "Alanine",
    "GAA": "Glutamate"
}

print(codon_table)


# =====================================================
# 25. ACCESS DICTIONARY VALUES
# =====================================================

print(codon_table["AUG"])

print(codon_table["GAA"])


# =====================================================
# 26. LOOP THROUGH DICTIONARY
# =====================================================

for codon in codon_table:
    print(codon, codon_table[codon])


# =====================================================
# 27. FUNCTIONS
# =====================================================

def greet():

    print("Welcome to Bioinformatics")


greet()


# =====================================================
# 28. FUNCTION WITH ARGUMENT
# =====================================================

def show_gene(gene):

    print("Gene:", gene)


show_gene("TP53")


# =====================================================
# 29. FUNCTION WITH RETURN
# =====================================================

def square(x):

    return x * x


result = square(5)

print(result)


# =====================================================
# 30. GC CONTENT
# =====================================================

dna = "ATGCGTAA"

gc_count = dna.count("G") + dna.count("C")

gc_percent = gc_count / len(dna) * 100

print(gc_percent)


# =====================================================
# 31. GC CONTENT FUNCTION
# =====================================================

def gc_content(seq):

    gc = seq.count("G") + seq.count("C")

    return gc / len(seq) * 100


print(gc_content("ATGCGTAA"))


# =====================================================
# 32. START CODON DETECTION
# =====================================================

dna = "ATGAAACCCGGG"

if "ATG" in dna:
    print("Start codon found")
else:
    print("No start codon")


# =====================================================
# 33. STOP CODON DETECTION
# =====================================================

if "TAA" in dna or "TAG" in dna or "TGA" in dna:
    print("Stop codon found")
else:
    print("No stop codon")


# =====================================================
# 34. CODON SPLITTING
# =====================================================

dna = "ATGAAACCCGGGTAA"

for i in range(0, len(dna), 3):

    print(dna[i:i+3])


# =====================================================
# 35. DNA VALIDATION
# =====================================================

dna = "ATGCGTAA"

valid = True

for base in dna:

    if base not in "ATGC":
        valid = False

if valid:
    print("Valid DNA Sequence")

else:
    print("Invalid DNA Sequence")


# =====================================================
# 36. SIMPLE DNA TRANSLATION
# =====================================================

codons = {
    "ATG": "M",
    "TTT": "F",
    "GAA": "E",
    "GCT": "A"
}

dna = "ATGTTTGAA"

for i in range(0, len(dna), 3):

    codon = dna[i:i+3]

    if codon in codons:
        print(codons[codon])


# =====================================================
# 37. MINI PROJECT
# COMPLETE DNA ANALYZER
# =====================================================

dna = input("Enter DNA Sequence: ")

print("\nDNA ANALYSIS REPORT")
print("-" * 30)

print("Sequence =", dna)

print("Length =", len(dna))

print("A =", dna.count("A"))
print("T =", dna.count("T"))
print("G =", dna.count("G"))
print("C =", dna.count("C"))

gc = dna.count("G") + dna.count("C")

gc_percent = gc / len(dna) * 100

print("GC Content =", round(gc_percent, 2), "%")

if "ATG" in dna:
    print("Start Codon Present")
else:
    print("Start Codon Absent")

print("-" * 30)
print("Analysis Complete")
