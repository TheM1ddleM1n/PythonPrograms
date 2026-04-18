import subprocess
import os
import shlex


# 1. Using subprocess.run (Recommended for most use cases)
def run_with_subprocess_run(command):
    try:
        result = subprocess.run(
            command, shell=True, check=True, text=True, capture_output=True
        )
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)


# 2. Using subprocess.Popen (More control over input/output streams)
def run_with_subprocess_popen(command):
    process = subprocess.Popen(
        shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("Output:", stdout)
    else:
        print("Error:", stderr)


# 3. Using os.system (Simple but not recommended for new code due to security risks)
def run_with_os_system(command):
    exit_code = os.system(command)
    print(f"Command exited with code {exit_code}")


# 4. Using subprocess.check_output (Useful for capturing command output)
def run_with_check_output(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        print("Output:", output)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)


# Example commands for demonstration
command1 = "echo Hello, World!"
command2 = "ls -l" if os.name != "nt" else "dir"

# Execute the commands using various methods
print("=== subprocess.run ===")
run_with_subprocess_run(command1)

print("\n=== subprocess.Popen ===")
run_with_subprocess_popen(command1)

print("\n=== os.system ===")
run_with_os_system(command1)

print("\n=== subprocess.check_output ===")
run_with_check_output(command1)
