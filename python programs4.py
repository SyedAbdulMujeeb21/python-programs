def simple_interest(P, R, T):
    return (P * R * T) / 100


P = 10000   
R = 5       
T = 3       

SI = simple_interest(P, R, T)
print(f"Simple Interest = {SI}")