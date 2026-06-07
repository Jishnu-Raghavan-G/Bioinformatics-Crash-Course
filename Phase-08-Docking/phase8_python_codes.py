phase8_python_codes.py
# ==========================================================
# PHASE 8 : MOLECULAR DOCKING
# ==========================================================

# Topics Covered
#
# 1. Ligand Database
# 2. Target Protein
# 3. Docking Score Analysis
# 4. Best Ligand Selection
# 5. Binding Affinity Ranking
# 6. Virtual Screening
# 7. Hydrogen Bond Analysis
# 8. Binding Energy Analysis
# 9. Drug Candidate Selection
# 10. Docking Report Generation
#
# ==========================================================


# ==========================================================
# 1. TARGET PROTEIN
# ==========================================================

print("\n===== TARGET PROTEIN =====")

target_protein = "EGFR"

print("Target Protein =", target_protein)


# ==========================================================
# 2. LIGAND DATABASE
# ==========================================================

print("\n===== LIGAND DATABASE =====")

ligands = {

    "Ligand_A": -8.4,

    "Ligand_B": -6.1,

    "Ligand_C": -9.3,

    "Ligand_D": -4.8,

    "Ligand_E": -7.5

}

for ligand in ligands:

    print(
        ligand,
        "Docking Score:",
        ligands[ligand]
    )


# ==========================================================
# 3. BEST LIGAND
# ==========================================================

print("\n===== BEST LIGAND =====")

best_ligand = min(
    ligands,
    key=ligands.get
)

print("Best Ligand =", best_ligand)

print(
    "Score =",
    ligands[best_ligand]
)


# ==========================================================
# 4. WEAKEST LIGAND
# ==========================================================

print("\n===== WEAKEST LIGAND =====")

worst_ligand = max(
    ligands,
    key=ligands.get
)

print("Weakest Ligand =", worst_ligand)

print(
    "Score =",
    ligands[worst_ligand]
)


# ==========================================================
# 5. VIRTUAL SCREENING
# ==========================================================

print("\n===== VIRTUAL SCREENING =====")

threshold = -7.0

for ligand in ligands:

    if ligands[ligand] <= threshold:

        print(
            ligand,
            "Passed Screening"
        )


# ==========================================================
# 6. BINDING AFFINITY CLASSIFICATION
# ==========================================================

print("\n===== BINDING AFFINITY =====")

for ligand in ligands:

    score = ligands[ligand]

    if score <= -8:

        status = "Strong"

    elif score <= -6:

        status = "Moderate"

    else:

        status = "Weak"

    print(
        ligand,
        "->",
        status
    )


# ==========================================================
# 7. SORT LIGANDS
# ==========================================================

print("\n===== RANKING =====")

ranking = sorted(
    ligands.items(),
    key=lambda x: x[1]
)

for rank, data in enumerate(ranking, start=1):

    print(
        rank,
        data[0],
        data[1]
    )


# ==========================================================
# 8. HYDROGEN BOND ANALYSIS
# ==========================================================

print("\n===== HYDROGEN BONDS =====")

hydrogen_bonds = {

    "Ligand_A": 3,

    "Ligand_B": 1,

    "Ligand_C": 5,

    "Ligand_D": 0,

    "Ligand_E": 2

}

for ligand in hydrogen_bonds:

    print(
        ligand,
        ":",
        hydrogen_bonds[ligand],
        "Hydrogen Bonds"
    )


# ==========================================================
# 9. BEST HYDROGEN BOND FORMER
# ==========================================================

print("\n===== BEST H-BOND FORMER =====")

best_hbond = max(
    hydrogen_bonds,
    key=hydrogen_bonds.get
)

print(best_hbond)

print(
    hydrogen_bonds[best_hbond],
    "Hydrogen Bonds"
)


# ==========================================================
# 10. COMBINED DOCKING ANALYSIS
# ==========================================================

print("\n===== COMBINED ANALYSIS =====")

for ligand in ligands:

    print(
        ligand,
        "| Score:",
        ligands[ligand],
        "| H-Bonds:",
        hydrogen_bonds[ligand]
    )


# ==========================================================
# 11. DRUG CANDIDATE SELECTION
# ==========================================================

print("\n===== DRUG CANDIDATES =====")

for ligand in ligands:

    if (
        ligands[ligand] <= -7
        and
        hydrogen_bonds[ligand] >= 2
    ):

        print(
            ligand,
            "Selected"
        )


# ==========================================================
# 12. BINDING ENERGY INTERPRETATION
# ==========================================================

print("\n===== ENERGY ANALYSIS =====")

energy = -9.1

if energy <= -8:

    print("Excellent Binding")

elif energy <= -6:

    print("Moderate Binding")

else:

    print("Weak Binding")


# ==========================================================
# 13. ACTIVE SITE RESIDUES
# ==========================================================

print("\n===== ACTIVE SITE =====")

active_site = [

    "ASP45",
    "LYS67",
    "SER89",
    "TYR102"

]

for residue in active_site:

    print(residue)


# ==========================================================
# 14. DOCKING POSES
# ==========================================================

print("\n===== DOCKING POSES =====")

poses = {

    "Pose_1": -7.2,

    "Pose_2": -8.9,

    "Pose_3": -6.8,

    "Pose_4": -9.4

}

best_pose = min(
    poses,
    key=poses.get
)

print(
    "Best Pose =",
    best_pose
)

print(
    "Score =",
    poses[best_pose]
)


# ==========================================================
# 15. FINAL DOCKING REPORT
# ==========================================================

print("\n===== FINAL REPORT =====")

print(
    "Target Protein :",
    target_protein
)

print(
    "Top Ligand :",
    best_ligand
)

print(
    "Docking Score :",
    ligands[best_ligand]
)

print(
    "Hydrogen Bonds :",
    hydrogen_bonds[best_ligand]
)

print(
    "Best Pose :",
    best_pose
)

print(
    "Pose Score :",
    poses[best_pose]
)


# ==========================================================
# 16. EXPORT REPORT
# ==========================================================

with open(
    "docking_report.txt",
    "w"
) as file:

    file.write(
        "MOLECULAR DOCKING REPORT\n"
    )

    file.write(
        "Target Protein: "
        + target_protein
        + "\n"
    )

    file.write(
        "Best Ligand: "
        + best_ligand
        + "\n"
    )

    file.write(
        "Docking Score: "
        + str(
            ligands[best_ligand]
        )
        + "\n"
    )

print(
    "\nReport Saved Successfully"
)


# ==========================================================
# END OF PHASE 8
# ==========================================================
