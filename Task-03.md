# Task-03: Automation Testing – Login and Order Flow

##  Scope
Automated testing of login, product interaction, and checkout flow using Selenium and ChromeDriver.

---

##  Test Cases

### 1. Login
- **Positive Case**: Valid credentials →  Redirected to product page.
- **Negative Case**: Invalid credentials →  Error message displayed.

### 2. Product Interaction
- **Add to Cart**:  Item added successfully.
- **Filters**: Sorting works (A–Z, Z–A, Price Low–High, High–Low).

### 3. Checkout Flow
- **Place Order**:  Redirects to form.
- **Form Submission**:  Accepts First Name, Last Name, Zip.
- **Payment Overview**: Displays order details.
- **Cancel Order**:  Returns to product page.
- **Finish Order**:  Confirmation message displayed (*"Your order has been dispatched, and will arrive just as fast as the pony can get there!"*).

---

##  Summary
- All major flows (login, cart, filters, checkout, cancel, finish) automated successfully.
- Confirmation page validated.
- Negative login handled correctly.
- Manual findings (broken links, banner clicks not functional) noted separately in Task‑02.

---

##  Conclusion
Task‑03 demonstrates automation testing using Selenium.  
Both **script (`task_03.py`)** and **report (`Task-03.md`)** are ready for submission.
