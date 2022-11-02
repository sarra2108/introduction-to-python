#question3:
def notef(devoirMoyenne,partiel,examen):
    note=devoirMoyenne*25/100+partiel*25/100+examen*50/100
    return note
note=notef(100,100,100)
note2=notef(200,300,100)
print(note)
print(note2)
