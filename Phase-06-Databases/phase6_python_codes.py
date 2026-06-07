# =====================================================
# PHASE 6 : BIOLOGICAL DATABASES
# =====================================================

# Topics Covered
#
# 1. Gene Database
# 2. Protein Database
# 3. Search by Gene Name
# 4. Search by Accession Number
# 5. Database Statistics
# 6. Add New Record
# 7. Update Record
# 8. Delete Record
# 9. FASTA Storage
# 10. Annotation Retrieval
# 11. Mini NCBI Search
# 12. Database Report
#
# =====================================================


# =====================================================
# 1. GENE DATABASE
# =====================================================

print("\n===== GENE DATABASE =====")

gene_database = {

    "BRCA1": {
        "organism": "Human",
        "function": "DNA Repair"
    },

    "TP53": {
        "organism": "Human",
        "function": "Tumor Suppressor"
    },

    "EGFR": {
        "organism": "Human",
        "function": "Growth Receptor"
    }

}

for gene in gene_database:

    print(gene)


# =====================================================
# 2. SEARCH BY GENE NAME
# =====================================================

print("\n===== SEARCH GENE =====")

gene = "BRCA1"

if gene in gene_database:

    print("Gene Found")

    print(gene_database[gene])

else:

    print("Gene Not Found")


# =====================================================
# 3. ACCESSION DATABASE
# =====================================================

print("\n===== ACCESSION NUMBERS =====")

accession_database = {

    "NM_007294": "BRCA1",

    "NM_000546": "TP53",

    "NM_005228": "EGFR"

}

for accession in accession_database:

    print(accession,
          "->",
          accession_database[accession])


# =====================================================
# 4. SEARCH BY ACCESSION NUMBER
# =====================================================

print("\n===== ACCESSION SEARCH =====")

query = "NM_000546"

if query in accession_database:

    print("Gene:",
          accession_database[query])

else:

    print("Not Found")


# =====================================================
# 5. DATABASE SIZE
# =====================================================

print("\n===== DATABASE SIZE =====")

print("Total Records =",
      len(gene_database))


# =====================================================
# 6. ADD NEW GENE
# =====================================================

print("\n===== ADD RECORD =====")

gene_database["MYC"] = {

    "organism": "Human",

    "function": "Cell Growth Regulation"

}

print("MYC Added")


# =====================================================
# 7. UPDATE RECORD
# =====================================================

print("\n===== UPDATE RECORD =====")

gene_database["MYC"]["function"] = "Oncogene"

print(gene_database["MYC"])


# =====================================================
# 8. DELETE RECORD
# =====================================================

print("\n===== DELETE RECORD =====")

del gene_database["MYC"]

print("MYC Deleted")


# =====================================================
# 9. PROTEIN DATABASE
# =====================================================

print("\n===== PROTEIN DATABASE =====")

protein_database = {

    "P69905": {
        "name": "Hemoglobin Alpha",
        "length": 142
    },

    "P01308": {
        "name": "Insulin",
        "length": 110
    }

}

for protein in protein_database:

    print(protein,
          protein_database[protein]["name"])


# =====================================================
# 10. FASTA STORAGE
# =====================================================

print("\n===== FASTA STORAGE =====")

fasta_database = {

    "BRCA1":
    "ATGCGTAACCGGTTAA",

    "TP53":
    "ATGGGCTAACCGGTAA"

}

for gene in fasta_database:

    print(">", gene)

    print(fasta_database[gene])


# =====================================================
# 11. SEQUENCE RETRIEVAL
# =====================================================

print("\n===== SEQUENCE RETRIEVAL =====")

gene = "BRCA1"

if gene in fasta_database:

    print(fasta_database[gene])


# =====================================================
# 12. ANNOTATION DATABASE
# =====================================================

print("\n===== ANNOTATIONS =====")

annotations = {

    "BRCA1": {
        "chromosome": 17,
        "function": "DNA Repair",
        "disease": "Breast Cancer"
    }

}

print(annotations["BRCA1"])


# =====================================================
# 13. MINI NCBI SEARCH
# =====================================================

print("\n===== MINI NCBI SEARCH =====")

query = "TP53"

if query in gene_database:

    print("Record Found")

    print(gene_database[query])

else:

    print("No Result")


# =====================================================
# 14. GENE FUNCTION SEARCH
# =====================================================

print("\n===== FUNCTION SEARCH =====")

for gene in gene_database:

    function = gene_database[gene]["function"]

    print(gene,
          "->",
          function)


# =====================================================
# 15. ORGANISM FILTER
# =====================================================

print("\n===== ORGANISM FILTER =====")

for gene in gene_database:

    if gene_database[gene]["organism"] == "Human":

        print(gene)


# =====================================================
# 16. LONGEST PROTEIN
# =====================================================

print("\n===== LONGEST PROTEIN =====")

longest = ""

max_length = 0

for protein in protein_database:

    length = protein_database[protein]["length"]

    if length > max_length:

        max_length = length

        longest = protein

print("Longest Protein =", longest)

print("Length =", max_length)


# =====================================================
# 17. DATABASE REPORT
# =====================================================

print("\n===== DATABASE REPORT =====")

print("Genes:",
      len(gene_database))

print("Proteins:",
      len(protein_database))

print("Sequences:",
      len(fasta_database))

print("Annotations:",
      len(annotations))


# =====================================================
# 18. EXPORT DATABASE
# =====================================================

print("\n===== EXPORT =====")

with open("database_report.txt", "w") as file:

    file.write("BIOLOGICAL DATABASE REPORT\n")

    file.write("-------------------------\n")

    file.write(
        "Genes: "
        + str(len(gene_database))
        + "\n"
    )

    file.write(
        "Proteins: "
        + str(len(protein_database))
        + "\n"
    )

print("Report Saved")


# =====================================================
# 19. SIMPLE PUBMED SIMULATION
# =====================================================

print("\n===== PUBMED SEARCH =====")

papers = {

    "CRISPR":
    "Genome Editing Paper",

    "Cancer":
    "Cancer Genomics Paper",

    "Longevity":
    "Aging Research Paper"

}

keyword = "Longevity"

if keyword in papers:

    print(papers[keyword])


# =====================================================
# 20. COMPLETE DATABASE SUMMARY
# =====================================================

print("\n===== SUMMARY =====")

print("NCBI -> Central Resource")
print("GenBank -> DNA Sequences")
print("RefSeq -> Curated Sequences")
print("UniProt -> Protein Information")
print("PDB -> 3D Structures")
print("PubMed -> Research Papers")


# =====================================================
# END OF PHASE 6
# =====================================================
