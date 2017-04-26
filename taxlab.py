def calculate_tax(incomes_dict):
    if type(incomes_dict) != dict:
        raise ValueError('The provided input is not a dictionary.')
    tax_dict = {}
    if len(incomes_dict) == 0:
        return tax_dict
    rates = [.1, .15, .2, .25, .3]
    bounds = [1000, 10000, 20200, 30750, 50000]
    
    for key in incomes_dict.keys():
        if type(incomes_dict[key]) != int:
            raise ValueError
        tax = 0
        for ibound in range(len(bounds) - 1):
            if incomes_dict[key] > bounds[ibound]:
                if incomes_dict[key] > bounds[ibound+1]:
                    tax = tax + (bounds[ibound+1] - bounds[ibound]) * rates[ibound]
                else:
                    tax = tax + (incomes_dict[key] - bounds[ibound]) * rates[ibound]
                    break
        if incomes_dict[key] > bounds[len(bounds)-1]:
            tax = tax + (incomes_dict[key] - bounds[len(bounds)-1]) * rates[len(rates)-1]
        tax_dict[key] = tax
        
    return tax_dict

print(
       calculate_tax(
       {"James": 20500, "Mary": 500,
       "Evan": 70000, "Simeon": 12000,
       "Mutiso": 100000, "Marion": 3000000,
       "Mwende": 34000, "Bernard": 350000})             
      )

#print prime_gen(10)
