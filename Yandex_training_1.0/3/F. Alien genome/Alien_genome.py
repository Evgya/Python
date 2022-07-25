def get_closeness_of_genomes(first_genome, second_genome):
    first_genome_basis = tuple(zip(first_genome, first_genome[1:]))
    second_genome_basis = set(zip(second_genome, second_genome[1:]))
    return len(
        tuple(filter(lambda x: x in second_genome_basis, first_genome_basis))
        )

print(get_closeness_of_genomes(input(), input()))
