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


def mortgageTable(principal, years, interest, additionalPayment=0, begMonth=0, endMonth=0):
  print("Principal: " + "${:,.2f}".format(principal))
  print("Years of Payment : " + str(years))
  print("Interest: " + "%{:,.2f}".format(interest))
  print("Additional Payment: " + "${:,.2f}".format(additionalPayment))
  print("Month".center(5),  "Payment".center(9),
        "Addtl Pmt". center(15), "Balance".center(15))
  print("".center(5, "-"), "".center(9, "-"),
        "".center(15, "-"), "".center(15, "-"))

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
  if additionalPayment > 0:

    for i in range(1, numberOfMonths + 1):
      if i in range(begMonth - 1, endMonth + 1):

        actualMonths += 1
        interestPayment = balance * monthlyInterest
        totalInterest += interestPayment
        principalPayment = monthlyPayment + additionalPayment - interestPayment
        balance -= principalPayment

        print(str(i).center(5), "${:,.2f}".format(round(monthlyPayment, 2)).center(10), "${:,.2f}".format(
            additionalPayment).center(15), "${:,.2f}".format(round(balance, 2)).center(15))

        if balance < 0:
          break

      else:

        actualMonths += 1
        interestPayment = balance * monthlyInterest
        totalInterest += interestPayment
        principalPayment = monthlyPayment - interestPayment
        balance -= principalPayment

        print(str(i).center(5), "${:,.2f}".format(round(monthlyPayment, 2)).center(
            10), "${:,.2f}".format(0).center(15), "${:,.2f}".format(round(balance, 2)).center(15))

        if balance < 0:
          break
  else:
    for i in range(1, numberOfMonths + 1):

      totalInterest += interestPayment
      actualMonths += 1
      interestPayment = balance * monthlyInterest
      principalPayment = monthlyPayment - interestPayment
      balance -= principalPayment

      print(str(i).center(5), "${:,.2f}".format(round(monthlyPayment, 2)).center(10), "${:,.2f}".format(
          additionalPayment).center(15), "${:,.2f}".format(round(balance, 2)).center(15))

  savedMonths = numberOfMonths - actualMonths
  savedYear = savedMonths // 12
  if additionalPayment > 0:
    print("Monthly Additional Payment: " +
          str("${:,.2f}".format(additionalPayment)))

    print("Months Saved: " + str(savedMonths) + " months" + " or " +
          str(savedYear) + " years and " + str(savedMonths - savedYear * 12) + " months.")

    print("Total Interest Payment Saved: " + str("${:,.2f}".format(
        accumulatedInterest(principal, years, interest) - totalInterest)))


mortgageTable(20000, 4, 4, 0, 0, 0)
