# Number data types

# Subroutine to calculate VAT
def VAT(Total):
    return Total * 0.05


# Main program
Total = 100.12
ValueAddedTax = VAT(Total)
ToPay = Total + ValueAddedTax
print("Total £{:.2f} VAT £{:.2f} To pay £{:.2f}".format(Total, ValueAddedTax, ToPay))
