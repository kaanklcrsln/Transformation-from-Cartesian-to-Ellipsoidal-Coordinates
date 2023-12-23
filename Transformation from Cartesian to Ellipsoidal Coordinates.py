import math

def xyz2blh(x, y, z):
    # GRS80 ellipsoid parameters
    a, b = 6378137.0, 6356752.3141  
    e_squared = 1 - (b**2 / a**2)

    # set ellipsoidal coordinates
    # initial guess for latitude
    phi = math.atan2(z, math.sqrt(x**2 + y**2))  
    # initial guess for longitude
    lam = math.atan2(y, x)  
    # initial value for radius of curvature in prime vertical
    N = a / math.sqrt(1 - e_squared * math.sin(phi)**2)  

    precision, delta_h = 1e-6, float('inf')

    while delta_h > precision:
        # save previous latitude and calculate ellipsoidal height
        phi_prev, h = phi, math.sqrt(x**2 + y**2) / math.cos(phi) - N
        # update latitude and radius of curvature
        phi, N = math.atan2(z, math.sqrt(x**2 + y**2)), a / math.sqrt(1 - e_squared * math.sin(phi)**2)
        # check change in ellipsoidal height for convergence
        delta_h = abs(h - (math.sqrt(x**2 + y**2) / math.cos(phi) - N))

    # converting angle to degree
    phi_degrees, lam_degrees = math.degrees(phi), math.degrees(lam)

    return phi_degrees, lam_degrees, h

# example usage from assignment 3 pdf
x, y, z = 4210520.621, 1128205.600, 4643227.496
phi, lam, h = xyz2blh(x, y, z)

# printing the results
print(f"Latitude (phi): {phi:.4f} degrees")
print(f"Longitude (lambda): {lam:.4f} degrees")
print(f"Ellipsoidal height (h): {h:.4f} meters")