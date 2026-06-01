Phase 1: Biology Foundations for Bioinformatics
Objective

Build the biological foundation required to understand sequence analysis, genomics, protein analysis, structure prediction, docking, and other bioinformatics applications.

1. The Central Dogma of Molecular Biology

The central dogma explains how genetic information flows inside living organisms.

DNA → RNA → Protein
DNA

DNA (Deoxyribonucleic Acid) stores hereditary information.

Functions:

Stores genetic instructions.
Passes information to future generations.
Serves as a template for RNA synthesis.

DNA bases:

A = Adenine
T = Thymine
G = Guanine
C = Cytosine

Example:

ATGCGATTA
RNA

RNA (Ribonucleic Acid) is a working copy of DNA.

Functions:

Carries genetic information from DNA.
Participates in protein synthesis.

RNA bases:

A = Adenine
U = Uracil
G = Guanine
C = Cytosine

Notice:

DNA: A T G C
RNA: A U G C

Thymine (T) is replaced by Uracil (U).

Example:

AUGCGAUUA
Protein

Proteins are biological molecules that perform most cellular functions.

Examples:

Enzymes
Antibodies
Hormones
Structural proteins

Proteins are made from amino acids.

2. DNA Structure

DNA consists of repeating units called nucleotides.

Each nucleotide contains:

Sugar
+
Phosphate
+
Nitrogenous Base

Bases:

A
T
G
C
Complementary Base Pairing

DNA strands pair according to fixed rules:

A ↔ T
G ↔ C

Example:

Strand 1: ATGCCA

Strand 2: TACGGT

This concept is heavily used in sequence analysis.

3. Genes and Genomes
Gene

A gene is a segment of DNA that contains instructions to produce a functional product, usually a protein.

Examples:

Insulin Gene
Hemoglobin Gene

Think of a gene as one chapter in a book.

Genome

A genome is the complete DNA content of an organism.

Examples:

Human genome
Rice genome
Bacterial genome

Think of a genome as the entire book.

4. Chromosomes

DNA is packaged into chromosomes.

Humans have:

23 pairs
=
46 chromosomes

Chromosomes help organize and protect DNA.

5. Transcription

Transcription is the process of producing RNA from DNA.

DNA → RNA

Example:

DNA:
ATGCCG

RNA:
AUGCCG

The RNA sequence is copied from DNA with T replaced by U.

6. Translation

Translation is the process of producing proteins from RNA.

RNA → Protein

Performed by:

Ribosome

The ribosome reads RNA instructions and assembles amino acids into proteins.

7. Codons

The ribosome reads RNA three nucleotides at a time.

A group of three nucleotides is called a codon.

Example:

AUG GCU UUU

Each codon specifies an amino acid or a special signal.

Important Codons
Start Codon
RNA: AUG
DNA: ATG

Codes for:

Methionine (Met)

Also signals the start of protein synthesis.

Stop Codons

RNA:

UAA
UAG
UGA

DNA:

TAA
TAG
TGA

Stop codons do not code for amino acids.

Their function is to terminate protein synthesis.

8. Amino Acids

Proteins are built from amino acids.

There are:

20 standard amino acids

Examples:

Codon	Amino Acid
AUG	Methionine
UUU	Phenylalanine
GCU	Alanine
GAA	Glutamate

For now, remember:

Start codon = AUG
Stop codons = UAA, UAG, UGA
9. Open Reading Frame (ORF)

An Open Reading Frame (ORF) is a sequence that has the potential to encode a protein.

Structure:

Start Codon
↓
Coding Region
↓
Stop Codon

Example:

ATG AAA CCC GGG TAA

Bioinformatics tools often search genomes for ORFs.

10. Mutations

A mutation is a change in a DNA sequence.

Example:

Original:

ATGCCA

Mutated:

ATGCTA

One nucleotide has changed.

Types of Mutations
Substitution

One nucleotide is replaced.

A → G

Example:

ATGCCA
ATGCTA
Insertion

An extra nucleotide is added.

