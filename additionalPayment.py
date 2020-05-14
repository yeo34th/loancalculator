def paymentCalculator(principal, years, interest):

  numberOfMonths = years * 12
  adjustedInterest = interest / 100
  monthlyInterest = adjustedInterest / 12
  monthlyPayment = principal * (monthlyInterest * (1 + monthlyInterest)
                                ** numberOfMonths / ((1 + monthlyInterest)**numberOfMonths - 1))
  return round(monthlyPayment, 2)


def accumulatedInterest(principal, years, interest):
  numberOfMonths = years * 12
  adjustedInterest = interest / 100
  monthlyInterest = adjustedInterest / 12
  monthlyPayment = principal * (monthlyInterest * (1 + monthlyInterest)
                                ** numberOfMonths / ((1 + monthlyInterest)**numberOfMonths - 1))
  totalInterest = 0
  totalInterest = monthlyPayment * numberOfMonths - principal
  return(totalInterest)

def additionalPayment(principal, years, interest, additionalPayment=0, begMonth=0, endMonth=0):

  numberOfMonths = years * 12
  if endMonth == 0:
    endMonth = numberOfMonths
  adjustedInterest = interest / 100
  monthlyInterest = adjustedInterest / 12
  monthlyPayment = principal * (monthlyInterest * (1 + monthlyInterest)
                                ** numberOfMonths / ((1 + monthlyInterest)**numberOfMonths - 1))
  interestPayment = principal * monthlyInterest
  principalPayment = monthlyPayment - interestPayment
  totalInterest = 0
  balance = principal
  actualMonths = 0
  for i in range(1, numberOfMonths + 1):
    if i in range(begMonth - 1, endMonth + 1):
      actualMonths += 1
      interestPayment = balance * monthlyInterest
      totalInterest += interestPayment
      principalPayment = monthlyPayment + additionalPayment - interestPayment
      balance -= principalPayment
      if balance < 0:
        break
    else:
      actualMonths += 1
      interestPayment = balance * monthlyInterest
      totalInterest += interestPayment
      principalPayment = monthlyPayment - interestPayment
      balance -= principalPayment
      if balance < 0:
        break

  savedMonths = numberOfMonths - actualMonths
  savedYear = savedMonths // 12

  return str("${:,.2f}".format(additionalPayment)).center(10) + " ".join([str(savedMonths), "months"]).center(15) + str("${:,.2f}".format(totalInterest)).center(25) + str("${:,.2f}".format(accumulatedInterest(principal, years, interest) - totalInterest)).center(20)


def additionalPmtComparison(principal, years, interest, startingPayment, endingPayment, interval):

  print("Principal: " + "${:,.2f}".format(principal))
  print("Years of Payment : " + str(years))
  print("Interest Rate: " + "%{:,.2f}".format(interest))
  print("Monthly Payment: " +
        "%{:,.2f}".format(paymentCalculator(principal, years, interest)))
  print("Total interst paid at maturity: " +
        "%{:,.2f}".format(accumulatedInterest(principal, years, interest)))
  print("Additional Payment Range: " + "${:,.2f}".format(startingPayment) + " - " +
        "${:,.2f}".format(endingPayment) + " at " + "${:,.2f}".format(interval) + " interval")
  print("")
  print("Addtl Pmt".center(10),  "Months Saved".center(15),
        "Total Interest Paid". center(25), "Interest Saved". center(20))
  print("".center(10, "-"), "".center(15, "-"),
        "".center(25, "-"),  "".center(20, "-"))

  for payment in range(startingPayment, endingPayment + 1, interval):
    print(additionalPayment(principal, years, interest, payment, 0, 0))


additionalPmtComparison(300000, 30, 3, 100, 3000, 100)
