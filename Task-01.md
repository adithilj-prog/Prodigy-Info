### TC_CALC_001
**Description:** Addition of two positive integers  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter 5  
2. Press '+'  
3. Enter 3  
4. Press '='  
**Expected Result:** Display shows 8

### TC_CALC_002
**Description:** Subtraction of two positive integers  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter 5  
2. Press '-'  
3. Enter 4  
4. Press '='  
**Expected Result:** Display shows 1

### TC_CALC_003
**Description:** Multiplication of two positive integers  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter 7  
2. Press '*'  
3. Enter 6
4. Press '='  
**Expected Result:** Display shows 42

### TC_CALC_004
**Description:** Division of two positive integers  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter 20  
2. Press '/'  
3. Enter 4  
4. Press '='  
**Expected Result:** Display shows 5

### TC_CALC_005
**Description:** Addition of two decimal numbers  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter 2.5  
2. Press '+'  
3. Enter 3.5  
4. Press '='  
**Expected Result:** Display shows 6.0

### TC_CALC_006
**Description:** Division involving a negative number  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter -12  
2. Press '/'  
3. Enter 3  
4. Press '='  
**Expected Result:** Display shows -4

### TC_CALC_007
**Description:** Division by zero  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter 9  
2. Press '/'  
3. Enter 0  
4. Press '='  
**Expected Result:** Error message displayed (e.g., "Cannot divide by zero")

### TC_CALC_008
**Description:** Addition with non-numeric input  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter 'abc'  
2. Press '+'  
3. Enter 5  
4. Press '='  
**Expected Result:** Error message displayed (e.g., "Invalid input")

### TC_CALC_009
**Description:** Order of operations (BODMAS)  
**Preconditions:** Calculator is open  
**Test Steps:**  
1. Enter 2  
2. Press '+'  
3. Enter 3  
4. Press '*'  
5. Enter 4  
6. Press '='  
**Expected Result:** Display shows 14  

---
## Summary
This document contains 9 test cases for a simple calculator application, covering:
- Core operations (add, subtract, multiply, divide)
- Special cases (decimals, negative numbers)
- Invalid inputs (division by zero, non-numeric input)
- Order of operations (BODMAS)

All test cases include ID, description, preconditions, steps, and expected results.
