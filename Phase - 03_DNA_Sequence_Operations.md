Phase 3 — DNA Sequence Operations
Learning Objective

Learn how computers manipulate DNA sequences.

By the end you should understand:

DNA sequence storage
Length calculation
Base counting
GC content
Complement
Reverse complement
Transcription
Translation basics
Start/Stop codons
ORFs
1. DNA Sequence

Example:

ATGCGTAA

DNA is stored as a string.

In bioinformatics:

dna = "ATGCGTAA"
2. Sequence Length

Definition:

Number of nucleotides present.

Example:

ATGCGTAA

Length:

8

Python:

dna = "ATGCGTAA"

print(len(dna))

Output:

8
3. Nucleotide Counting

Count:

A
T
G
C

Python:

dna = "ATGCGTAA"

print("A =", dna.count("A"))
print("T =", dna.count("T"))
print("G =", dna.count("G"))
print("C =", dna.count("C"))

Output:

A = 3
T = 2
G = 2
C = 1
Why Count Bases?

Used for:

Genome statistics
GC content
Sequence quality
Comparative genomics
4. GC Content
Definition

Percentage of:

G + C

in DNA.

Formula:

GC% =
(G + C)
-------
Total Bases
×100

Example

ATGCGTAA

Count:

G = 2

C = 1

Total = 8

Calculation:

GC% = (3/8)×100

= 37.5%

Python:

dna = "ATGCGTAA"

gc = dna.count("G") + dna.count("C")

gc_percent = gc / len(dna) * 100

print(gc_percent)
Why GC Content Matters

High GC:

More stable DNA
Higher melting temperature

Low GC:

Less stable DNA
5. Complementary Bases

Remember:

A ↔ T

G ↔ C

Example

Original:

ATGC

Complement:

TACG

Why?

Because DNA strands are complementary.

6. Reverse Complement

Very important.

Step 1:

ATGC

Complement:

TACG

Step 2:

Reverse:

GCAT

Final:

Reverse Complement
=
GCAT

Why Important?

Used in:

PCR
Primer design
Genome assembly
Alignment

Python

dna = "ATGC"

comp = dna.replace("A","t")\
          .replace("T","a")\
          .replace("G","c")\
          .replace("C","g")

print(comp.upper())
7. Transcription

DNA → RNA

Rule:

T becomes U

Example:

DNA

ATGCGTAA

RNA

AUGCGUAA

Python

dna = "ATGCGTAA"

rna = dna.replace("T","U")

print(rna)
Why Transcription?

Because:

DNA stays in nucleus

RNA carries information
to ribosome
8. Translation Basics

RNA codons produce amino acids.

Example:

AUG

gives:

Methionine (M)

Important Codons

Start Codon
AUG

Methionine

Starts translation.

Stop Codons
UAA

UAG

UGA

Stop protein synthesis.

9. Open Reading Frame (ORF)

Definition:

Start codon
↓
Coding sequence
↓
Stop codon

Example:

AUG GCU AAA UAA

ORF:

AUG → UAA

Why Important?

ORFs often indicate:

Potential genes
10. Mutation Basics

A mutation is:

Change in sequence

Example:

ATGC

↓

ATTC

One base changed.

Types

Substitution
A → G
Insertion
ATGC

↓

ATTGC
Deletion
ATGC

↓

AGC
11. Biological Sequence Alignment (Introduction)

Purpose:

Compare sequences

Example:

ATGCGT

ATGAGT

Find:

Matches

Differences

Applications:

Evolution
Homology
Gene identification
BLAST
12. Keywords To Memorize
Nucleotide
Sequence
Length
GC Content
Complement
Reverse Complement
Transcription
Translation
Codon
Start Codon
Stop Codon
ORF
Mutation
Alignment
Phase 3 Practical Files

Keep these in your repo:

phase3_length.py

phase3_base_count.py

phase3_gc_content.py

phase3_complement.py

phase3_reverse_complement.py

phase3_transcription.py

phase3_orf_basics.py

or if you prefer a single file:

phase3_dna_operations.py

containing all Phase 3 code examples together.
