# ========== R2.10 - Gestion de Projets et Organisation ==========
# ===== TP1 - Tableaux Kanban, GitHub & GitHub Projects =====

def calcul_moyenne():
    liste_notes = []

    for i in range(6):
        note = float(input(f"Entrez la moyenne de votre UE {i+1} : "))
        liste_notes.append(note)

    moyenne_generale = sum(liste_notes) / len(liste_notes)

    return liste_notes, moyenne_generale
