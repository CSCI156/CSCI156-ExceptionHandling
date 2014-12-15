1. Write a procedure that
   - i. Asks the user to input their social security number. The phrasing for the question should be passed in as a string.
   - ii. Checks to make sure the input has the correct format AAA-GG-SSSS using a try except. AAA is the area number, GG is the group number, and SSSS is the serial number.
   - iii. returns the AAA, GG, and SSSS as a tuple if the user put in a valid SS number, otherwise it returns None.
2. Write a procedure SS that calls the procedure above until the user puts in a valid SS#.
3. The string that asks the user to input their SS# should be hardcoded as a variable at the beginning of the program.
This string should be passed to the above two procedures.


####NOTES:
      A. Numbers with all zeros in any digit group (000-##-####, ###-00-####, ###-##-0000) are not allowed.
      B. Numbers with 666 or 900-999 in the first digit group are invalid.
      C. The number 078-05-1120 is invalid as it was used in an advertising campaign.
