def catculator():
    print("--- 🐾 Welcome to the Catculator 🐾 ---")
    print("I can add, subtract, multiply, or divide... for a treat.")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            op = input("Enter operator (+, -, *, /) or 'q' to quit: ").lower()
            
            if op == 'q':
                print("Meow-revoir! 🐱")
                break
                
            num2 = float(input("Enter second number: "))

            # Perform calculations
            if op == '+':
                result = num1 + num2
                comment = "That's a lot of catnip!"
            elif op == '-':
                result = num1 - num2
                comment = "Subtracting? Like my motivation for a bath."
            elif op == '*':
                result = num1 * num2
                comment = "Multiplying faster than kittens in a barn!"
            elif op == '/':
                if num2 == 0:
                    print("Error: You can't divide by zero! That's a catastrophe.")
                    continue
                result = num1 / num2
                comment = "Slicing the tuna precisely."
            else:
                print("Invalid operator! *Hisses*")
                continue

          
            print(f"\nResult: {result}")
            print(f"🐾 {comment}")
            
        except ValueError:
            print("Invalid input! Please enter numbers only. *Swipes paw*")

if __name__ == "__main__":
    catculator()