# =====================================
# PHASE 3 : DNA SEQUENCE OPERATIONS
# =====================================

dna = "ATGCGTAAGCTAGCGTATCG"

print("DNA Sequence:", dna)

# =====================================
# 1. SEQUENCE LENGTH
# =====================================

print("\n--- Sequence Length ---")
print("Length =", len(dna))

# =====================================
# 2. NUCLEOTIDE COUNT
# =====================================

print("\n--- Nucleotide Count ---")

print("A =", dna.count("A"))
print("T =", dna.count("T"))
print("G =", dna.count("G"))
print("C =", dna.count("C"))

# =====================================
# 3. GC CONTENT
# =====================================

print("\n--- GC Content ---")

gc = dna.count("G") + dna.count("C")

gc_percent = (gc / len(dna)) * 100

print("GC Content =", round(gc_percent, 2), "%")

# =====================================
# 4. COMPLEMENTARY DNA
# =====================================

print("\n--- Complement Sequence ---")

complement_dict = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

complement = ""

for base in dna:
    complement += complement_dict[base]

print("Complement =", complement)

# =====================================
# 5. REVERSE COMPLEMENT
# =====================================

print("\n--- Reverse Complement ---")

reverse_complement = complement[::-1]

print("Reverse Complement =", reverse_complement)

# =====================================
# 6. TRANSCRIPTION
# =====================================

print("\n--- Transcription ---")

rna = dna.replace("T", "U")

print("RNA =", rna)

# =====================================
# 7. START AND STOP CODON CHECK
# =====================================

print("\n--- Codon Check ---")

start_codon = "ATG"

stop_codons = ["TAA", "TAG", "TGA"]

if dna.startswith(start_codon):
    print("Start codon found")
else:
    print("Start codon not found")

for codon in stop_codons:
    if codon in dna:
        print("Stop codon found:", codon)

# =====================================
# 8. CODON SPLITTING
# =====================================

print("\n--- Codons ---")

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]

    if len(codon) == 3:
        print(codon)

# =====================================
# 9. SIMPLE MUTATION
# =====================================

print("\n--- Mutation Example ---")

mutated = dna.replace("A", "G", 1)

print("Original =", dna)
print("Mutated  =", mutated)

# =====================================
# 10. PALINDROME CHECK
# =====================================

print("\n--- Palindrome Check ---")

if dna == reverse_complement:
    print("Palindrome Sequence")
else:
    print("Not Palindrome")

# =====================================
# 11. NUCLEOTIDE PERCENTAGE
# =====================================

print("\n--- Base Percentage ---")

length = len(dna)

print("A % =", round(dna.count("A")/length*100,2))
print("T % =", round(dna.count("T")/length*100,2))
print("G % =", round(dna.count("G")/length*100,2))
print("C % =", round(dna.count("C")/length*100,2))

# =====================================
# 12. SIMPLE ORF DETECTION
# =====================================

print("\n--- ORF Detection ---")

for i in range(len(dna)-2):

    codon = dna[i:i+3]

    if codon == "ATG":

        print("Possible ORF starts at position:", i)

# =====================================
# END OF PHASE 3
# =====================================
