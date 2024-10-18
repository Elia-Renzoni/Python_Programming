#
#
#

class Materia:
    '''
        Classe che contiene l'entità materia con attributi
        - docente.
        - anno.
        - semestre.
        - cfu.
    '''
    def __init__(self, docente, anno, semestre, cfu, nomeCorso):
        self.docente = docente
        self.anno = anno
        self.semestre = semestre
        self.cfu = cfu
        self.nomeCorso = nomeCorso
    
    def getDocente(self):
        return self.docente
    
    def getAnno(self):
        return self.anno
    
    def getSemestre(self):
        return self.semestre
    
    def getCFU(self):
        return self.cfu
    
    def getNomeCorso(self):
        return self.nomeCorso