import subprocess
import os
import shlex
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_with_subprocess_run(command, timeout=10):
    try:
        result = subprocess.run(
            shlex.split(command), check=True, text=True, capture_output=True, timeout=timeout
        )
        logging.info("Output: %s", result.stdout.strip())
    except subprocess.TimeoutExpired:
        logging.error("Command timed out after %d seconds", timeout)
    except subprocess.CalledProcessError as e:
        logging.error("Error: %s", e.stderr.strip())

def run_with_subprocess_popen(command, timeout=10):
    process = subprocess.Popen(
        shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    try:
        stdout, stderr = process.communicate(timeout=timeout)
        if process.returncode == 0:
            logging.info("Output: %s", stdout.strip())
        else:
            logging.error("Error: %s", stderr.strip())
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        logging.error("Command timed out and process was killed")

def run_with_check_output(command, timeout=10):
    try:
        output = subprocess.check_output(shlex.split(command), text=True, timeout=timeout)
        logging.info("Output: %s", output.strip())
    except subprocess.TimeoutExpired:
        logging.error("Command timed out after %d seconds", timeout)
    except subprocess.CalledProcessError as e:
        logging.error("Error: %s", e.stderr.strip())

command1 = "echo Hello, World!"
command2 = "ls -l" if os.name != "nt" else "dir"

logging.info("=== subprocess.run ===")
run_with_subprocess_run(command1)

logging.info("=== subprocess.Popen ===")
run_with_subprocess_popen(command1)

logging.info("=== subprocess.check_output ===")
run_with_check_output(command1)
