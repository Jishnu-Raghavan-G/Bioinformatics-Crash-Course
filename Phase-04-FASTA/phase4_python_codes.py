# ==========================================
# PHASE 4 : FASTA FILE HANDLING
# ==========================================

# Topics Covered:
# 1. Read FASTA File
# 2. Print Headers
# 3. Print Sequences
# 4. Ignore Headers
# 5. Build Complete Sequence
# 6. Sequence Length
# 7. Nucleotide Count
# 8. GC Content
# 9. Multi-FASTA Parsing
# 10. Save Sequence to File
# ==========================================


# ==========================================
# 1. READ FASTA FILE
# ==========================================

print("\n===== READ FASTA FILE =====")

with open("sample.fasta") as file:

    for line in file:

        print(line.strip())


# ==========================================
# 2. PRINT ONLY HEADERS
# ==========================================

print("\n===== FASTA HEADERS =====")

with open("sample.fasta") as file:

    for line in file:

        line = line.strip()

        if line.startswith(">"):

            print(line)


# ==========================================
# 3. PRINT ONLY SEQUENCES
# ==========================================

print("\n===== FASTA SEQUENCES =====")

with open("sample.fasta") as file:

    for line in file:

        line = line.strip()

        if not line.startswith(">"):

            print(line)


# ==========================================
# 4. BUILD COMPLETE SEQUENCE
# ==========================================

print("\n===== COMPLETE SEQUENCE =====")

sequence = ""

with open("sample.fasta") as file:

    for line in file:

        line = line.strip()

        if not line.startswith(">"):

            sequence += line

print(sequence)


# ==========================================
# 5. SEQUENCE LENGTH
# ==========================================

print("\n===== SEQUENCE LENGTH =====")

print("Length =", len(sequence))


# ==========================================
# 6. NUCLEOTIDE COUNT
# ==========================================

print("\n===== NUCLEOTIDE COUNT =====")

print("A =", sequence.count("A"))
print("T =", sequence.count("T"))
print("G =", sequence.count("G"))
print("C =", sequence.count("C"))


# ==========================================
# 7. GC CONTENT
# ==========================================

print("\n===== GC CONTENT =====")

gc = sequence.count("G") + sequence.count("C")

gc_percent = (gc / len(sequence)) * 100

print("GC Content =", round(gc_percent, 2), "%")


# ==========================================
# 8. FASTA HEADER COUNT
# ==========================================

print("\n===== NUMBER OF SEQUENCES =====")

count = 0

with open("sample.fasta") as file:

    for line in file:

        if line.startswith(">"):

            count += 1

print("Total Sequences =", count)


# ==========================================
# 9. MULTI-FASTA PARSING
# ==========================================

print("\n===== MULTI-FASTA PARSING =====")

header = ""
sequence = ""

with open("sample.fasta") as file:

    for line in file:

        line = line.strip()

        if line.startswith(">"):

            if sequence:

                print(header)
                print(sequence)
                print()

            header = line
            sequence = ""

        else:

            sequence += line

if sequence:

    print(header)
    print(sequence)


# ==========================================
# 10. SAVE SEQUENCE TO NEW FILE
# ==========================================

print("\n===== SAVE OUTPUT =====")

sequence = ""

with open("sample.fasta") as file:

    for line in file:

        line = line.strip()

        if not line.startswith(">"):

            sequence += line

with open("output_sequence.txt", "w") as out:

    out.write(sequence)

print("Sequence Saved Successfully")


# ==========================================
# 11. FIND MOTIF
# ==========================================

print("\n===== MOTIF SEARCH =====")

motif = "ATG"

if motif in sequence:

    print("Motif Found")

else:

    print("Motif Not Found")


# ==========================================
# 12. RNA TRANSCRIPTION
# ==========================================

print("\n===== DNA TO RNA =====")

rna = sequence.replace("T", "U")

print(rna)


# ==========================================
# 13. REVERSE COMPLEMENT
# ==========================================

print("\n===== REVERSE COMPLEMENT =====")

complement = {
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G"
}

reverse_complement = ""

for base in reversed(sequence):

    reverse_complement += complement[base]

print(reverse_complement)


# ==========================================
# 14. BASE PERCENTAGES
# ==========================================

print("\n===== BASE PERCENTAGES =====")

length = len(sequence)

print("A % =", round(sequence.count("A")/length*100,2))
print("T % =", round(sequence.count("T")/length*100,2))
print("G % =", round(sequence.count("G")/length*100,2))
print("C % =", round(sequence.count("C")/length*100,2))


# ==========================================
# END OF PHASE 4
# ==========================================
