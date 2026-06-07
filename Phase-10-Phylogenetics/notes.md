Phase 10 — Phylogenetics and Evolutionary Bioinformatics
Learning Objectives

By the end of this phase you should know:

Phylogenetics
Evolution
Phylogenetic Tree
Ancestor
Descendant
Clade
Node
Branch
Root
Leaf
Outgroup
Homologous Sequences
Orthologs
Paralogs
Distance Matrix
Tree Construction
UPGMA
Neighbor Joining
Bootstrap Analysis
Molecular Evolution
1. What is Phylogenetics?

Phylogenetics is the study of evolutionary relationships between organisms, genes, or proteins.

Question:

Who evolved from whom?
Who is most closely related?

Phylogenetics helps answer these questions.

Example

Suppose we compare:

Human
Chimpanzee
Mouse
Dog

Phylogenetics helps determine:

Human and Chimpanzee
are more closely related
than Human and Mouse.
2. Evolution

Evolution means:

Gradual change in organisms
over generations.

Occurs through:

Mutation
Natural Selection
Genetic Drift
Example

DNA:

ATGCGT

Mutation:

ATGAGT

Small changes accumulate over millions of years.

3. Why Compare Sequences?

Similar sequences often indicate:

Common ancestry

Example:

Human Gene:
ATGCGTAA

Chimp Gene:
ATGCGTAT

Very similar.

Likely share a recent ancestor.

4. Homologous Sequences

Homologous sequences are sequences that share a common evolutionary origin.

Example:

Human Hemoglobin

Mouse Hemoglobin

Both evolved from an ancestral hemoglobin gene.

Important

Correct:

These genes are homologous.

Incorrect:

70% homologous.

Use:

70% identity.
5. Orthologs

Orthologs are:

Genes in different species
derived from a common ancestor.

Example:

Human TP53

Mouse TP53

Usually perform similar functions.

6. Paralogs

Paralogs are:

Genes produced by duplication
within the same species.

Example:

Gene A
↓ duplication
Gene A1
Gene A2

Both remain in the same organism.

Ortholog vs Paralog
Ortholog
=
Different species

Paralog
=
Same species
7. Phylogenetic Tree

A diagram showing evolutionary relationships.

Example:

       Human
      /
-----|
      \Chimp


Shows:

Human and Chimp
share a recent ancestor.
8. Components of a Tree
Root

Starting point.

Represents:

Common ancestor

Example:

      Root
        |
      -----
Branch

Line connecting organisms.

Represents:

Evolutionary path
Node

Branching point.

Represents:

Common ancestor
Leaf (Tip)

End of branch.

Represents:

Current organism

Example:

Human
Chimp
Mouse
9. Node

Very important.

A node represents:

Hypothetical ancestor

Example:

      Node
      /  \
 Human  Chimp

Means:

Human and Chimp
share this ancestor.
10. Branch Length

Branch length often represents:

Evolutionary distance

Long branch:

More changes

Short branch:

Fewer changes
11. Clade

A clade includes:

Ancestor
+
All descendants

Example:

Human
Chimp
Gorilla

may form one clade.

12. Outgroup

Used as reference.

Example:

Human
Chimp
Mouse

Outgroup:
Fish

Helps determine evolutionary direction.

13. Distance Matrix

Table showing evolutionary distances.

Example:

Species	  Human	    Chimp	    Mouse
Human	     0	        2	       12
Chimp	     2	        0	       11
Mouse	     12	        11 	      0

Small number:

More similar

Large number:

Less similar
14. Tree Construction

Process of building phylogenetic trees.

Workflow:

Sequences
↓
Alignment
↓
Distance Calculation
↓
Tree Construction
15. UPGMA

Full Form:

Unweighted Pair Group Method
with Arithmetic Mean

Simple tree-building method.

Assumes:

Constant evolutionary rate
Limitation

Real evolution is rarely constant.

16. Neighbor Joining (NJ)

Most popular beginner method.

Builds trees using:

Distance matrix

Advantages:

Fast
Simple
Widely used
17. Molecular Evolution

Study of evolution using molecular data.

Examples:

DNA sequences
RNA sequences
Protein sequences

instead of physical characteristics.

Example

Instead of:

Tail length
Body size

we compare:

DNA sequences
18. Bootstrap Analysis

Measures confidence in a phylogenetic tree.

Example:

Bootstrap = 95%

Means:

Relationship strongly supported.
Interpretation
>90%
Very strong

70-90%
Good

<50%
Weak
19. Applications of Phylogenetics
Evolutionary Biology

Study organism evolution.

Disease Tracking

Track pathogen evolution.

Example:

COVID-19 variants
Species Identification

Identify unknown organisms.

Conservation Biology

Study endangered species relationships.

Drug Research

Understand protein evolution.

20. Real Workflow
DNA Sequences
↓
Alignment
↓
Distance Matrix
↓
Phylogenetic Tree
↓
Evolutionary Interpretation
Keywords to Memorize
Phylogenetics
Evolution
Phylogenetic Tree
Root
Node
Branch
Leaf
Clade
Outgroup
Homologous Sequences
Ortholog
Paralog
Distance Matrix
UPGMA
Neighbor Joining
Bootstrap
Molecular Evolution
Common Ancestor
Viva Questions
What is phylogenetics?
Study of evolutionary relationships among organisms, genes, or proteins.
What is a phylogenetic tree?
Diagram showing evolutionary relationships.
What is a node?
A branching point representing a common ancestor.
What is a branch?
Evolutionary pathway connecting nodes.
What is a clade?
Ancestor and all its descendants.
Difference between orthologs and paralogs?
Orthologs:
Different species

Paralogs:
Same species
What is bootstrap analysis?
Method used to estimate confidence in a phylogenetic tree.
What is an outgroup?
Reference organism used to root a phylogenetic tree.
5-Minute Revision
Phylogenetics = Evolutionary relationships

Tree = Evolution diagram

Root = Common ancestor

Node = Ancestor point

Branch = Evolution path

Leaf = Current organism

Clade = Ancestor + descendants

Ortholog = Different species

Paralog = Same species

Distance Matrix = Similarity table

UPGMA = Simple tree method

Neighbor Joining = Popular tree method

Bootstrap = Confidence score

Molecular Evolution = Evolution using DNA/RNA/proteins
