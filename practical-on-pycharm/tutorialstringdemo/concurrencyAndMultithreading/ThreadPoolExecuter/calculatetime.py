import time
#record start time
start_time = time.time()
numbers=[1,38789,5,68975,9189,187]
squares=[num**2 for num in numbers]
end_time=time.time()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time} seconds")
