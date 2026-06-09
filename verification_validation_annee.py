# ========== R2.10 - Gestion de Projets et Organisation ==========
# ===== TP1 - Tableaux Kanban, GitHub & GitHub Projects =====

# Imports nécessaires
from calcul_moyenne_generale import calcul_moyenne

# Fonction permettant de vérifier le semestre
def verifier_semestre():
    print("=== Vérification du semestre ===")

    notes, moyenne = calcul_moyenne()

    competences_validees = sum(1 for note in notes if note >= 10)

    absences = int(input("Nombre d'absences non justifiées : "))

    condition1 = competences_validees >= 4
    condition2 = all(note >= 8 for note in notes if note < 10)
    condition3 = absences <= 5

    if condition1 and condition2 and condition3:
        print(f"✅ Semestre validé avec {moyenne:.2f}/20")
        return True
    else:
        print(f"❌ Semestre non validé ({moyenne:.2f}/20)")
        return False

# Fonction permettant de valider l'année
def verifier_annee():
    print("\n=== Vérification de l'année ===")

    semestre1 = verifier_semestre()
    semestre2 = verifier_semestre()

    if semestre1 and semestre2:
        print("\n🎉 Année validée !")
    else:
        print("\n❌ Année non validée")