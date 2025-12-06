# Task-04: Cross-Browser Testing with BrowserStack

## Objective
Perform cross-browser automation testing using Selenium WebDriver integrated with BrowserStack.  
The chosen test case was the login functionality of the demo site **Swag Labs**.

## Steps Implemented
1. **Setup Selenium in VS Code**
   - Installed Selenium 4.
   - Configured BrowserStack credentials.

2. **Created Scripts for Multiple Browsers**
   - Chrome → `webdriver.ChromeOptions()`
   - Firefox → `webdriver.FirefoxOptions()`
   - Safari → `webdriver.SafariOptions()`
   - Edge → `webdriver.EdgeOptions()`

3. **Test Scenario**
   - Navigate to `https://www.saucedemo.com/`
   - Enter username: `standard_user`
   - Enter password: `secret_sauce`
   - Click login button
   - Assert that the **Products** page is displayed
## Results
| Browser  | Result | Notes |
|----------|--------|-------|
| Chrome   |  Pass | Login successful |
| Firefox  |  Pass | Login successful |
| Safari   |  Pass | Login successful |
| Edge     |  Pass | Login successful |

## Observations
- Minor UI differences across browsers (fonts, button alignment).
- All functional tests passed consistently.
- Warning about embedding credentials in URL was noted but did not affect execution.

## Deliverables
- Four Selenium scripts (one per browser).
- This documentation file summarizing the task.

---

**Conclusion:** Task‑04 successfully demonstrated cross‑browser testing using BrowserStack.  
The login functionality of Swag Labs was validated across Chrome, Firefox, Safari, and Edge.

4. **Execution**
   - Scripts executed locally in VS Code.
   - Browser sessions ran remotely on BrowserStack cloud.
   - Each browser test completed successfully.
