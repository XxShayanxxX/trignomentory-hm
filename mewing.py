import math


angle_deg = float(input("Enter the angle in degrees: "))

angle_rad = math.radians(angle_deg)

sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)


print("Sine(", angle_deg, ") =", sin_value)
print("Cosine(", angle_deg, ") =", cos_value)
print("Tangent(", angle_deg, ") =", tan_value)