ATGC

↓

ATAGC
Deletion

A nucleotide is removed.

ATGC

↓

AGC
11. Frameshift Mutation

Codons are read in groups of three.

Original:

ATG AAA CCC

Removing one nucleotide changes the reading frame:

ATA AAC CC...

This is called a frameshift mutation.

Frameshifts often have severe biological effects.

12. Protein Structure Levels
Primary Structure

Amino acid sequence.

Example:

MET-ALA-GLY
Secondary Structure

Local folding patterns:

α-Helix
β-Sheet
Tertiary Structure

Complete three-dimensional folding of a single protein.

Quaternary Structure

Association of multiple protein chains.

Example:

Hemoglobin.

13. Enzymes

Most proteins function as enzymes.

Definition:

An enzyme is a biological catalyst that speeds up chemical reactions without being consumed.

Example:

Amylase

which breaks down starch.

14. Homology

Homology indicates evolutionary relatedness.

Example:

Human:
ATGCGTAAA

Mouse:
ATGCGTAAA

Highly similar sequences may share a common ancestor.

15. Sequence Identity

Sequence identity measures similarity between sequences.

Example:

ATGCCA
ATGCTA

5 out of 6 positions match.

Identity:

83.3%

Sequence identity is widely used in alignment and comparative genomics.

16. FASTA Format

FASTA is the most common sequence file format.

Example:

>Human_Gene
ATGGCCAAATTTGGG

Components:

Header
>Human_Gene

Starts with > and contains sequence information.

Sequence
ATGGCCAAATTTGGG

Contains DNA, RNA, or protein data.

17. DNA vs RNA vs Protein
Feature	          DNA	               RNA	                Protein
Building Blocks	Nucleotides	        Nucleotides	          Amino Acids
Bases	          A,T,G,C	            A,U,G,C	              None
Function	     Information Storage	Information Transfer  Cellular Function
Example	          ATGC	                 AUGC 	               MAGL

18. BLAST Concept

BLAST (Basic Local Alignment Search Tool) is one of the most important tools in bioinformatics.

Purpose:

Unknown Sequence
        ↓
BLAST Search
        ↓
Similar Sequences Found

Think of BLAST as:

Google Search for DNA, RNA, and Protein Sequences

Applications:

Gene identification
Evolutionary analysis
Sequence comparison
19. Important Databases
National Center for Biotechnology Information (NCBI)

Contains:

Genes
Genomes
Sequences
Publications
GenBank

Contains:

DNA sequences
UniProt

Contains:

Protein sequences
Protein function information
Protein Data Bank (PDB)

Contains:

Protein structures
3D molecular structures
PubMed

Contains:

Scientific research papers
Biomedical publications
Phase 1 Checklist

Before moving to Phase 2, make sure you can explain:

✅ DNA → RNA → Protein

✅ Difference between DNA, RNA, and proteins

✅ A-T and G-C pairing

✅ Gene vs Genome

✅ Chromosome

✅ Transcription

✅ Translation

✅ Codon

✅ Start codon (ATG/AUG)

✅ Stop codons (TAA, TAG, TGA)

✅ ORF

✅ Mutation types

✅ Frameshift mutation

✅ Protein structure levels

✅ Homology

✅ Sequence identity

✅ FASTA format

EXTRA INFO:

1) "DNA serves as a template for RNA synthesis" means:

👉 DNA acts like a master copy or blueprint.

When a cell needs RNA, an enzyme called RNA polymerase reads one strand of DNA and builds a complementary RNA molecule from it.

Example:

DNA strand:

ATGCCGTA

RNA made from it:

UACGGCAU

Notice:

DNA uses A, T, G, C
RNA uses A, U, G, C (U replaces T)

Think of it like this:

📖 DNA = Original book
📝 RNA = Copy of one chapter from the book

The process of making RNA from DNA is called transcription.

So, "DNA serves as a template" = DNA provides the information that RNA copies.

✅ BLAST concept

✅ NCBI, GenBank, UniProt, PDB, PubMed


