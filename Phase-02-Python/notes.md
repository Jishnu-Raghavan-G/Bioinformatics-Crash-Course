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

EXTRA: 
1)We calculate GC content because G (Guanine) and C (Cytosine) form 3 hydrogen bonds, while A (Adenine) and T (Thymine) form only 2 hydrogen bonds.

G ≡ C   → 3 bonds
A = T   → 2 bonds

Because of this:

More GC → DNA is more stable and harder to separate.
Less GC → DNA is less stable and easier to separate.
Why biologists care about GC content?
DNA stability
High GC DNA is stronger.
Melting temperature (Tm)
High GC → higher temperature needed to denature DNA.
Species comparison
Different organisms have different GC percentages.
PCR primer design
Primers need a suitable GC content (usually 40–60%).
Can we calculate AT content?

Yes!

AT Content = %A + %T

In fact:

GC% + AT% = 100%

So if GC content is 60%:

AT content = 40%
Example

DNA:

ATGCGC

Count:

A = 1
T = 1
G = 2
C = 2
Total = 6

GC content:

(2 + 2)/6 × 100
= 66.7%

AT content:

(1 + 1)/6 × 100
= 33.3%

So AT content is not ignored; GC content is just more informative because it directly affects DNA stability, melting temperature, and many bioinformatics analyses.
