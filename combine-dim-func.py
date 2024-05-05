import subprocess
import multiprocessing
import os
import time
import concurrent.futures

skipped = {}

# Compile the C++ file
if not os.path.exists('./main'):
    subprocess.run(["g++", "main.cpp", "cec22_test_func.cpp", "-o", "main"], check=True)

def run_test(i):
    for j in [10, 20]:
        for k in range(1, j+1):
            # Set the dimension as a command line argument for the C++ program
            args = [str(i), str(j), str(k)]
            subprocess.run(['python', './run-tests.py'] + args)

if __name__ == '__main__':
    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(1, 13):
            if i in skipped:
                continue
            # Run the test in a separate thread
            futures.append(executor.submit(run_test, i))

        # Wait for all the tests to finish or timeout after 60 seconds
        for future in concurrent.futures.as_completed(futures, timeout=180):
            try:
                future.result()
            except concurrent.futures.TimeoutError:
                print("A test took too long and was cancelled.")


