from abc import ABC, abstractmethod

# Kelas abstract
class AlatMusik(ABC):

    @abstractmethod
    def bermain(self):
        pass

    @abstractmethod
    def jenis_suara(self):
        pass

    def info(self):
        print("Saya adalah alat musik.")

class Gitar(AlatMusik):
    def bermain(self):
        print("Gitar dimainkan dengan memetik senar.")

    def jenis_suara(self):
        print("Suara gitar: Melodi lembut atau petikan yang kuat.")

class Piano(AlatMusik):
    def bermain(self):
        print("Piano dimainkan dengan menekan tuts.")

    def jenis_suara(self):
        print("Suara piano: Nada harmonis yang kaya.")

class Drum(AlatMusik):
    def bermain(self):
        print("Drum dimainkan dengan memukul membran.")

    def jenis_suara(self):
        print("Suara drum: Ritme yang kuat dan dinamis.")


gitar = Gitar()
gitar.info()
gitar.bermain()
gitar.jenis_suara()

print()  

piano = Piano()
piano.info()
piano.bermain()
piano.jenis_suara()

print() 

drum = Drum()
drum.info()
drum.bermain()
drum.jenis_suara()
