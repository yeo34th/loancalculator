def paymentCalculator(principal, years, interest):

  numberOfMonths = years * 12
  adjustedInterest = interest / 100
  monthlyInterest = adjustedInterest / 12
  monthlyPayment = principal*(monthlyInterest*(1+monthlyInterest)**numberOfMonths / ((1+monthlyInterest)**numberOfMonths-1))
  return round(monthlyPayment, 2)

def accumulatedInterest(principal, years, interest):
  numberOfMonths = years * 12
  adjustedInterest = interest / 100
  monthlyInterest = adjustedInterest / 12
  monthlyPayment = principal*(monthlyInterest*(1+monthlyInterest)**numberOfMonths / ((1+monthlyInterest)**numberOfMonths-1))
  totalInterest = 0
  totalInterest = monthlyPayment * numberOfMonths - principal
  return(totalInterest)

def interestComparison(principal, years, begInterest, endInterest, interval):
  print("Principal: " + "${:,.2f}".format(principal))
  print("Years of Payment : " + str(years))
  for interest in range(begInterest*int(1 / interval), int(1 / interval) * endInterest + 1):
    actualInterest = interest/(1/interval)
    print("%{:,.2f}".format(actualInterest).ljust(10) + "${:,.2f}".format(paymentCalculator(principal, years, actualInterest)).ljust(10) + "${:,.2f}".format(accumulatedInterest(principal, years, actualInterest)))


interestComparison(25000, 5, 3, 5, .15)
