Phase 4 – FASTA Files and Sequence Handling

1. What is FASTA?

FASTA is the most widely used file format in bioinformatics for storing biological sequences.

It can store:

DNA sequences
RNA sequences
Protein sequences

Think of FASTA as:

Sequence Name
+
Sequence Data
2. Why FASTA is Important

Almost every bioinformatics tool accepts FASTA files.

Examples:

BLAST
Clustal Omega
MUSCLE
ORF Finder
EMBOSS
MAFFT

FASTA is the starting point of most sequence analyses.

3. FASTA Structure

Example:

>Gene1
ATGCGTAACGTA

>Gene2
TTAACCGGTTAA

Structure:

Header
Sequence
4. FASTA Header

Every header starts with:

>

Example:

>BRCA1_Human

The header contains information about the sequence.

Examples:

Gene name
Protein name
Species name
Database ID
Accession number
5. What is Metadata?

Metadata means:

Data about data

Example:

>BRCA1_Human
ATGCGTAACGTA

Here:

BRCA1_Human

is metadata.

The actual DNA sequence is:

ATGCGTAACGTA
6. DNA FASTA

Contains:

A
T
G
C

Example:

>DNA1
ATGCGTAACGTAGCTA
7. RNA FASTA

Contains:

A
U
G
C

Example:

>RNA1
AUGCGUAACGUAGCUA
8. Protein FASTA

Contains amino acid letters.

Example:

>Protein1
MKWVTFISLLFLFSSAYS

Some amino acid symbols:

A = Alanine
G = Glycine
L = Leucine
V = Valine
M = Methionine
K = Lysine
F = Phenylalanine
9. Multi-FASTA

A FASTA file can contain many sequences.

Example:

>Gene1
ATGC

>Gene2
TTAA

>Gene3
GGCC

This is called:

Multi-FASTA
10. Why Multi-FASTA is Used

Used in:

Sequence Alignment
Phylogenetics
Genome Analysis
Comparative Genomics
Database Storage
11. Long FASTA Sequences

Long sequences are often split into multiple lines.

Example:

>Gene1

ATGCGTACGTAGC

TTAACCGGTTAA

GGGCCCAAATTT

Actually means:

ATGCGTACGTAGCTTAACCGGTTAAGGGCCCAAATTT

All sequence lines are joined together.

12. Reading FASTA Concept

When reading a FASTA file:

Read line by line
Identify headers
Extract sequences
Store sequence data
13. Ignoring Headers

Sometimes only sequence is needed.

Example:

>Gene1
ATGC

Ignore:

>Gene1

Keep:

ATGC

This is common during sequence analysis.

14. Building Complete Sequences

Example FASTA:

ATGC
CGTA
TTAA

Computers combine them into:

ATGCCGTATTAA

before analysis.

15. FASTA Applications
BLAST
Find similar sequences
Alignment
Compare sequences
ORF Detection
Find possible genes
Primer Design
Design PCR primers
Restriction Mapping
Find restriction enzyme sites
Genome Annotation
Identify genes and features
Phylogenetics
Study evolution
16. FASTA in Biological Databases

Most biological databases provide sequences in FASTA format.

Examples:

NCBI
EMBL
DDBJ
UniProt
17. FASTA vs GenBank
FASTA

Contains:

Header
Sequence

Simple and compact.

GenBank

Contains:

Header
Sequence
Gene information
Annotations
References
Features

Much more detailed.

18. Accession Number

Every sequence in a database gets a unique identifier.

Example:

NM_007294

Think of it as:

Roll Number for a sequence

Used to retrieve exact sequences from databases.

19. FASTA Workflow
DNA/RNA/Protein
        ↓
FASTA File
        ↓
BLAST
        ↓
Alignment
        ↓
Gene Analysis
        ↓
Biological Conclusions
Keywords to Memorize
FASTA
Header
Sequence
Metadata
Multi-FASTA
DNA FASTA
RNA FASTA
Protein FASTA
Accession Number
BLAST
Alignment
ORF
Primer Design
Restriction Mapping
Genome Annotation
Viva Questions
What is FASTA?

A text-based format for storing biological sequences.

What symbol starts a FASTA header?
>
What is metadata?

Information about the sequence.

What is Multi-FASTA?

A FASTA file containing multiple sequences.

Why is FASTA important?

It is the standard format accepted by most bioinformatics tools.

5-Minute Revision
FASTA = Sequence file format

> = Header

Header = Metadata

DNA FASTA = A,T,G,C

RNA FASTA = A,U,G,C

Protein FASTA = Amino acid letters

Multi-FASTA = Multiple sequences

Used in:
BLAST
Alignment
ORF Finding
Primer Design
Genome Analysis
Phylogenetics
