#
#
#


class Studente:
    '''
        Classe che contiene l'entità studente con attributi:
        - nome
        - congome
        - anno corso
        - facoltà
    '''
    def __init__(self, nome, cognome, annoCorso, facolta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.annoCorso = annoCorso
        self.facolta = facolta
        self.matricola = matricola
    
    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome
    
    def getAnnoCorso(self):
        return self.annoCorso
    
    def getFacolta(self):
        return self.facolta
    
    def getMatricola(self):
        return self.matricola
