# =====================================================
# PHASE 7 : PROTEIN STRUCTURE PREDICTION
# =====================================================

# Topics Covered
#
# 1. Protein Length
# 2. Amino Acid Composition
# 3. Molecular Weight Estimation
# 4. Hydrophobic Residue Analysis
# 5. Hydrophilic Residue Analysis
# 6. Protein Domain Search Simulation
# 7. Secondary Structure Prediction (Simple)
# 8. Motif Search
# 9. Structure Validation Simulation
# 10. RMSD Interpretation
#
# =====================================================


# =====================================================
# SAMPLE PROTEIN
# =====================================================

protein = "MKWVTFISLLFLFSSAYSRGVFRRDTHKSEIAHRFKDLGE"

print("Protein Sequence:")
print(protein)

print()


# =====================================================
# 1. PROTEIN LENGTH
# =====================================================

print("===== PROTEIN LENGTH =====")

length = len(protein)

print("Length =", length)

print()


# =====================================================
# 2. AMINO ACID COMPOSITION
# =====================================================

print("===== AMINO ACID COMPOSITION =====")

for aa in sorted(set(protein)):

    print(
        aa,
        "->",
        protein.count(aa)
    )

print()


# =====================================================
# 3. MOLECULAR WEIGHT ESTIMATION
# =====================================================

print("===== MOLECULAR WEIGHT =====")

# Rough estimate

mw = length * 110

print(
    "Approx Molecular Weight =",
    mw,
    "Da"
)

print()


# =====================================================
# 4. HYDROPHOBIC RESIDUES
# =====================================================

print("===== HYDROPHOBIC RESIDUES =====")

hydrophobic = "AVLIMFWY"

count = 0

for aa in protein:

    if aa in hydrophobic:

        count += 1

print("Hydrophobic Residues =", count)

print()


# =====================================================
# 5. HYDROPHILIC RESIDUES
# =====================================================

print("===== HYDROPHILIC RESIDUES =====")

hydrophilic = "RNDQEKHST"

count = 0

for aa in protein:

    if aa in hydrophilic:

        count += 1

print("Hydrophilic Residues =", count)

print()


# =====================================================
# 6. HYDROPHOBIC PERCENTAGE
# =====================================================

print("===== HYDROPHOBIC PERCENTAGE =====")

count = 0

for aa in protein:

    if aa in hydrophobic:

        count += 1

percentage = (count / length) * 100

print(
    "Hydrophobic %",
    round(percentage, 2)
)

print()


# =====================================================
# 7. MOTIF SEARCH
# =====================================================

print("===== MOTIF SEARCH =====")

motif = "RGVF"

if motif in protein:

    print("Motif Found")

else:

    print("Motif Not Found")

print()


# =====================================================
# 8. DOMAIN SEARCH SIMULATION
# =====================================================

print("===== DOMAIN SEARCH =====")

if length > 40:

    print("Possible Multi-Domain Protein")

else:

    print("Possible Single Domain Protein")

print()


# =====================================================
# 9. SECONDARY STRUCTURE PREDICTION
# =====================================================

print("===== SIMPLE SECONDARY STRUCTURE =====")

helix_formers = "ALMEQKH"

helix_score = 0

for aa in protein:

    if aa in helix_formers:

        helix_score += 1

print(
    "Helix Forming Residues =",
    helix_score
)

print()


# =====================================================
# 10. CHARGE ANALYSIS
# =====================================================

print("===== CHARGE ANALYSIS =====")

positive = "KRH"

negative = "DE"

pos = 0
neg = 0

for aa in protein:

    if aa in positive:
        pos += 1

    if aa in negative:
        neg += 1

print("Positive Residues =", pos)

print("Negative Residues =", neg)

print()


# =====================================================
# 11. PROTEIN BACKBONE COUNT
# =====================================================

print("===== PROTEIN BACKBONE =====")

print(
    "Peptide Bonds =",
    length - 1
)

print()


# =====================================================
# 12. RMSD INTERPRETATION
# =====================================================

print("===== RMSD ANALYSIS =====")

rmsd = 1.2

if rmsd < 2:

    print("Structures Highly Similar")

elif rmsd < 5:

    print("Moderately Similar")

else:

    print("Structures Different")

print()


# =====================================================
# 13. RAMACHANDRAN CHECK
# =====================================================

print("===== RAMACHANDRAN CHECK =====")

allowed = 94

if allowed > 90:

    print("Good Quality Structure")

else:

    print("Poor Quality Structure")

print()


# =====================================================
# 14. PDB RECORD SIMULATION
# =====================================================

print("===== PDB ENTRY =====")

pdb = {

    "ID": "1CRN",

    "Protein":
    "Crambin",

    "Resolution":
    1.5
}

for key in pdb:

    print(
        key,
        ":",
        pdb[key]
    )

print()


# =====================================================
# 15. STRUCTURE PREDICTION REPORT
# =====================================================

print("===== FINAL REPORT =====")

print("Protein Length :", length)

print("Approx MW      :", mw)

print("Hydrophobic %  :", round(percentage,2))

print("PDB Example    :", pdb["ID"])

print()

# =====================================================
# END OF PHASE 7
# =====================================================
