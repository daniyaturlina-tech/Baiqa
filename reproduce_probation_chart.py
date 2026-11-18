# From Sergazina (2024) NU thesis, Table 2 (aggregate sample counts).
# These academic probation proportions do NOT measure mental health or missed faculty outreach.
import csv
from pathlib import Path
with (Path(__file__).parent/'sergazina_2024_probation_table2.csv').open() as f:
 for row in csv.DictReader(f):
  print(f"{row['group']}: {int(row['ever_on_probation'])}/{int(row['total_students'])} = {100*int(row['ever_on_probation'])/int(row['total_students']):.2f}%")
