import random
import numpy as np
import math

max_dna_mutations = 10

max_add_dna_mutations = 10
max_more_dna_mutations = 10
max_height = 10
max_hunger = 10
max_thirst = 10
max_metabolism = 10
max_communication = 10
max_regeneration = 10
max_loss_of_limb = 10

max_skills = 100

people = {}
genes_lst = ["s", "a", "A", "d", "v", "c", "S", "r"]

class Person:
    def __init__(self, name, age, dna):
        self.name = name
        self.age = age
        self.dna = dna
        self.retardedness = 0

        self.add_dna_mutation = 0
        self.more_dna_mutation = 0
        self.loss_of_limb = 0
        self.communication = 0
        self.intelligence = 0
        self.height = 0
        self.hunger = 0
        self.thirst = 0
        self.metabolism = 0

        self.strength = 0
        self.agility = 0
        self.attack = 0
        self.defense = 0
        self.vitality = 0
        self.charisma = 0
        self.stamina = 0
        self.regeneration = 0
        people[name] = self
            
class Man(Person):
    def __init__(self, name, age, dna):
        super().__init__(name, age, dna)
        self.gender = "male"
        
class Woman(Person):
    def __init__(self, name, age, dna):
        super().__init__(name, age, dna)
        self.gender = "female"
        self.substances = []
    def take_substance(self, substance):
        self.substances.append(substance)

def dna_similarity(X, Y):
    similarity = 0
    dna_strands = (X, Y)
    for i in range(0, len(dna_strands[0])):
        if dna_strands[0][i] == dna_strands[1][i]:
            similarity += 1
            print(dna_strands[0][i])
    return similarity/len(dna_strands[0])

def new_dna_retardedness(p1, p2):
    dna1 = p1.dna
    dna2 = p2.dna
    retardedness = dna_similarity(dna1, dna2)
    if type(p1).__name__ == "Woman": 
        Woman = p1
    else: 
        Woman = p2
    alcohol_influence = 0
    drug_influence = 0
    for substance in Woman.substances:
        if substance == "Beer":
            alcohol_influence += 0.05
        elif substance == "Champagne":
            alcohol_influence += 0.075
        elif substance == "Vodka":
            alcohol_influence += 0.10
        elif substance == "Marijuana":
            drug_influence += 0.15
        elif substance == "Cocaine":
            drug_influence += 0.20
    retardedness *= (1+alcohol_influence+drug_influence)
    if retardedness > 1:
        retardedness = 1
    new_dna = []
    if (len(dna1)/2).is_integer():
        ran = random.randint(0, 1)
        if ran: length = (len(dna1)+1)/2
        else: length = (len(dna1)-1)/2
    else:
        length = len(dna1)/2
    for _ in range(int(length)):
        new_dna += random.choice(dna1)
    if (len(dna2)/2).is_integer():
        ran = random.randint(0, 1)
        if ran: length = (len(dna2)+1)/2
        else: length = (len(dna2)-1)/2
    else:
        length = len(dna2)/2
    for _ in range(int(length)):
        new_dna += random.choice(dna2)

    mutation_chance = random.randint(0, 100)
    number_of_mutations = 0
    if retardedness*100 >= mutation_chance:
        number_of_mutations = math.ceil(mutation_chance/max_dna_mutations*drug_influence)
        for i in range(number_of_mutations):
            ran = random.randint(-max_add_dna_mutations, max_add_dna_mutations)
            if (p1.add_dna_mutation+p1.add_dna_mutation)/2 <= ran:
                new_dna.append(random.choice(genes_lst)+random.choice(genes_lst)+random.choice(genes_lst)+random.choice(genes_lst)+random.choice(genes_lst))
            else:
                new_dna.remove[random.choice(new_dna)]
    
    return new_dna, retardedness

def makeChild(partner1, partner2, name, age):
    if partner1.age < 13 or partner2.age < 13:
        print("Parents too young")
    #elif partner1.gender == partner2.gender:
    #    print("Same genders can't make children")
    else:
        dna_retardedness = new_dna_retardedness(partner1, partner2)
        ran = random.randint(0, 1)
        if ran == 0:
            new_child = Man(name, age, f"{dna_retardedness[0]}")
        else:
            new_child = Woman(name, age, f"{dna_retardedness[0]}")
        new_child.retardedness = dna_retardedness[1]
    return new_child

def random_dna_strains(length):
    genes_dict = {"strength": 0, "attack": 0, "agility": 0, "defense": 0, "vitality": 0, "charisma": 0, "stamina": 0, "regeneration": 0, "metabolism": 0, "saturation": 0, "hydration": 0, "communication": 0, "intelligence": 0, "loss_of_limb": 0, "more_dna_mutation": 0, "add_dna_mutation": 0}
    dna = []
    for _ in range(length):
        dna_strain = random.choice(genes_lst) + random.choice(genes_lst) + random.choice(genes_lst) + random.choice(genes_lst) + random.choice(genes_lst)
        dna.append(dna_strain)
        genes_dict = get_genes_dict(dna_strain, genes_dict)
    print(genes_dict)
    return dna

def get_genes_dict(dna_strain, genes_dict):
    match dna_strain[0]:
        case "s", "a", "A", "d":
            match dna_strain[1]:     
                case "s": genes_dict["strength"] += 1
                case "a": genes_dict["attack"] += 1
                case "A": genes_dict["agility"] += 1
                case "d": genes_dict["defense"] += 1
                case "v": genes_dict["vitality"] += 1
                case "c": genes_dict["charisma"] += 1
                case "S": genes_dict["stamina"] += 1
                case "r": genes_dict["regeneration"] += 1
        case "v", "c", "S", "r":
            match dna_strain[1]:
                case "s": genes_dict["metabolism"] += 1
                case "a": genes_dict["saturation"] += 1
                case "A": genes_dict["hydration"] += 1
                case "d": genes_dict["communication"] += 1
                case "v": genes_dict["intelligence"] += 1
                case "c": genes_dict["loss_of_limb"] += 1
                case "S": genes_dict["more_dna_mutation"] += 1
                case "r": genes_dict["add_dna_mutation"] += 1
    return genes_dict

Woman("Jakob", 21, random_dna_strains(50))
Man("Alexander", 18, random_dna_strains(50))
makeChild(people["Jakob"], people["Alexander"], "b1", 18)
print(dna_similarity(people["Jakob"].dna, people["Alexander"].dna))
