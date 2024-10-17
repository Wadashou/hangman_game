class SimulateSavings:
  def __init__(self, totalCost = 1000000, portionDownPayment=0.25, interestRate = 0.04, annualSalary = 120000):
    self.総額 =  totalCost
    self.頭金割合 = portionDownPayment
    self.年利 = interestRate
    self.年収 = annualSalary

  def __str__(self):
    return ",".join(map(str, [self.総額, self.頭金割合, self.年利, self.年収]))

  def simulate(self, 貯蓄率=0.1):
    貯蓄額 = 0
    貯蓄月数=0
    while(self.頭金割合*self.総額>貯蓄額):
      貯蓄額+=self.年収*貯蓄率/12+貯蓄額*self.年利/12
      貯蓄月数+=1

    return 貯蓄月数
