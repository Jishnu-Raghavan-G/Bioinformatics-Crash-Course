Phase 2: Python for Bioinformatics
Objective

Learn Python fundamentals required for bioinformatics and biological sequence analysis.

Why Python?

Python is widely used in bioinformatics for:

DNA sequence analysis
Protein analysis
FASTA file processing
Genome analysis
NGS data processing
Automation
Variables

Variables store data.

Example:

dna = "ATGCGT"
Data Types
String

Text data.

dna = "ATGCGT"
Integer

Whole numbers.

length = 100
Float

Decimal numbers.

gc = 56.7
Boolean

True or False values.

is_gene = True
Strings

DNA sequences are treated as strings.

Example:

dna = "ATGCGTAA"

Length:

len(dna)
String Indexing
dna[0]

returns first character.

dna[1]

returns second character.

String Slicing
dna[0:3]

returns:

ATG
Counting Characters
dna.count("A")

Counts adenine bases.

User Input
dna = input("Enter DNA: ")
Arithmetic
+
-
*
/

Used for calculations like GC%.

Comparison Operators
>
<
==
!=
>=
<=
If Statements
if condition:
    statement
If Else
if condition:
    statement
else:
    statement
Loops
for base in dna:

Used to process sequences.

Lists

Store multiple values.

genes = ["BRCA1","TP53","EGFR"]
Dictionaries

Store key-value pairs.

codons = {
    "AUG":"Methionine"
}
Functions

Reusable code blocks.

def greet():
    print("Hello")
Return Statement
return value

Sends output back.

GC Content

Formula:

(G+C)/Length × 100

Example:

gc = dna.count("G") + dna.count("C")
gc_percent = gc / len(dna) * 100
Important Bioinformatics Skills Learned
Sequence storage
Base counting
GC content analysis
Codon detection
Basic automation
