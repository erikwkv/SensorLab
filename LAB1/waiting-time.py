import math

start_frequency = 0.1
end_frequency = 20_000_000
num_samples = 501
total_time = 0
periods = 16
samples_to_average = 10
current_sample = 71
elapsed_time = 0
for i in range(num_samples):
    frequency = math.exp(math.log(start_frequency) + (math.log(end_frequency) - math.log(start_frequency)) * i / (num_samples - 1))
    time = periods * samples_to_average * (1 / frequency)
    total_time += time
    if i == current_sample:
        elapsed_time = total_time

print("\n")
hours, remainder = divmod(total_time, 3600)
days, hours = divmod(hours, 24)
minutes, seconds = divmod(remainder, 60)
print("Total waiting time: {:2} days, {:2} hours, {:2} minutes, {:4.1f} seconds".format(days, hours, minutes, seconds))

elapsed_hours, elapsed_remainder = divmod(elapsed_time, 3600)
elapsed_days, elapsed_hours = divmod(elapsed_hours, 24)
elapsed_minutes, elapsed_seconds = divmod(elapsed_remainder, 60)
print("Elapsed time:        {:2} days, {:2} hours, {:2} minutes, {:4.1f} seconds".format(elapsed_days, elapsed_hours, elapsed_minutes, elapsed_seconds))

remaining_time = total_time - elapsed_time
remaining_hours, remaining_remainder = divmod(remaining_time, 3600)
remaining_days, remaining_hours = divmod(remaining_hours, 24)
remaining_minutes, remaining_seconds = divmod(remaining_remainder, 60)
print("Time remaining:      {:2} days, {:2} hours, {:2} minutes, {:4.1f} seconds".format(remaining_days, remaining_hours, remaining_minutes, remaining_seconds))

print("\n")