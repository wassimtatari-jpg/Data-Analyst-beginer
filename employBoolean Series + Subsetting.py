import pandas as pd

employess=pd.DataFrame({
    "name":["wassim","mohamed","yassmine","farah"],
    "age":[38,42,19,22],
    "department":["python","driver","doctro","training"],
    "full_time":[True,False,True,False]

})

print(employess)

ft=employess['full_time']
print(ft)

sel=employess[ft]
print(sel)

assert sel["full_time"].all()