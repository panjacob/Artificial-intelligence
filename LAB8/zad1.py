from LAB8.evolution import generate_genotype, genotype_to_xy, xy_to_genotype

SIZE = 128

genotype = generate_genotype(size=SIZE)
x, y = genotype_to_xy(genotype)
