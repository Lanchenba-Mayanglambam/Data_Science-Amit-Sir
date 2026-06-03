import pandas as p
d = {
    "name":["alice","shubham","rohit",],
    "age":[22,25,25],
    "score":[85,92,95]
}

df = p.DataFrame(d)
print(df)
print(df.head(3))
print(df.info())
df['score']
df[['name','age']]


#how to add in dframe
df['location'] = ["USA","Delhi","Noida"]
print(df)