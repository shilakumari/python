import random

pwd_gen="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$!"
seq=""
for _ in range(12):
    seq += random.choice(pwd_gen)

print(seq)