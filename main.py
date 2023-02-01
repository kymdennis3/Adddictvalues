toys = {"robot": "$40.0", "car": "$25", "ironman": "$12"}

sum = list(toys.values())

total = (eval(sum[0][1:]) + eval(sum[1][1:]) + eval(sum[2][1:]))

print(total)