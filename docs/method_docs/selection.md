### Parallel Hill Climber 
- A hill climber algorithm is a local search algorithm that optimizes a problem using incremental changes.
    - It starts with an arbitrary solution (parent), and then at each generation, it mutates the parent to create a child. If the 
    child has a higher fitness than the parent, then it replaces the parent. 
    - This continues for a set number of generations and the parent is the creature with the highest fitness.
- To parallelize the hill climber algorithm, in each generation, there is a set population size and they all perform hill climbing
    - Each family is unknown to each other so the parents do not influence the mutation of each other's children
    - At the end of the set number of generations, the parent with the highest fitness is determined the best creature. 