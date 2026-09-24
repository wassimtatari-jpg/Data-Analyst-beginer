import pandas as pd

orders=pd.DataFrame({
    "customers":["Kawtar","Tasnim","Adnan","Akram","ali"],
    "product":["Shampoo","water","tv","pantalon","coffe"],
    "price":[80,10,10000,250,7],
    "paid":[True,True,False,False,True]
})
print(orders)
p=orders["paid"]
print(p)
sel=orders[p]
print(sel)

assert sel['paid'].all()