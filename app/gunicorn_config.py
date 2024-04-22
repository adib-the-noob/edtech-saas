import multiprocessing

# Calculate the number of workers (adjust the multiplier based on your application and server)
workers = multiprocessing.cpu_count() * 2 + 1

bind = "0.0.0.0:8000"
timeout = 120