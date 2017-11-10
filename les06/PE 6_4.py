studentencijfers = [[]]
def gemiddelde_per_student(studentencijfers):
    antwoord= []
    for student in studentencijfers:
        gem= sum(student)/len(student)
        antwoord.append(gem)
    return antwoord

def gemiddelde_van_alle_studenten(studentencijfers):
    som= sum(gemiddelde_per_student(studentencijfers))
    aantal= len(studentencijfers)
    antwoord= som/aantal
    return antwoord