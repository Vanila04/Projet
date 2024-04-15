from itertools import product

def fonction_logique(A, B,C):
    # Exemple de fonction:(A AND B) OR (not A AND C)
    return  (A and B) or (not A and C)

def generer_table_de_verite(func):
    variables = [0, 1]  # 0 pour faux, 1 pour vrai
    table = []

    for values in product(variables, repeat=3):
        resultat= func(*values)
        table.append((*values, resultat))
    
    return table

def forme_canonique(table):
    fnd = []
    fnc = []

    for ligne in table:
        A, B, C, resultat = ligne
        if resultat:
            fnd.append(f"({'A' if A else 'notA'} AND {'B' if B else 'notB'} AND {'C' if C else 'notC'})")
        else:
            fnc.append(f"({'A' if not A else 'notA'} OR {'B' if not B else 'notB'} OR {'C' if not C else 'notC'})")
    
    # Joindre les expressions avec OR pour FND et AND pour FNC
    fnd_expression = " OR ".join(fnd)
    fnc_expression = " AND ".join(fnc)

    return fnd_expression, fnc_expression

# Génération de la table de vérité
table = generer_table_de_verite(fonction_logique)

# Affichage de la table de vérité
print("A   B   C   | F(A,B,C)")
print("------------------")
for ligne in table:
    print(f"{ligne[0]} | {ligne[1]} | { ligne[2]} | {ligne[3]}")

# Calcul des formes canoniques
fnd, fnc = forme_canonique(table)

print("\nForme Normale Disjonctive (FND):", fnd)

print("Forme Normale Conjonctive (FNC):", fnc)
