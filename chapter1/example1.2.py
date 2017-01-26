

import pandas as pd

da = pd.read_table("./chapter1/text/d-ibm3dx7008.txt",index_col=['Date'])



da.head(1)

da.tail(1)

print da.tail(1)