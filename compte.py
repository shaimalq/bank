class compte:
    def __init__(self ,num, proprietaire, solde,date_ouverture):
        self._num = num
        self._proprietaire = proprietaire
        self._solde = solde
        self._date_ouverture = date_ouverture

    @property
    def num(self):
        return self._num
    @property
    @num.setter
    def num(self,num):
        return self._num == num
    
    @property
    def proprietaire(self):
        return self._proprietaire
    @property
    @proprietaire.setter
    def proprietaire(self,proprietaire):
        return self._proprietaire == proprietaire
    
    @property
    def solde(self):
        return self._num
    @property
    @solde.setter
    def solde(self,solde):
        return self._solde== solde
    
    @property
    def date_ouverture(self):
        return self._date_ouverture
    @property
    @date_ouverture.setter
    def date_ouverture(self,date_ouverture):
        return self._date_ouverture == date_ouverture
    
    def __str__(self) :
        return f"numero:{self._num},solde:{self._solde} ,proprietaire{self._proprietaire},date d'overtures{self._date_ouverture}"