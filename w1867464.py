# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210380
# UOW ID:w1867464
# Date:2021/12/7

new = []
credit = []
out=0
progress = 0
trailer = 0
retriver = 0
exclude = 0
mode=int(input("Enter mode 1 for student version or 2 for staff version: "))
while True:
 if mode==1:
    try:
        credit_pass = int(input("Please enter your credits at pass: "))
        if credit_pass not in range(0, 121, 20):
            print("Out of range")
            continue

        credit_defer = int(input("Please enter your credits at defer: "))
        if credit_defer not in range(0, 121, 20):
            print("Out of range")
            continue

        credit_fail = int(input("Please enter your credits at fail: "))
        if credit_fail not in range(0, 121, 20):
            print("out of range")
            continue

        total = credit_fail + credit_defer + credit_pass

        if total != 120:
            print("Total incorrect")
            print(' ')
            continue

        elif credit_pass == 120 and credit_defer == 0 and credit_fail == 0:
            print("progress")
            exit()

        elif credit_pass == 100 and (credit_defer == 20 or credit_defer == 0) and (
                credit_fail == 0 or credit_fail == 20):
            print("Progress (module trailer)")
            exit()


        elif (
                credit_pass == 80 or credit_pass == 60 or credit_pass == 40 or credit_pass == 20 or credit_pass == 0) and (
                credit_defer == 20 or credit_defer == 40 or credit_defer == 60 or credit_defer == 80 or credit_defer == 100 or credit_defer == 120 or credit_defer == 0) and (
                credit_fail == 20 or credit_fail == 40 or credit_fail == 60 or credit_fail == 0):
            print("Module retriever")
            exit()

        elif (credit_pass == 20 or credit_pass == 0 or credit_pass == 40) and (
                credit_defer == 20 or credit_defer == 0 or credit_defer==40) and (
                credit_fail == 80 or credit_fail == 100 or credit_fail == 120):
            print("Exclude")
            exit()
    except ValueError:
        print('integer required')
        print('')
        continue
 else:

  print("Staff Version with histogram")
  print('')
  def rangeChecker(inputCredit):
    if inputCredit not in range(0, 121, 20):
        print("Out of range")
        return False
    return True

  def getUserInput():
      global progress, trailer, retriver, exclude,out
      try:
          while True:
              credit_pass = int(input("Enter your total PASS credits: "))
              if rangeChecker(credit_pass):
                  break

          while True:
              credit_defer = int(input("Enter your total DEFER credits: "))
              if rangeChecker(credit_defer):
                  break

          while True:
              credit_fail = int(input("Enter your total FAIL credits: "))
              if rangeChecker(credit_fail):
                  break
          new.append([credit_pass, credit_defer, credit_fail])
          if credit_pass==120 and credit_defer==0 and credit_fail==0:
              print("progress")
              progress += 1
              out += 1
              credit.append('progress')
              print('')
          if credit_pass==100 and (credit_defer==20 or credit_defer==0) and (credit_fail==0 or credit_fail==20):
              print("Progress (module trailer)")
              trailer += 1
              out += 1
              credit.append('Progress (module trailer)')
              print('')
          if (credit_pass==80 or credit_pass==60 or credit_pass==40 or credit_pass==20 or credit_pass==0) and (
                  credit_defer==20 or credit_defer==40 or credit_defer==60 or credit_defer==80 or credit_defer==100 or credit_defer==120 or credit_defer==0) and (
                  credit_fail==20 or credit_fail==40 or credit_fail==60 or credit_fail==0):
              print("Module retriever")
              retriver += 1
              out += 1
              credit.append('Module retriever')
              print('')
          if (credit_pass==20 or credit_pass==0 or credit_pass==40) and (
                  credit_defer==20 or credit_defer==0 or credit_defer==40) and (
                  credit_fail==80 or credit_fail==100 or credit_fail==120):
              print("Exclude")
              exclude += 1
              out += 1
              credit.append('Exclude')
              print('')
          if credit_pass + credit_defer + credit_fail != 120:
              print("Total incorrect")
              getUserInput()



      except ValueError:
          print("Integer required")
          credit_pass = 0
          credit_defer = 0
          credit_fail = 0
          getUserInput()



# Part 1 - Horizontal Histogram--------------------------------

  def Horizontalhisto():
    totalOutcomes = progress + trailer + retriver + exclude

    print("\n-----------------Horizontal Histogram-----------------")
    print(f"Progress {progress}\t: {progress * '*'}")
    print(f"Trailer {trailer}\t: {trailer * '*'}")
    print(f"Retriever {retriver}\t: {retriver * '*'}")
    print(f"Exclude {exclude}\t: {exclude * '*'}")
    print(totalOutcomes, "outcomes in total.")
    print("--------------------------------------------------------")


# Part 2 - Vertical Histogram----------------------------------

  def verticalhisto():
    print()
    global progress, trailer, retriver, exclude
    outputs = [progress, trailer, retriver, exclude]
    maximum = max(outputs)
    print('Vertical Histogram')
    programms = 'Progress | Trailer | Retriever | Exclude'
    print(programms)
    for i in range(maximum):
        a = []
        for star in outputs:
            if i < star:
                a.append('*')
            else:
                a.append(' ')
        print(f'{a[0]:>4}{a[1]:>11}{a[2]:>11}{a[3]:>11}')         #line 161-167 referenced by https://stackoverflow.com/questions/43563672/python-plotting-a-histogram-downward
    print("--------------------------------------------------------")


# Part 3 -------------------------------------------------------

  def datalist():
    print()
    for x in range(0, out):
        newl = str(new[x])[1:-1]  # To remove brackets from the list referenced : https://stackoverflow.com/questions/13207697/how-to-remove-square-brackets-from-list-in-python
        print(credit[x], ' - ', newl)
    print("--------------------------------------------------------")


# Part 4 -TextFile-----------------------------------------------

  def TextFile():
      print("..........Text File...................")

      with open('textfile.txt', 'w') as output:
          for x in range(0, out):
              newl = str(new[x])[1:-1]
              output.write(credit[x] + '-' + newl + '\n')


      with open('textfile.txt', 'r') as f:
          f_contents = f.read()
          print(f_contents)


# --------------------------------------------------------------

  def resultsMenu():
    print("1-Horizontal Histogram")
    print("2-vertical Histogram")
    print("3-list ")
    print("4-Text File")
    menu = 0
    while True:
        menu = input("choose menu(1-4)/ 'q' to exit:")
        if menu=="1":
            Horizontalhisto()
        elif menu=="2":
            verticalhisto()
        elif menu=="3":
            datalist()
        elif menu=="4":
            TextFile()
        elif menu=="q":
            exit()
        else:
            print("Invalid selection")

  while True:
    getUserInput()
    wantLoop = 0
    while wantLoop != 'q' and wantLoop != 'y':
        wantLoop = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        print('')
    if wantLoop == 'q':
        resultsMenu()
        break