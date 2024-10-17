from simulatesavings import SimulateSavings
import datetime


#A1
research = SimulateSavings()
print(research.__str__())
print(research.simulate())
#print(research.simulate(0.5))

#A2
class SerchSavingsRate(SimulateSavings):
    def __init__(self, totalCost = 1000000, portionDownPayment=0.25, interestRate = 0.04, annualSalary = 120000):
        super().__init__(totalCost, portionDownPayment, interestRate, annualSalary)
        self.potionToSave = 0
        self.low_potion = 0
        self.high_potion = 1
        self.epsilon = 0.001
        self.count = 0
    
    def binarySearch(self, monthToSave=36):#頭金を指定した期間に貯蓄する適切な貯蓄率の値を求める
        st = datetime.datetime.now()
        while self.low_potion <= self.high_potion:
            mid_potion = (self.low_potion + self.high_potion) / 2
            saving_month = self.simulate(mid_potion)
            self.count += 1
            if abs(saving_month-monthToSave) <= self.epsilon:
                ed = datetime.datetime.now()
                time = (ed - st).total_seconds()
                print("{}回のシュミレーションで答えを見つけました。".format(self.count))
                print("シュミレーションに{}秒かかりました。".format(time))
                return round(mid_potion, 5)
            elif saving_month > monthToSave:
                self.low_potion = mid_potion + self.epsilon
            else:
                self.high_potion = mid_potion - self.epsilon
        
        ed_2 = datetime.datetime.now()
        time_2 = (ed_2 - st).total_seconds()
        print("{}回のシュミレーションで答えが見つかりませんでした。".format(self.count))
        print("シュミレーションに{}秒かかりました。".format(time_2))
        return -1      

search = SerchSavingsRate()                                                      
print(search.binarySearch())

search = SerchSavingsRate(10**7, 0.5, 0.01, 100)
print(search.binarySearch())

search_2 = SerchSavingsRate(10000000, 0.3, 0.1, 15000000)
print(search_2.binarySearch())


research = SimulateSavings()
months_needed = research.simulate(0.6565)
print(months_needed)

months_needed_2 = search_2.simulate(0.05771)
print(months_needed_2)
