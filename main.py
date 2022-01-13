
def count_batteries_by_usage(cycles):
  low,medium,high=0,0,0
  #loop through the list to categorize batteries
  for i in cycles:
    if i<400:
      low += 1
    elif i<920:
      medium += 1
    else:
      high += 1
  return {
    "lowCount": low,
    "mediumCount": medium,
    "highCount": high
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
