# ==========================================================
# PHASE 11 : SYSTEMS BIOLOGY & BIOLOGICAL NETWORKS
# ==========================================================

# Topics Covered
#
# 1. Biological Network
# 2. Nodes and Edges
# 3. Degree Calculation
# 4. Hub Gene Detection
# 5. Gene Regulatory Network
# 6. Protein Interaction Network
# 7. Pathway Analysis
# 8. Network Centrality
# 9. Disease Network
# 10. Pathway Enrichment
# 11. Network Report
#
# ==========================================================


# ==========================================================
# 1. GENE NETWORK
# ==========================================================

print("\n===== GENE NETWORK =====")

network = {

    "TP53"  : ["BRCA1", "MYC", "EGFR"],

    "BRCA1" : ["TP53", "RAD51"],

    "MYC"   : ["TP53", "EGFR"],

    "EGFR"  : ["TP53", "MYC"],

    "RAD51" : ["BRCA1"]

}

for gene in network:

    print(gene, "->", network[gene])


# ==========================================================
# 2. TOTAL NODES
# ==========================================================

print("\n===== TOTAL NODES =====")

nodes = len(network)

print("Nodes =", nodes)


# ==========================================================
# 3. TOTAL EDGES
# ==========================================================

print("\n===== TOTAL EDGES =====")

edges = 0

for gene in network:

    edges += len(network[gene])

edges = edges // 2

print("Edges =", edges)


# ==========================================================
# 4. DEGREE OF EACH NODE
# ==========================================================

print("\n===== NODE DEGREE =====")

for gene in network:

    degree = len(network[gene])

    print(
        gene,
        "Degree =",
        degree
    )


# ==========================================================
# 5. HUB GENE DETECTION
# ==========================================================

print("\n===== HUB GENE =====")

hub_gene = max(
    network,
    key=lambda gene:
    len(network[gene])
)

print("Hub Gene =", hub_gene)

print(
    "Connections =",
    len(network[hub_gene])
)


# ==========================================================
# 6. CENTRALITY SCORE
# ==========================================================

print("\n===== CENTRALITY =====")

for gene in network:

    centrality = (
        len(network[gene])
        /
        (nodes - 1)
    )

    print(
        gene,
        "Centrality =",
        round(centrality,2)
    )


# ==========================================================
# 7. GENE REGULATORY NETWORK
# ==========================================================

print("\n===== GENE REGULATION =====")

regulation = {

    "TP53" : ["DNA_REPAIR"],

    "MYC"  : ["CELL_GROWTH"],

    "EGFR" : ["PROLIFERATION"]

}

for regulator in regulation:

    for target in regulation[regulator]:

        print(
            regulator,
            "->",
            target
        )


# ==========================================================
# 8. PROTEIN INTERACTION NETWORK
# ==========================================================

print("\n===== PPI NETWORK =====")

ppi = [

    ("TP53", "BRCA1"),

    ("TP53", "MYC"),

    ("MYC", "EGFR"),

    ("BRCA1", "RAD51")

]

for interaction in ppi:

    print(
        interaction[0],
        "<->",
        interaction[1]
    )


# ==========================================================
# 9. PATHWAY DATABASE
# ==========================================================

print("\n===== PATHWAYS =====")

pathways = {

    "Cell_Cycle" :
    ["TP53", "MYC"],

    "DNA_Repair" :
    ["TP53", "BRCA1", "RAD51"],

    "Growth_Signaling" :
    ["EGFR", "MYC"]

}

for pathway in pathways:

    print(pathway)


# ==========================================================
# 10. PATHWAY MEMBERS
# ==========================================================

print("\n===== PATHWAY GENES =====")

for pathway in pathways:

    print("\n", pathway)

    for gene in pathways[pathway]:

        print(gene)


# ==========================================================
# 11. PATHWAY SIZE
# ==========================================================

print("\n===== PATHWAY SIZE =====")

for pathway in pathways:

    print(
        pathway,
        "=",
        len(pathways[pathway]),
        "Genes"
    )


# ==========================================================
# 12. PATHWAY ENRICHMENT
# ==========================================================

print("\n===== ENRICHMENT =====")

experimental_genes = [

    "TP53",

    "BRCA1",

    "RAD51"

]

for pathway in pathways:

    overlap = 0

    for gene in experimental_genes:

        if gene in pathways[pathway]:

            overlap += 1

    print(
        pathway,
        "Overlap =",
        overlap
    )


# ==========================================================
# 13. DISEASE NETWORK
# ==========================================================

print("\n===== DISEASE NETWORK =====")

disease_genes = {

    "Cancer" :
    ["TP53", "BRCA1", "MYC"],

    "Breast_Cancer" :
    ["BRCA1"],

    "Lung_Cancer" :
    ["EGFR"]

}

for disease in disease_genes:

    print(
        disease,
        "->",
        disease_genes[disease]
    )


# ==========================================================
# 14. MULTI-OMICS DATA
# ==========================================================

print("\n===== MULTI-OMICS =====")

omics = {

    "Genomics" :
    "DNA Mutation Data",

    "Transcriptomics" :
    "RNA Expression Data",

    "Proteomics" :
    "Protein Abundance Data",

    "Metabolomics" :
    "Metabolite Data"

}

for omic in omics:

    print(
        omic,
        "->",
        omics[omic]
    )


# ==========================================================
# 15. LONGEVITY PATHWAYS
# ==========================================================

print("\n===== LONGEVITY =====")

longevity = [

    "mTOR",

    "AMPK",

    "Sirtuins",

    "Autophagy"

]

for pathway in longevity:

    print(pathway)


# ==========================================================
# 16. MOST CONNECTED PATHWAY
# ==========================================================

print("\n===== LARGEST PATHWAY =====")

largest = max(
    pathways,
    key=lambda p:
    len(pathways[p])
)

print(
    "Largest Pathway =",
    largest
)

print(
    "Genes =",
    len(pathways[largest])
)


# ==========================================================
# 17. NETWORK SUMMARY
# ==========================================================

print("\n===== NETWORK SUMMARY =====")

print("Nodes =", nodes)

print("Edges =", edges)

print("Hub Gene =", hub_gene)

print(
    "Largest Pathway =",
    largest
)


# ==========================================================
# 18. EXPORT REPORT
# ==========================================================

with open(
    "systems_biology_report.txt",
    "w"
) as file:

    file.write(
        "SYSTEMS BIOLOGY REPORT\n"
    )

    file.write(
        "Nodes: "
        + str(nodes)
        + "\n"
    )

    file.write(
        "Edges: "
        + str(edges)
        + "\n"
    )

    file.write(
        "Hub Gene: "
        + hub_gene
        + "\n"
    )

    file.write(
        "Largest Pathway: "
        + largest
        + "\n"
    )

print(
    "\nReport Saved Successfully"
)


# ==========================================================
# END OF PHASE 11
# ==========================================================
