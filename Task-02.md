# Task-02: QA Testing Report – E-Commerce Demo Site

## ✅ Overview
This report documents the functional testing performed on the provided demo e-commerce site.  
The focus was on **search**, **cart**, **checkout**, **navigation links**, and **banner images**.

---

##  Test Cases and Results

### 1. Search Bar
- **Steps**: Enter product name in search bar → press Enter.
- **Expected Result**: Relevant product results displayed.
- **Actual Result**: No action triggered, search not functional.
- **Bug Note**: Search feature broken.

---

### 2. Add to Cart
- **Steps**: Select product → click "Add to Cart".
- **Expected Result**: Product added, cart count updated.
- **Actual Result**: Works as expected.

---

### 3. Place Order
- **Steps**: Add product → click "Place Order".
- **Expected Result**: Prompt for user details (address, payment) before confirmation.
- **Actual Result**: Direct success message shown: *"Order placed successfully, we have sent you email"*.
- **Bug Note**: Checkout validation missing.

---

### 4. Navigation Links
- **Home / Online Store / Helpful Links / Partners**
  - **Expected Result**: Redirect to respective pages.
  - **Actual Result**: Hover works, but click does not navigate anywhere.

- **Clothing**
  - **Expected Result**: Redirect to clothing category page.
  - **Actual Result**:  Page Not Found error.

- **Accessories**
  - **Expected Result**: Redirect to accessories category page.
  - **Actual Result**: Page Not Found error.

---

### 5. Banner Images (Sales / Models)
- **Steps**: Click rotating banner images.
- **Expected Result**: Redirect to relevant sales or product pages.
- **Actual Result**:  No action triggered, click not functional.
- **Bug Note**: Banner carousel images not linked.

---

## Summary of Findings
- Search bar → Broken.  
- Add to cart → Works.  
- Place order → Skips validation, direct success message.  
- Navigation links → Hover works, click fails.  
- Clothing & Accessories → Page Not Found errors.  
- Banner images → Not clickable.  

---

## Conclusion
The demo site has **major functional gaps** in search, checkout validation, navigation, and banner interactivity.  
Only **Add to Cart** works correctly.  
These issues should be logged for developer fixes and retested after resolution.
