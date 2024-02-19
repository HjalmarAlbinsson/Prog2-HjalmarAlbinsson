from datetime import datetime


class Student:
    skola = "Åva gymnasium"
    def __init__(self, namn, personnr):
        self.__namn: str = namn
        self.__personnr: int = personnr

    def get_namn(self):
        return self.__namn
    
    def get_alder(self):
        today = datetime.today().strftime("%Y%m%d")
        if self.__personnr[2:4] > today[4:6]:
            return today[2:4] - self.__personnr[:2] - 1
        if self.__personnr[2:4] == today[4:6]:
            if self.__personnr[4:6] <= today[6:8]:
                return today[2:4] - self.__personnr[:2]
            else:
                return today[2:4] - self.__personnr[:2] - 1
        else:
            return today[2:4] - self.__personnr
        
        
        today[2:4] - self.__personnr[:2]

        year = self.__personnr[:2]
        month = self.__personnr[2:4]
        day = self.__personnr[4:6]

        print(year, month, day)

Student("alex", "050425").get_alder()
