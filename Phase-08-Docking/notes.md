Phase 8 — Molecular Docking and Drug Discovery
Learning Objectives

By the end of this phase you should know:

Molecular docking
Drug discovery
Target protein
Ligand
Binding site
Active site
Lock and key model
Induced fit model
Binding affinity
Docking score
Hydrogen bonds
Hydrophobic interactions
Virtual screening
AutoDock
AutoDock Vina
Protein-ligand complex
Drug candidates
1. What is Molecular Docking?

Molecular docking is a computational method used to predict:

How a molecule binds
to a protein

Think:

Protein
=
Lock

Drug Molecule
=
Key

Docking tries to determine:

Which key fits the lock best
Why Do We Need Docking?

Suppose:

10,000 drug molecules

Testing all experimentally is expensive.

Docking helps:

Computer
↓
Predict best candidates
↓
Reduce laboratory work
2. What is a Target Protein?

A protein involved in a disease.

Example:

Cancer protein

Viral protein

Bacterial enzyme

Scientists try to block it.

Example

COVID research:

Viral Protease

became a target protein.

3. What is a Ligand?

Very important term.

A ligand is:

A molecule that binds
to another molecule

In docking:

Drug Molecule
=
Ligand
Examples
Drug

Hormone

Neurotransmitter

Small molecule

can all act as ligands.

Example
Protein
↓
Ligand binds
↓
Protein activity changes
4. Protein-Ligand Complex

After binding:

Protein
+
Ligand

becomes:

Protein-Ligand Complex

Example:

Enzyme
+
Drug
=
Complex
5. Binding Site

The region where ligand binds.

Think:

Lock
↓
Keyhole

The keyhole is:

Binding Site
6. Active Site

Special type of binding site.

Usually found in enzymes.

Where actual reaction occurs.

Example:

Enzyme
↓
Active Site
↓
Catalysis
Easy Difference
Binding Site
=
Any binding region

Active Site
=
Reaction region
7. Lock and Key Model

Old model.

Idea:

Protein shape fixed

Ligand shape fixed

Perfect fit required.

Example:

Lock
+
Correct Key
=
Fit
Limitation

Proteins are not completely rigid.

8. Induced Fit Model

Modern model.

Protein changes shape slightly during binding.

Ligand approaches
↓
Protein adjusts
↓
Better binding

More realistic.

9. Binding Affinity

Measures:

How strongly ligand binds

High Affinity

Strong binding

Low Affinity

Weak binding
Example
Drug A
Affinity = High

Drug B
Affinity = Low

Drug A usually preferred.

10. Docking Score

Computers estimate binding strength.

Result:

Docking Score

Usually:

Negative values

Example

-3 kcal/mol

Weak.

-6 kcal/mol

Moderate.

-9 kcal/mol

Strong.

Important Rule
More Negative
=
Better Binding

Example

-10

better than

-5
11. Hydrogen Bond

Very important interaction.

Occurs between:

Hydrogen
+
Electronegative atom

such as:

Oxygen

Nitrogen

Why Important?

Helps stabilize binding.

Example

Drug
↔
Protein

Hydrogen Bond
12. Hydrophobic Interaction

Hydrophobic groups avoid water.

Examples:

Valine

Leucine

Isoleucine

Phenylalanine

These interact together.

Why Important?

Contributes significantly to ligand binding.

13. Van der Waals Interactions

Weak attractive forces.

Very common in docking.

Individually weak.

Together important.

14. Virtual Screening

Suppose:

100,000 molecules

Need best candidates.

Computer performs docking repeatedly.

Process:

Database
↓
Docking
↓
Ranking
↓
Top Hits

Called:

Virtual Screening
15. Drug Discovery Workflow
Disease
↓
Target Protein
↓
Ligand Library
↓
Docking
↓
Top Candidates
↓
Laboratory Testing
↓
Drug Development
16. AutoDock

Most famous docking software.

Used for:

Protein-ligand docking

Input:

Protein structure

Ligand structure

Output:

Docking poses

Binding scores
17. AutoDock Vina

Improved version.

Advantages:

Faster

More accurate

Popular

Widely used.

18. Docking Pose

Pose means:

Ligand orientation

inside binding site.

One ligand can have:

Many possible poses

Software chooses:

Best pose
19. Binding Energy

Energy released during binding.

Usually reported as:

kcal/mol

Example

-8 kcal/mol

Good binding.

Rule:

Lower Energy
=
More Stable Complex
20. Limitations of Docking

Docking is prediction.

Not proof.

Reasons:

Protein flexibility

Water molecules

Cellular environment

Approximate calculations

Therefore:

Docking
↓
Experimental validation

is required.

21. Real Example

Suppose:

Cancer Protein

Target.

Dock:

1000 molecules

Results:

Drug A = -9.2

Drug B = -7.1

Drug C = -4.3

Best candidate:

Drug A

because score is most negative.

Keywords to Memorize
Docking
Target Protein
Ligand
Binding Site
Active Site
Protein-Ligand Complex
Binding Affinity
Docking Score
Binding Energy
Hydrogen Bond
Hydrophobic Interaction
Van der Waals Interaction
Virtual Screening
AutoDock
AutoDock Vina
Docking Pose
Drug Discovery
Lock and Key Model
Induced Fit Model
Viva Questions
What is molecular docking?
Computational prediction of how a ligand binds to a target protein.
What is a ligand?
A molecule that binds to another molecule.
What is a target protein?
Protein selected for drug targeting.
Difference between active site and binding site?
Active site performs catalysis.

Binding site is any ligand-binding region.
What is docking score?
Numerical estimate of binding strength.
Which docking score is better?
More negative score.
What is virtual screening?
Computational screening of many compounds using docking.
What is AutoDock Vina?
Popular molecular docking software.
5-Minute Revision
Protein = Lock

Ligand = Key

Binding Site = Keyhole

Docking = Predict binding

Affinity = Binding strength

Docking Score = Predicted strength

More Negative Score = Better

Hydrogen Bond = Stabilizes binding

Virtual Screening = Screen many compounds

AutoDock Vina = Docking software

Protein + Ligand = Complex

Docking → Prediction only

Lab experiments required for confirmation
