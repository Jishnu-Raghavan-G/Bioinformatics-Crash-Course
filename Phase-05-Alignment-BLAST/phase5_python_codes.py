# ==========================================================
# PHASE 5 : ALIGNMENT AND BLAST
# ==========================================================

# Topics Covered
#
# 1. Sequence Comparison
# 2. Match Counting
# 3. Mismatch Counting
# 4. Alignment Score
# 5. Percent Identity
# 6. Conserved Position Detection
# 7. Gap Counting
# 8. Pairwise Alignment Display
# 9. Similarity Search (Mini BLAST)
# 10. Best Match Finder
#
# ==========================================================


# ==========================================================
# 1. SEQUENCE COMPARISON
# ==========================================================

print("\n===== SEQUENCE COMPARISON =====")

seq1 = "ATGCGT"
seq2 = "ATGAGT"

print("Sequence 1:", seq1)
print("Sequence 2:", seq2)


# ==========================================================
# 2. MATCH COUNTING
# ==========================================================

print("\n===== MATCH COUNTING =====")

matches = 0

for a, b in zip(seq1, seq2):

    if a == b:
        matches += 1

print("Matches =", matches)


# ==========================================================
# 3. MISMATCH COUNTING
# ==========================================================

print("\n===== MISMATCH COUNTING =====")

mismatches = 0

for a, b in zip(seq1, seq2):

    if a != b:
        mismatches += 1

print("Mismatches =", mismatches)


# ==========================================================
# 4. ALIGNMENT SCORE
# ==========================================================

print("\n===== ALIGNMENT SCORE =====")

score = 0

for a, b in zip(seq1, seq2):

    if a == b:
        score += 1

    else:
        score -= 1

print("Alignment Score =", score)


# ==========================================================
# 5. PERCENT IDENTITY
# ==========================================================

print("\n===== PERCENT IDENTITY =====")

identity = (matches / len(seq1)) * 100

print("Identity =", round(identity,2), "%")


# ==========================================================
# 6. CONSERVED POSITIONS
# ==========================================================

print("\n===== CONSERVED POSITIONS =====")

for i in range(len(seq1)):

    if seq1[i] == seq2[i]:

        print(
            "Position",
            i+1,
            "=",
            seq1[i]
        )


# ==========================================================
# 7. GAP COUNTING
# ==========================================================

print("\n===== GAP COUNTING =====")

seq3 = "ATG-CGT"
seq4 = "ATGACGT"

gaps = seq3.count("-")

print("Sequence 3 =", seq3)
print("Sequence 4 =", seq4)

print("Gap Count =", gaps)


# ==========================================================
# 8. SIMPLE ALIGNMENT DISPLAY
# ==========================================================

print("\n===== ALIGNMENT DISPLAY =====")

alignment = ""

for a, b in zip(seq1, seq2):

    if a == b:

        alignment += "|"

    else:

        alignment += " "

print(seq1)
print(alignment)
print(seq2)


# ==========================================================
# 9. FIND DIFFERENT POSITIONS
# ==========================================================

print("\n===== MUTATION POSITIONS =====")

for i in range(len(seq1)):

    if seq1[i] != seq2[i]:

        print(
            "Difference at Position",
            i+1,
            ":",
            seq1[i],
            "->",
            seq2[i]
        )


# ==========================================================
# 10. MINI BLAST SEARCH
# ==========================================================

print("\n===== MINI BLAST =====")

query = "ATGCGT"

database = [

    "ATGCGT",
    "ATGAGT",
    "TTGCGT",
    "CCCCCC",
    "ATGCAT"

]

for sequence in database:

    score = 0

    for a, b in zip(query, sequence):

        if a == b:
            score += 1

    print(sequence, "Score =", score)


# ==========================================================
# 11. BEST MATCH FINDER
# ==========================================================

print("\n===== BEST MATCH =====")

query = "ATGCGT"

database = [

    "ATGCGT",
    "ATGAGT",
    "TTGCGT",
    "CCCCCC",
    "ATGCAT"

]

best_score = -1
best_sequence = ""

for sequence in database:

    score = 0

    for a, b in zip(query, sequence):

        if a == b:

            score += 1

    if score > best_score:

        best_score = score

        best_sequence = sequence

print("Best Match =", best_sequence)
print("Score =", best_score)


# ==========================================================
# 12. SIMPLE E-VALUE CONCEPT
# ==========================================================

print("\n===== E-VALUE INTERPRETATION =====")

evalue = 1e-20

if evalue < 1e-5:

    print("Highly Significant Match")

else:

    print("Weak Match")


# ==========================================================
# 13. MULTIPLE SEQUENCE CONSERVATION
# ==========================================================

print("\n===== CONSERVED REGION ANALYSIS =====")

sequences = [

    "ATGCGT",
    "ATGCGT",
    "ATGAGT",
    "ATGCGA"

]

length = len(sequences[0])

for position in range(length):

    column = []

    for seq in sequences:

        column.append(seq[position])

    if len(set(column)) == 1:

        print(
            "Conserved Position:",
            position + 1,
            column[0]
        )


# ==========================================================
# 14. BLAST RESULT SUMMARY
# ==========================================================

print("\n===== BLAST SUMMARY =====")

query = "ATGCGT"

subject = "ATGAGT"

matches = 0

for a, b in zip(query, subject):

    if a == b:

        matches += 1

identity = (matches / len(query)) * 100

print("Query   :", query)
print("Subject :", subject)

print("Matches :", matches)

print("Identity:", round(identity,2), "%")


# ==========================================================
# END OF PHASE 5
# ==========================================================
