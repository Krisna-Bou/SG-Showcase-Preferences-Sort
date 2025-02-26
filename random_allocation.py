import random
from collections import defaultdict

def allocate_dancers(dancers, performances):
    allocation = defaultdict(list)
    remaining_slots = performances.copy()
    dancer_allocations = defaultdict(list)
    
    # Shuffle dancer list to ensure fairness
    dancer_list = list(dancers.keys())
    random.shuffle(dancer_list)
    
    for dancer in dancer_list:
        #Each dancers preferences
        for preference in dancers[dancer]:
            #If there's still slots available for the preference and the dancer has less than 3 performances
            if remaining_slots[preference] > 0 and len(dancer_allocations[dancer]) < 3:
                allocation[preference].append(dancer)
                dancer_allocations[dancer].append(preference)
                remaining_slots[preference] -= 1
    
    return allocation