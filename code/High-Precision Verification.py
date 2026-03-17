import mpmath

# Set precision to 50 decimal places to verify exactness
mpmath.mp.dps = 50

print("--- Sultanian Identity Verification ---")

# 1. Identity for pi/2: pi/2 = -i * ln(i)
pi_lhs = mpmath.pi / 2
pi_rhs = -1j * mpmath.ln(1j)

print(f"\nIdentity 1 (pi/2):")
print(f"LHS (Standard pi/2): {pi_lhs}")
print(f"RHS (-i * ln(i)):    {pi_rhs}")
print(f"Absolute Difference: {abs(pi_lhs - pi_rhs)}")

# 2. Identity for sqrt(2): 2^( (i*pi/ln(2)) + 1/2 ) = -sqrt(2)
sqrt2_lhs = 2**( (1j * mpmath.pi / mpmath.ln(2)) + 0.5 )
sqrt2_rhs = -mpmath.sqrt(2)

print(f"\nIdentity 2 (sqrt(2)):")
print(f"LHS (Complex Power): {sqrt2_lhs}")
print(f"RHS (-sqrt(2)):      {sqrt2_rhs}")
print(f"Absolute Difference: {abs(sqrt2_lhs - sqrt2_rhs)}")


# 3. Identity for sqrt(2): (i+1)/sqrt(i) = sqrt(2)
sqrt2_lhs_2 = (1j+1) / mpmath.sqrt(1j) 
sqrt2_rhs_2 = mpmath.sqrt(2)  

print(f"\nIdentity 3 (sqrt(2)):")
print(f"LHS ((i+1)/sqrt(i)): {sqrt2_lhs_2}")
print(f"RHS (sqrt(2)):       {sqrt2_rhs_2}")
print(f"Absolute Difference: {abs(sqrt2_lhs_2 - sqrt2_rhs_2 )}")

# 4. Identity for pi: -4i * ln((i/sqrt(2)) + (1/sqrt(2))) = pi
sqrt2_lhs_3 = -4 *(1j) *mpmath.ln(((1j)/sqrt2_rhs_2)+(1/sqrt2_rhs_2)) 
sqrt2_rhs_3 =  mpmath.pi  

print(f"\nIdentity 4 (pi):")
print(f"LHS (-4i * ln((i/sqrt(2)) + (1/sqrt(2)))): {sqrt2_lhs_3}")
print(f"RHS (pi):       {sqrt2_rhs_3}")
print(f"Absolute Difference: {abs(sqrt2_lhs_3 - sqrt2_rhs_3 )}")