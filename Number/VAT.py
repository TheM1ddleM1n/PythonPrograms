def VAT(Total):
    return Total * 0.05

Total = 100.12
ValueAddedTax = VAT(Total)
ToPay = Total + ValueAddedTax
print(f"Total £{Total:.2f} VAT £{ValueAddedTax:.2f} To pay £{ToPay:.2f}")
