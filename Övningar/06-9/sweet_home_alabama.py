import random
import numpy as np
import math
import datetime
import time

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
timeline_dict = {}
running = True

class Person:
    def __init__(self, name, age, dna):
        self.name = name
        self.age = age
        self.dna = dna
        self.retardedness = 0

        self.genes_dict = {"strength": 0, "attack": 0, "agility": 0, "defense": 0, "vitality": 0, "charisma": 0, "stamina": 0, "regeneration": 0, "metabolism": 0, "saturation": 0, "hydration": 0, "communication": 0, "intelligence": 0, "loss_of_limb": 0, "more_dna_mutation": 0, "add_dna_mutation": 0}

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
        self.is_pregnant = False
    def take_substance(self, substance):
        self.substances.append(substance)

def dna_similarity(X, Y):
    similarity = 0
    if len(X) <= len(Y): 
        dna_strands = [X, Y] 
    else: dna_strands = [Y, X]
    for i in range(0, len(dna_strands[0])):
        if dna_strands[0][i] in dna_strands[1]:
            similarity += 1
    return similarity/len(dna_strands[0])

def new_dna_retardedness(p1, p2):
    dna1 = p1.dna.copy()
    dna2 = p2.dna.copy()
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
    retardedness += (alcohol_influence+drug_influence)
    if retardedness > 1:
        retardedness = 1
    new_dna = []
    if (len(dna1)/2).is_integer():
        length = len(dna1)/2
    else:
        ran = random.randint(0, 1)
        if ran: length = (len(dna1)+1)/2
        else: length = (len(dna1)-1)/2
    for _ in range(int(length)):
        new_dna.append(random.choice(dna1))
        dna1.remove(new_dna[-1])
    if (len(dna2)/2).is_integer():
        length = len(dna2)/2
    else:
        ran = random.randint(0, 1)
        if ran: length = (len(dna2)+1)/2
        else: length = (len(dna2)-1)/2
    for _ in range(int(length)):
        new_dna.append(random.choice(dna2))
        dna2.remove(new_dna[-1])

    mutation_chance = random.randint(0, 100)
    number_of_mutations = 0
    if retardedness*100 >= mutation_chance:
        number_of_mutations = math.ceil(max_dna_mutations*drug_influence)
        for _ in range(number_of_mutations):
            ran = random.randint(-max_add_dna_mutations, max_add_dna_mutations)
            if (p1.genes_dict["add_dna_mutation"]+p2.genes_dict["add_dna_mutation"])/2 <= ran:
                #print("Adding mutation...")
                new_dna.append(random.choice(genes_lst)+random.choice(genes_lst)+random.choice(genes_lst)+random.choice(genes_lst)+random.choice(genes_lst))
            else:
                #print("Removing dna")
                new_dna.remove(random.choice(new_dna))
    
    return new_dna, retardedness

def makeChild(partner1, partner2, name, age):
    if partner1.age < 15 or partner2.age < 15:
        print("Parents too young")
    #elif partner1.gender == partner2.gender:
    #    print("Same genders can't make children")
    else:
        if partner1.gender == "female":
            woman = partner1
        else: woman = partner2
        if not timeline_check(woman):
            print(f"Already pregnant! ({get_time_left(woman)})")
            return
        woman.is_pregnant = True
        dna_retardedness = new_dna_retardedness(partner1, partner2)
        ran = random.randint(0, 1)
        if ran == 0:
            new_child = Woman(name, age, dna_retardedness[0])
        else:
            new_child = Woman(name, age, dna_retardedness[0])
        new_child.retardedness = dna_retardedness[1]

        duration = 60*(1+new_child.retardedness)
        add_to_timeline(woman, duration)
        print("Made child")
    return new_child

def random_dna_strains(length):
    genes_dict = {"strength": 0, "attack": 0, "agility": 0, "defense": 0, "vitality": 0, "charisma": 0, "stamina": 0, "regeneration": 0, "metabolism": 0, "saturation": 0, "hydration": 0, "communication": 0, "intelligence": 0, "loss_of_limb": 0, "more_dna_mutation": 0, "add_dna_mutation": 0}
    dna = []
    for _ in range(length):
        dna_strain = random.choice(genes_lst) + random.choice(genes_lst) + random.choice(genes_lst) + random.choice(genes_lst) + random.choice(genes_lst)
        dna.append(dna_strain)
        genes_dict = get_genes_dict(dna_strain, genes_dict)
    return dna, genes_dict

def get_genes_dict(dna_strain, genes_dict):
    match dna_strain[0]:
        case "s" | "a" | "A" | "d":
            match dna_strain[1]:     
                case "s": genes_dict["strength"] += 1
                case "a": genes_dict["attack"] += 1
                case "A": genes_dict["agility"] += 1
                case "d": genes_dict["defense"] += 1
                case "v": genes_dict["vitality"] += 1
                case "c": genes_dict["charisma"] += 1
                case "S": genes_dict["stamina"] += 1
                case "r": genes_dict["regeneration"] += 1
        case "v" | "c" | "S" | "r":
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

def add_to_timeline(event, duration):
    time_when_finished = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    timeline_dict[event] = time_when_finished

def timeline_check(event):
    if event in timeline_dict:
        if not timeline_dict[event] < datetime.datetime.now():
            return False 
    return True

def get_time_left(event):
    return f"{int((timeline_dict[event] - datetime.datetime.now()).total_seconds())} seconds..."

Man("ADAM", 18, random_dna_strains(100)[0])
Woman("EVE", 21, random_dna_strains(200)[0])

while running:
    request = input("[Make child: (M), Shop: (S), Genetics: (G)] ENTER: ").upper()
    match request:
        case "M":
            p1 = input("[(First Parent)] ENTER: ").upper()
            p2 = input("[(Secound Parent)] ENTER: ").upper()
            name = input("[(Name)] ENTER: ").upper()
            makeChild(people[p1], people[p2], name, 0)
        case "S":
            print("Shop")
        case "G":
            request = input("[Compare dna: (C), Statistics: (S) ENTER: ").upper()
            if request == "C":
                p1 = input("[(First person)] ENTER: ").upper()
                p2 = input("[(Secound person)] ENTER: ").upper()
                print(dna_similarity(people[p1].dna, people[p2].dna))
            elif request == "S":
                p = people[input("[(Person)] ENTER: ").upper()]
                for gene in p.genes_dict:
                    print(f"{gene}: {p.genes_dict[gene]}")
