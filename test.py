# Part (a) - Finding F
def find_F(k, e):
    F = k * e
    return F

# Part (b) - Determining Stress
def determine_stress(F, A):
    stress = F / A
    return stress

# Part (c) - Determining Strain
def determine_strain(e, I):
    strain = e / I
    return strain

# Part (d) - Determining Young's Modulus (E)
def determine_young_modulus(stress, strain):
    E = stress / strain
    return E

# Main program
def main():
    k = float(input("Enter the material constant (k in N/m): "))
    e = float(input("Enter the extension (e in m): "))
    A = float(input("Enter the cross-sectional area (A in m^2): "))
    I = float(input("Enter the original length (I in m): "))
    
    F = find_F(k, e)
    stress = determine_stress(F, A)
    strain = determine_strain(e, I)
    E = determine_young_modulus(stress, strain)
    
    print("\n") 
    # This print is only here to put space before the answers is displayed in the terminal 

    print("Part (a) - Finding F:")
    print("F =", F, "N")
    
    print("\nPart (b) - Determining Stress:")
    print("Stress =", stress, "N/m^2 (Pa)")
    
    print("\nPart (c) - Determining Strain:")
    print("Strain =", strain)
    
    print("\nPart (d) - Determining Young's Modulus (E):")
    print("Young's Modulus (E) =", E, "N/m^2 (Pa)")

    print("\n") 
    # This print is only here to put space before the path is displayed in the terminal 

if __name__ == "__main__":
    main()
