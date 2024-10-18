#
#
#


class Libretto:

    def __init__(self):
        self.inMemoryStore = dict()
        self.pointer = open("libretto.txt", "w")

    def addEsame(self, materia, voto):
        if materia in self.inMemoryStore.keys():
            return False
        self.inMemoryStore[materia] = voto
        self.pointer.write(f"{materia.getNomeCorso()}, {materia.getDocente()}, {materia.getAnno()}, {materia.getSemestre()}, {materia.getMatricola()}, {voto.getVoto()}")
        return True

    def removeEsame(self, materia):
        if materia in self.inMemoryStore.keys():
            del self.inMemoryStore[materia]
            return True
        return False

l = Libretto()
