Phase 5 — Sequence Alignment and BLAST
Learning Objectives

By the end of this phase you should know:

What alignment is
Why alignment is important
Sequence similarity
Sequence identity
Matches
Mismatches
Gaps
Pairwise alignment
Multiple sequence alignment
BLAST
Database searching
E-value
Score
Query sequence
Subject sequence
Homology
1. What is Sequence Alignment?

Alignment means:

Comparing biological sequences
to identify similarities and differences.

Example:

Sequence 1
ATGCGT

Sequence 2
ATGAGT

Alignment:

ATGCGT
||| ||
ATGAGT
Why Align Sequences?

Scientists align sequences to determine:

Gene function
Protein function
Evolutionary relationships
Mutations
Species similarity
2. Match

A match occurs when bases are identical.

Example:

A = A
G = G
T = T

Alignment:

ATGCGT
||| ||
ATGAGT

Matches:

A
T
G
G
T
3. Mismatch

A mismatch occurs when bases differ.

Example:

C ≠ A

Alignment:

ATGCGT
ATGAGT

Mismatch:

C
A
4. Gap

Sometimes a sequence gains or loses bases.

To align properly we insert gaps.

Example:

ATG-CGT
ATGACGT

Gap:

-
Why Gaps?

Represent:

Insertion
Deletion
Evolutionary changes
5. Identity

Identity means:

Exact matches

Example:

ATGCGT
ATGAGT

Matches:

5

Total positions:

6

Identity:

5/6 × 100

83.3%
6. Similarity

Similarity means:

Sequences are related
even if not identical.

Protein example:

Leucine
Isoleucine

Different amino acids.

But chemically similar.

7. Pairwise Alignment

Comparison of:

One sequence
vs
One sequence

Example:

Human Gene

Mouse Gene
Applications
Mutation detection
Species comparison
Gene identification
8. Multiple Sequence Alignment (MSA)

Comparison of:

Many sequences
at the same time

Example:

Human

Chimpanzee

Mouse

Dog

Alignment:

ATGCGT
ATGCGT
ATGAGT
ATGCGA
Why MSA?

Used for:

Phylogenetics
Conserved regions
Evolution studies
9. Conserved Region

Region that remains unchanged.

Example:

ATGCGT
ATGCGT
ATGCGT
ATGCGT

Conserved:

ATGCGT
Why Conserved Regions Matter?

Often indicate:

Important biological functions
Essential genes
Active sites
10. What is BLAST?

BLAST stands for:

Basic Local Alignment Search Tool

One of the most important tools in bioinformatics.

Purpose of BLAST

Given an unknown sequence:

ATGCGTAACCGTT

BLAST searches databases for similar sequences.

Think of BLAST Like Google

Google:

Search word
↓
Find webpages

BLAST:

Search sequence
↓
Find similar sequences
Example

Query:

ATGCGTAACCGTT

BLAST searches:

Millions of sequences

and returns:

Closest matches
11. Query Sequence

The sequence you submit.

Example:

ATGCGTAACCGTT

This is called:

Query
12. Subject Sequence

Database sequence matching your query.

Example:

ATGCGTAACCGTT

Found in database.

Called:

Subject Sequence
13. BLAST Workflow
Query Sequence
        ↓
BLAST Search
        ↓
Database Scan
        ↓
Alignment
        ↓
Results
14. BLAST Databases

Common databases:

GenBank
RefSeq
UniProt
PDB
15. Types of BLAST
BLASTN
DNA vs DNA
BLASTP
Protein vs Protein
BLASTX
DNA → Protein search
TBLASTN
Protein vs DNA database
TBLASTX
Translated DNA vs Translated DNA
16. Alignment Score

Higher score means:

Better alignment

More:

Matches

Fewer:

Mismatches
Gaps
17. E-value

One of the most important BLAST concepts.

E-value means:

Expected number of matches
occurring by chance.
Interpretation
Good
0.0

Very significant.

Excellent
1e-50

Almost certainly related.

Weak
1

Could happen by chance.

Very Poor
10

Usually meaningless.

Easy Rule
Lower E-value
=
Better Match
18. Homology

Homology means:

Two sequences share
a common ancestor.

Important:

Sequences are either homologous
or not homologous.

Not:

70% homologous

This is scientifically incorrect.

Instead say:

70% identity
19. Applications of BLAST
Gene Identification

Unknown gene.

Find its identity.

Species Identification

Unknown organism.

Determine species.

Mutation Analysis

Compare normal and mutant genes.

Drug Research

Find related proteins.

Evolutionary Studies

Compare organisms.

20. Real-Life Example

Suppose:

You sequence a gene.

Unknown:

ATGCGTAACCGTT...

Run BLAST.

Result:

99% identity
Human BRCA1 gene

Now you know:

Gene identity
Gene function
Related research
Keywords to Memorize
Alignment
Match
Mismatch
Gap
Identity
Similarity
Pairwise Alignment
Multiple Sequence Alignment
BLAST
BLASTN
BLASTP
Query Sequence
Subject Sequence
Alignment Score
E-value
Conserved Region
Homology
Viva Questions
What is sequence alignment?
Comparison of biological sequences to identify similarities and differences.
What is BLAST?
Basic Local Alignment Search Tool used to find similar sequences in databases.
What is a query sequence?
The sequence submitted for searching.
What is a subject sequence?
The matching sequence found in the database.
What does a low E-value indicate?
A highly significant match.
Difference between identity and similarity?
Identity = exact matches

Similarity = related properties or function
5-Minute Revision
Alignment = sequence comparison

Match = same bases

Mismatch = different bases

Gap = insertion/deletion

Identity = exact matching %

BLAST = sequence search engine

Query = your sequence

Subject = database sequence

Score = alignment quality

E-value = chance match

Lower E-value = better result

MSA = many sequences aligned together

Conserved region = unchanged region

Homology = common ancestry
