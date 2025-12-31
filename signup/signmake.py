signupkey = 21412
print(signupkey)

tdata = 200,400,500
ldata = [10,20,30]

for idx, (td, ld) in enumerate(zip(tdata, ldata)):
    ldata[idx] = td + ld

print(ldata)