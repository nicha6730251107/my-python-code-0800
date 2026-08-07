# สามเหลื่ยม
def calculate_triangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * base * height
    print(f"Rectangle with height {height} and base {base}")
    print(f"Area = {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)


#วงกลม
def calculate_circle_area(radius):
    """Calculates and displays circle area"""
    area = 3.14 * radius * radius
    print(f"Circle with radius {radius}")
    print(f"Area = 3.14 × {radius} × {radius} = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5, 7)
calculate_circle_area(10, 7)

# เขียนฟังก์ชัน ชื่อ calculate_sphere(radius):
# คำนวนหา ปริมาตร ของทรงกลม volumn = 4.0 / 3 * radius ** 3
# จากนั้นแสดงผลลัพธ์ที่เหมาะสมออกทางจอ