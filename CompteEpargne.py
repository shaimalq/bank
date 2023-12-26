from compte import* 
class CompteEpargne(compte):
    def __init__(self ,interet,num,proprietaire, sold,date_ouverture):
        super().__init__(num,proprietaire, sold,date_ouverture)
        self.__interet = interet

    @property
    def interet(self):
        return self.__interet
        
    def __str__(self) :
        return f"interet:{self.__interet}"
        