import math

start_frequency = 0.1
end_frequency = 20_000_000
num_samples = 501
total_time = 0
length = 16
samples = 10

for i in range(num_samples):
    frequency = math.exp(math.log(start_frequency) + (math.log(end_frequency) - math.log(start_frequency)) * i / (num_samples - 1))
    time = length*samples * (1 / frequency)
    total_time += time

hours, remainder = divmod(total_time, 3600)
days, hours = divmod(hours, 24)
minutes, seconds = divmod(remainder, 60)
print("\n")
print("Total waiting time: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, round(seconds, 1)))

