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
        self.low_portion = 0
        self.high_portion = 1
        self.epsilon = 0.001
        self.count = 0
    
    def binarySearch(self, monthToSave=36):#頭金を指定した期間に貯蓄する適切な貯蓄率の値を求める
        st = datetime.datetime.now()
        while self.low_portion <= self.high_portion:
            mid_portion = (self.low_portion + self.high_portion) / 2
            saving_month = self.simulate(mid_portion)
            self.count += 1
            if abs(saving_month-monthToSave) <= self.epsilon:
                ed = datetime.datetime.now()
                time = (ed - st).total_seconds()
                print("{}回のシュミレーションで答えを見つけました。".format(self.count))
                print("シュミレーションに{}秒かかりました。".format(time))
                return round(mid_portion, 5)
            elif saving_month > monthToSave:
                self.low_portion = mid_portion + self.epsilon
            else:
                self.high_potion = mid_portion - self.epsilon
        
        ed_2 = datetime.datetime.now()
        time_2 = (ed_2 - st).total_seconds()
        print("{}回のシュミレーションで答えが見つかりませんでした。".format(self.count))
        print("シュミレーションに{}秒かかりました。".format(time_2))
        return -1      

search = SerchSavingsRate()                                                      
print(search.binarySearch())

search = SerchSavingsRate(10**7, 0.5, 0.01, 100)
print(search.binarySearch())

"""
#A3
class SearchSavingdRateWRaise(SerchSavingsRate):
    def __init__(self, semiAnnualRaise, totalCost = 1000000, portionDownPayment=0.25, interestRate = 0.04, annualSalary = 120000):
        super().__init__(totalCost, portionDownPayment, interestRate, annualSalary)
        self.semiAnnuakRaise = semiAnnualRaise
        self.months = 0
        self.current_saving = 0
        self.totalCost = totalCost
        self.potionDownPayment = portionDownPayment
        self.interestRate = interestRate
        self.annualSalary = annualSalary
        
    def raise_simulate(self, potion_save):
        month_salary = self.annualSalary / 12
        while self.current_saving < self.totalCost * self.potionDownPayment:
            if self.months > 0 and self.months % 6 != 0:
                month_salary += month_salary * self.semiAnnuakRaise
            self.current_saving += month_salary * potion_save + self.current_saving *self.interestRate / 12
            self.months
            onths += 1
            return self.months
        
search = SearchSavingdRateWRaise(0.5).raise_simulate(0.5)
print(search)
search.binarysearch()
"""