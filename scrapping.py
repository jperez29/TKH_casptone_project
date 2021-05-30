import pandas as pd
from sodapy import Socrata


# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", '0NglgTmlSmVDevGUlpSizIcne')


# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("kpav-sd4t", limit=10)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(results_df.info())