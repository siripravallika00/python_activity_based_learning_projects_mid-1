# ATM Banking System Using Python

## 1. Aim

To write a Python program to develop a simple ATM Banking System that allows the user to deposit money, withdraw money, check the account balance, and exit the program using a while loop and conditional statements.

## 2. Algorithm

1. Start the program.
2. Initialize the account balance to 5000.
3. Initialize the choice to 0.
4. Display the ATM menu:
   - Deposit
   - Withdraw
   - Check Balance
   - Exit
5. Ask the user to enter their choice.
6. If the choice is 1:
   - Enter the deposit amount.
   - If the amount is greater than 0, add it to the balance.
   - Otherwise, display Invalid Amount.
7. If the choice is 2:
   - Enter the withdrawal amount.
   - If the amount is less than or equal to 0, display Invalid Amount.
   - If the amount is less than or equal to the balance, subtract it from the balance.
   - Otherwise, display Insufficient Balance.
8. If the choice is 3, display the current balance.
9. If the choice is 4, display Thank You and exit.
10. If the choice is invalid, display Invalid Choice.
11. Repeat the process until the user selects Exit.
12. Stop the program.

## 3. Flowchart

``` mermaid

flowchart TD
    A([Start]) --> B[Initialize balance = 5000]
    B --> C[Set choice = 0]
    C --> D{Choice != 4?}
    D -- Yes --> E[Display ATM Menu]
    E --> F[/Enter choice/]
    F --> G{Check choice}
    
    G -- 1 Deposit --> H[/Enter deposit amount/]
    H --> I{Amount > 0?}
    I -- Yes --> J[Add amount to balance]
    J --> K[Print Deposit Successful]
    I -- No --> L[Print Invalid Amount]
    
    G -- 2 Withdraw --> M[/Enter withdrawal amount/]
    M --> N{Amount <= 0?}
    N -- Yes --> O[Print Invalid Amount]
    N -- No --> P{Amount <= balance?}
    P -- Yes --> Q[Subtract amount from balance]
    Q --> R[Print Withdrawal Successful]
    P -- No --> S[Print Insufficient Balance]
    
    G -- 3 Check Balance --> T[Display Current Balance]
    G -- 4 Exit --> U[Print Thank You]
    G -- Other --> V[Print Invalid Choice]
    
    K --> D
    L --> D
    O --> D
    R --> D
    S --> D
    T --> D
    U --> D
    V --> D
    
    D -- No --> W([Stop])
```


Sample input:

```
Enter your choice: 1
Enter deposit amount: 1000

Enter your choice: 3

Enter your choice: 2
Enter withdrawal amount: 500

Enter your choice: 3

Enter your choice: 4
```

## 5. Output

Sample output:

```
1. Deposit
2. Withdraw
3. Check balance
4. Exit

Enter your choice: 1
Enter deposit amount: 1000
Deposit successful

1. Deposit
2. Withdraw
3. Check balance
4. Exit

Enter your choice: 3
Current balance = 6000.0

1. Deposit
2. Withdraw
3. Check balance
4. Exit

Enter your choice: 2
Enter withdrawal amount: 500
Withdrawal successful

1. Deposit
2. Withdraw
3. Check balance
4. Exit

Enter your choice: 3
Current balance = 5500.0

1. Deposit
2. Withdraw
3. Check balance
4. Exit

Enter your choice: 4
Thank you
```
