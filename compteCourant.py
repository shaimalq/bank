from compte import*
class CompteCourant (compte):
    def __init__(self,montantDecouvertAutoise,num, proprietaire, sold,date_ouverture):
        super().__init__(num,proprietaire, sold,date_ouverture)
        self.montantDecouvertAutoise = montantDecouvertAutoise
    @property
    def montantDecouvertAutoise(self):
        return self.montantDecouvertAutoise
    
    def __str__(self) :
        return f" montant_Decouvert_Autoise:{self.montantDecouvertAutoise}"
    
