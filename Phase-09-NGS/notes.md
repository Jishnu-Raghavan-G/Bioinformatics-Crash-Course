Phase 9 — Next Generation Sequencing (NGS), RNA-Seq and Functional Genomics
Learning Objectives

By the end of this phase you should know:

NGS
Sequencing
Reads
Coverage
Depth
Genome
Transcriptome
Gene Expression
RNA-Seq
FASTQ
Quality Score
Adapter
Mapping
Reference Genome
Alignment
Variant
SNP
Functional Genomics
Differential Expression
1. What is Sequencing?

Sequencing means:

Determining the exact order
of nucleotides in DNA or RNA.

Example:

Unknown DNA:

?

After sequencing:

ATGCGTACCGTA

Now we know its sequence.

2. First Generation vs NGS
First Generation
Sanger Sequencing

Characteristics:

Slow
Expensive
Few sequences
Next Generation Sequencing (NGS)

Characteristics:

Millions of sequences
Parallel sequencing
Fast
Cheaper
Why NGS Revolutionized Biology

Instead of:

1 sequence

NGS generates:

Millions of sequences
simultaneously
3. What is a Read?

Very important.

A read is:

A short sequence produced
by a sequencing machine.

Example:

Original DNA:

ATGCGTACCGTATTAACCGG

Machine produces:

ATGCG

CGTAC

ACCGT

GTATT

Each small fragment is called a:

Read
Why Reads are Needed

Sequencing machines cannot always read entire genomes at once.

Instead:

Genome
↓
Broken into fragments
↓
Sequenced
↓
Reads generated
4. Read Length

Length of a sequencing read.

Example:

ATGCG

Length:

5 bp

Modern platforms:

100 bp
150 bp
250 bp
300 bp

common.

5. Coverage (Depth)

One of the most important concepts.

Coverage means:

How many times a region
has been sequenced.

Example

DNA:

ATGCGT

Reads:

ATGCGT
ATGCGT
ATGCGT
ATGCGT

Coverage:

4X
Why Coverage Matters

Higher coverage:

More reliable data

Low coverage:

Higher error probability

Example

5X

Weak.

30X

Good.

100X

Excellent.

6. What is a Genome?

Genome means:

All DNA of an organism

Example:

Human genome:

≈ 3 billion base pairs

Contains:

All genes
+
Non-coding regions
7. What is a Transcriptome?

Transcriptome means:

All RNA molecules
inside a cell

Easy Difference

Genome
=
All genes

Transcriptome
=
Currently active genes

Example

Cell contains:

Gene A active

Gene B inactive

Gene C active

Transcriptome contains:

RNA from A

RNA from C

not B.

8. What is Gene Expression?

Gene expression means:

How active a gene is

Example

Gene A
1000 RNA copies

Gene B
10 RNA copies

Gene A:

Highly expressed

Gene B:

Low expression
Why?

More RNA copies means:

Gene is being used more
9. What are RNA Copies?

Gene:

DNA

transcribed into:

RNA

Each RNA molecule is a copy.

Example:

Gene A
↓

1000 RNA molecules

means:

Cell repeatedly uses
Gene A

So expression is high.

10. RNA-Seq

RNA Sequencing.

Technique used to measure:

Gene expression

Workflow:

RNA
↓
Convert to cDNA
↓
Sequence
↓
Count reads
↓
Expression levels
Example Output
Gene1 = High

Gene2 = Low

Gene3 = Medium

Meaning

Gene1:

Many reads
Many RNA copies
High expression

Gene2:

Few reads
Low expression
11. FASTQ File

Most common raw sequencing format.

Contains:

Sequence
Quality Scores

Example

@Read1

ATGCGTA

+

IIIIIII
FASTA vs FASTQ
FASTA
Header
Sequence
FASTQ
Header
Sequence
Quality
12. Quality Score

Measures confidence.

High score:

Reliable base

Low score:

Possible sequencing error
13. Reference Genome

Known genome used for comparison.

Example:

Human Reference Genome

New reads are compared against it.

14. Mapping

Mapping means:

Placing reads
onto reference genome

Example:

Read:

ATGCGT

Found at:

Chromosome 1
Position 1000

Read is mapped.

15. Alignment

Alignment means:

Matching reads
to reference sequence

Used during mapping.

16. Variant

Difference from reference genome.

Example:

Reference:

ATGCGT

Sample:

ATGAGT

Difference detected.

Called:

Variant
17. SNP

Single Nucleotide Polymorphism.

Example:

Reference
A

Sample
G

One nucleotide changed.

Called:

SNP
18. Functional Genomics

Study of:

What genes do

instead of just:

What genes exist

Questions:

Which genes active?

Which genes inactive?

How do genes respond?
19. Differential Expression

Comparing expression between conditions.

Example:

Healthy Cell:

Gene X = 100

Cancer Cell:

Gene X = 1000

Result:

Gene X Upregulated

Another Example

Healthy:

500

Cancer:

50

Result:

Downregulated
20. NGS Workflow
DNA/RNA Sample
↓
Library Preparation
↓
Sequencing
↓
Reads
↓
FASTQ
↓
Quality Control
↓
Alignment
↓
Analysis
↓
Biological Interpretation
Keywords to Memorize
NGS
Sequencing
Read
Read Length
Coverage
Depth
Genome
Transcriptome
Gene Expression
RNA Copies
RNA-Seq
FASTQ
Quality Score
Reference Genome
Mapping
Alignment
Variant
SNP
Functional Genomics
Differential Expression
Upregulation
Downregulation
Viva Questions
What is NGS?
High-throughput sequencing technology generating millions of reads simultaneously.
What is a read?
Short DNA sequence produced by a sequencing machine.
What is coverage?
Number of times a genomic region is sequenced.
What is RNA-Seq?
Sequencing-based method used to measure gene expression.
What is transcriptome?
All RNA molecules present in a cell.
What is gene expression?
The activity level of a gene measured by RNA production.
What is a SNP?
Single nucleotide difference in DNA sequence.
Difference between genome and transcriptome?
Genome = all genes

Transcriptome = active genes
5-Minute Revision
Sequencing = Reading DNA

NGS = Millions of reads

Read = Small DNA fragment

Coverage = How many times sequenced

Genome = All DNA

Transcriptome = All RNA

Gene Expression = Gene activity

RNA-Seq = Measures expression

FASTQ = Sequence + Quality

Mapping = Place reads on genome

Alignment = Match sequences

Variant = Difference from reference

SNP = Single base change

Functional Genomics = Study gene function

Differential Expression = Compare expression levels
