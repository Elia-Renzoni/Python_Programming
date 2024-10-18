#
#
#


class Voto:

    def __init__(self, voto, parziale):
        self.voto = voto
        self.parziale = parziale
    
    def getVoto(self):
        return self.voto
    
    def isParziale(self):
        return self.parziale
