def average_usage(values)
  """전력 사용량의 평균을 계산합니다."""
  return sum(values) / len(values)


sample = [12.4, 10.8, 13.1]
average = average_usage(sample)

print(f"평균 사용량:{average:.2f} kWh")
