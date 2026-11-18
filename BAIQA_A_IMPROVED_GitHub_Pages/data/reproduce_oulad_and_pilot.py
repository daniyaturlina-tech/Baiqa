"""Secondary reconstruction of published OULAD Table 5 and illustrative pilot cost arithmetic.
No individual student records or Baiqa predictions are used. Python 3, standard library only.
"""
import csv
from pathlib import Path
folder=Path(__file__).parent
with (folder/'oulad_2026_published_top5_precision.csv').open() as f:
 rows=list(csv.DictReader(f))
for split in ('Within-cohort test','Across-year test'):
 r={x['feature_set']:float(x['top5_precision_pct']) for x in rows if x['validation']==split}
 print(split, r)
 print('All-features minus behavior-only (percentage points):',round(r['All features']-r['Behavior only'],2))
assert 29/32*100-24/33*100>17.8  # separately published Hasan & Khan RCT
n_alerts=10; weeks=24; hourly=3040
hours=n_alerts*weeks*(10+.3*15)/60
for name,cost in [('Existing monitoring',96*hourly),('Rules',250000+hours*hourly),('Baiqa',1450000+hours*hourly+1181)]:print(name,round(cost))
