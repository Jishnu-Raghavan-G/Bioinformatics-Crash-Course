# ==========================================================
# PHASE 9 : NGS, RNA-SEQ AND FUNCTIONAL GENOMICS
# ==========================================================

# Topics Covered
#
# 1. Sequencing Reads
# 2. Read Count
# 3. Read Length
# 4. Coverage Calculation
# 5. FASTQ Parsing
# 6. Quality Score Analysis
# 7. Gene Expression Analysis
# 8. Differential Expression
# 9. Transcriptome Analysis
# 10. Variant Detection
# 11. SNP Detection
# 12. RNA-Seq Summary Report
#
# ==========================================================


# ==========================================================
# 1. SEQUENCING READS
# ==========================================================

print("\n===== SEQUENCING READS =====")

reads = [

    "ATGCG",
    "TGCGT",
    "GCGTA",
    "CGTAA",
    "GTAAC"

]

for read in reads:

    print(read)


# ==========================================================
# 2. TOTAL READ COUNT
# ==========================================================

print("\n===== TOTAL READS =====")

print("Read Count =", len(reads))


# ==========================================================
# 3. READ LENGTHS
# ==========================================================

print("\n===== READ LENGTHS =====")

for read in reads:

    print(
        read,
        "Length =",
        len(read)
    )


# ==========================================================
# 4. AVERAGE READ LENGTH
# ==========================================================

print("\n===== AVERAGE READ LENGTH =====")

total_length = 0

for read in reads:

    total_length += len(read)

average = total_length / len(reads)

print(
    "Average Length =",
    average
)


# ==========================================================
# 5. COVERAGE CALCULATION
# ==========================================================

print("\n===== COVERAGE =====")

genome_size = 20

total_bases = 0

for read in reads:

    total_bases += len(read)

coverage = total_bases / genome_size

print(
    "Coverage =",
    round(coverage,2),
    "X"
)


# ==========================================================
# 6. FASTQ RECORD
# ==========================================================

print("\n===== FASTQ RECORD =====")

header = "@Read1"

sequence = "ATGCGTA"

quality = "IIIIIII"

print(header)
print(sequence)
print("+")
print(quality)


# ==========================================================
# 7. GENE EXPRESSION DATA
# ==========================================================

print("\n===== GENE EXPRESSION =====")

expression = {

    "GeneA": 1000,
    "GeneB": 50,
    "GeneC": 300,
    "GeneD": 20

}

for gene in expression:

    print(
        gene,
        "=",
        expression[gene]
    )


# ==========================================================
# 8. HIGHLY EXPRESSED GENES
# ==========================================================

print("\n===== HIGH EXPRESSION =====")

for gene in expression:

    if expression[gene] > 500:

        print(gene)


# ==========================================================
# 9. LOW EXPRESSION GENES
# ==========================================================

print("\n===== LOW EXPRESSION =====")

for gene in expression:

    if expression[gene] < 100:

        print(gene)


# ==========================================================
# 10. MOST EXPRESSED GENE
# ==========================================================

print("\n===== TOP GENE =====")

top_gene = max(
    expression,
    key=expression.get
)

print(
    top_gene,
    expression[top_gene]
)


# ==========================================================
# 11. TRANSCRIPTOME ANALYSIS
# ==========================================================

print("\n===== TRANSCRIPTOME =====")

transcriptome = [

    "GeneA",
    "GeneC",
    "GeneD"

]

for transcript in transcriptome:

    print(transcript)

print(
    "Active Genes =",
    len(transcriptome)
)


# ==========================================================
# 12. DIFFERENTIAL EXPRESSION
# ==========================================================

print("\n===== DIFFERENTIAL EXPRESSION =====")

healthy = {

    "GeneA": 100,
    "GeneB": 200

}

cancer = {

    "GeneA": 1000,
    "GeneB": 50

}

for gene in healthy:

    if cancer[gene] > healthy[gene]:

        print(
            gene,
            "UPREGULATED"
        )

    elif cancer[gene] < healthy[gene]:

        print(
            gene,
            "DOWNREGULATED"
        )


# ==========================================================
# 13. VARIANT DETECTION
# ==========================================================

print("\n===== VARIANT DETECTION =====")

reference = "ATGCGT"

sample = "ATGAGT"

for i in range(len(reference)):

    if reference[i] != sample[i]:

        print(
            "Variant at Position",
            i+1
        )


# ==========================================================
# 14. SNP DETECTION
# ==========================================================

print("\n===== SNP DETECTION =====")

for i in range(len(reference)):

    if reference[i] != sample[i]:

        print(

            "Position:",
            i+1,

            "Reference:",
            reference[i],

            "Sample:",
            sample[i]
        )


# ==========================================================
# 15. QUALITY SCORE ANALYSIS
# ==========================================================

print("\n===== QUALITY SCORES =====")

qualities = [

    35,
    40,
    32,
    38,
    39

]

average_quality = sum(qualities) / len(qualities)

print(
    "Average Quality =",
    round(average_quality,2)
)


# ==========================================================
# 16. QUALITY FILTERING
# ==========================================================

print("\n===== QUALITY FILTER =====")

for score in qualities:

    if score >= 30:

        print(
            score,
            "PASS"
        )

    else:

        print(
            score,
            "FAIL"
        )


# ==========================================================
# 17. RNA-SEQ READ COUNTS
# ==========================================================

print("\n===== RNA-SEQ COUNTS =====")

rna_seq = {

    "GeneA": 5000,

    "GeneB": 200,

    "GeneC": 900,

    "GeneD": 50

}

for gene in rna_seq:

    print(
        gene,
        "Reads:",
        rna_seq[gene]
    )


# ==========================================================
# 18. GENE EXPRESSION CLASSIFICATION
# ==========================================================

print("\n===== EXPRESSION CLASS =====")

for gene in rna_seq:

    count = rna_seq[gene]

    if count > 2000:

        level = "HIGH"

    elif count > 500:

        level = "MEDIUM"

    else:

        level = "LOW"

    print(
        gene,
        "->",
        level
    )


# ==========================================================
# 19. NGS REPORT
# ==========================================================

print("\n===== NGS REPORT =====")

print(
    "Total Reads:",
    len(reads)
)

print(
    "Coverage:",
    round(coverage,2),
    "X"
)

print(
    "Top Expressed Gene:",
    top_gene
)

print(
    "Average Quality:",
    round(average_quality,2)
)


# ==========================================================
# 20. EXPORT REPORT
# ==========================================================

with open(
    "ngs_report.txt",
    "w"
) as file:

    file.write(
        "NGS ANALYSIS REPORT\n"
    )

    file.write(
        "Read Count: "
        + str(len(reads))
        + "\n"
    )

    file.write(
        "Coverage: "
        + str(round(coverage,2))
        + "X\n"
    )

    file.write(
        "Top Gene: "
        + top_gene
        + "\n"
    )

print(
    "\nReport Saved Successfully"
)

# ==========================================================
# END OF PHASE 9
# ==========================================================
