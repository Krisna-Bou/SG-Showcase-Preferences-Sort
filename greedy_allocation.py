import random
from collections import defaultdict

def allocate_dancers(dancers, performances):
    allocation = defaultdict(list)
    remaining_slots = performances.copy()
    dancer_allocations = defaultdict(list)
    
    # Sort dancers by the number of preferences (fewest preferences first for fairness)
    sorted_dancers = sorted(dancers.keys(), key=lambda d: len(dancers[d]))
    
    for dancer in sorted_dancers:
        for preference in dancers[dancer]:
            if remaining_slots[preference] > 0 and len(dancer_allocations[dancer]) < 3:
                allocation[preference].append(dancer)
                dancer_allocations[dancer].append(preference)
                remaining_slots[preference] -= 1
    
    return allocation
