keep_going = 'y'
#Validate it
#if good - proceed
#if not - don't proceed, ask user if they want to do it again, if yes, repeat process
#Get user input
        
while keep_going == 'y':
        Num1 = (input('Enter your first number: '))
        print(Num1)
        if (Num1.isnumeric) == False:
                Num1 = (input('Please enter a number this time: '))
        else:
                while keep_going == 'y':
                        Num2 = (input('Enter your second number: '))
                        if (Num2.isnumeric) == False:
                                Num2= (input('Please enter a number this time: '))
                        else:
                                        while keep_going == 'y':
                                                Op = input('Enter your operation (+,-,/,*,%): ')
                                                if Op == '+':
                                                    print(int(Num1) + int(Num2))
                                                    keep_going = input('Do you need another calculation? (Enter y for yes): ')
                                                elif Op == '-':
                                                    print(int(Num1) - int(Num2))
                                                    keep_going = input('Do you need another calculation? (Enter y for yes): ')
                                                elif Op == '/':
                                                    print(int(Num1) / int(Num2))
                                                    keep_going = input('Do you need another calculation? (Enter y for yes): ')
                                                elif Op == '*':
                                                    print(int(Num1) * int(Num2))
                                                    keep_going = input('Do you need another calculation? (Enter y for yes): ')
                                                elif Op == '%':
                                                    print((int(Num1))/100 * int(Num2))
                                                    keep_going = input('Do you need another calculation? (Enter y for yes): ')        
                                                else:
                                                    print('Please enter a correct operation(+,-,/,*,%): ')




