# ==========================================================
# PHASE 10 : PHYLOGENETICS
# ==========================================================

# Topics Covered
#
# 1. Species Dataset
# 2. Sequence Similarity
# 3. Percent Identity
# 4. Evolutionary Distance
# 5. Distance Matrix
# 6. Closest Species Detection
# 7. Conserved Positions
# 8. Mutation Counting
# 9. Ortholog Simulation
# 10. Paralog Simulation
# 11. Tree Representation
# 12. Bootstrap Interpretation
#
# ==========================================================


# ==========================================================
# 1. SPECIES SEQUENCES
# ==========================================================

print("\n===== SPECIES SEQUENCES =====")

species = {

    "Human" : "ATGCGTAA",

    "Chimp" : "ATGCGTAT",

    "Mouse" : "ATGAGCAA",

    "Dog"   : "TTGCGCAA"

}

for sp in species:

    print(sp, species[sp])


# ==========================================================
# 2. PERCENT IDENTITY
# ==========================================================

print("\n===== PERCENT IDENTITY =====")

seq1 = species["Human"]
seq2 = species["Chimp"]

matches = 0

for a, b in zip(seq1, seq2):

    if a == b:

        matches += 1

identity = (matches / len(seq1)) * 100

print("Human vs Chimp =", round(identity,2), "%")


# ==========================================================
# 3. EVOLUTIONARY DISTANCE
# ==========================================================

print("\n===== EVOLUTIONARY DISTANCE =====")

distance = len(seq1) - matches

print("Distance =", distance)


# ==========================================================
# 4. DISTANCE MATRIX
# ==========================================================

print("\n===== DISTANCE MATRIX =====")

species_names = list(species.keys())

for sp1 in species_names:

    row = []

    for sp2 in species_names:

        seqA = species[sp1]
        seqB = species[sp2]

        diff = 0

        for a,b in zip(seqA,seqB):

            if a != b:

                diff += 1

        row.append(diff)

    print(sp1, row)


# ==========================================================
# 5. CLOSEST SPECIES
# ==========================================================

print("\n===== CLOSEST SPECIES =====")

best_species = ""

lowest_distance = 999

human = species["Human"]

for sp in species:

    if sp == "Human":

        continue

    diff = 0

    for a,b in zip(human,species[sp]):

        if a != b:

            diff += 1

    if diff < lowest_distance:

        lowest_distance = diff

        best_species = sp

print("Closest To Human =", best_species)


# ==========================================================
# 6. MUTATION COUNT
# ==========================================================

print("\n===== MUTATION COUNT =====")

human = species["Human"]
chimp = species["Chimp"]

mutations = 0

for a,b in zip(human,chimp):

    if a != b:

        mutations += 1

print("Mutations =", mutations)


# ==========================================================
# 7. CONSERVED POSITIONS
# ==========================================================

print("\n===== CONSERVED POSITIONS =====")

all_sequences = list(species.values())

length = len(all_sequences[0])

for pos in range(length):

    bases = []

    for seq in all_sequences:

        bases.append(seq[pos])

    if len(set(bases)) == 1:

        print(
            "Position",
            pos+1,
            "Conserved:",
            bases[0]
        )


# ==========================================================
# 8. ORTHOLOG EXAMPLE
# ==========================================================

print("\n===== ORTHOLOGS =====")

orthologs = {

    "Human_TP53":
    "Mouse_TP53"

}

for gene in orthologs:

    print(
        gene,
        "<->",
        orthologs[gene]
    )


# ==========================================================
# 9. PARALOG EXAMPLE
# ==========================================================

print("\n===== PARALOGS =====")

paralogs = [

    "Hemoglobin Alpha",

    "Hemoglobin Beta"

]

for gene in paralogs:

    print(gene)


# ==========================================================
# 10. SIMPLE TREE
# ==========================================================

print("\n===== PHYLOGENETIC TREE =====")

print("""
          Human
         /
     ----
         \\
          Chimp

             \\
              Mouse
""")

# ==========================================================
# 11. BOOTSTRAP ANALYSIS
# ==========================================================

print("\n===== BOOTSTRAP =====")

bootstrap = 95

if bootstrap > 90:

    print("Strong Support")

elif bootstrap > 70:

    print("Moderate Support")

else:

    print("Weak Support")


# ==========================================================
# 12. CLADE EXAMPLE
# ==========================================================

print("\n===== CLADE =====")

clade = [

    "Human",

    "Chimp",

    "Gorilla"

]

print("Clade Members:")

for member in clade:

    print(member)


# ==========================================================
# 13. OUTGROUP
# ==========================================================

print("\n===== OUTGROUP =====")

outgroup = "Fish"

print("Outgroup =", outgroup)


# ==========================================================
# 14. MOLECULAR EVOLUTION
# ==========================================================

print("\n===== MOLECULAR EVOLUTION =====")

ancestor = "ATGCGTAA"

modern = "ATGAGCAA"

changes = 0

for a,b in zip(ancestor,modern):

    if a != b:

        changes += 1

print("Evolutionary Changes =", changes)


# ==========================================================
# 15. FINAL REPORT
# ==========================================================

print("\n===== PHYLOGENETIC REPORT =====")

print("Species Analysed:",
      len(species))

print("Closest To Human:",
      best_species)

print("Human-Chimp Identity:",
      round(identity,2),
      "%")

print("Bootstrap:",
      bootstrap,
      "%")


# ==========================================================
# 16. EXPORT REPORT
# ==========================================================

with open(
    "phylogenetic_report.txt",
    "w"
) as file:

    file.write(
        "PHYLOGENETIC ANALYSIS REPORT\n"
    )

    file.write(
        "Closest Species: "
        + best_species
        + "\n"
    )

    file.write(
        "Identity: "
        + str(round(identity,2))
        + "%\n"
    )

print("\nReport Saved Successfully")


# ==========================================================
# END OF PHASE 10
# ==========================================================
