def compare(weight, height):
  """
  คำนวณค่า BMI

  Args:
    weight: น้ำหนัก (กิโลกรัม)
    height: ส่วนสูง (เมตร)

  Returns:
    ค่า BMI
  """

  weight = float(weight)
  height = float(height)
  bmi = weight / pow(height, 2)
  return round(bmi, 2)


print(compare(50, 1.75))