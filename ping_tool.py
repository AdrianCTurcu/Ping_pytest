import subprocess

def ping(host="8.8.8.8"):
    result = subprocess.run(
        ["ping", "-n", "4", host],
        capture_output=True,
        text=True
    )
    print(result.stdout)   # afișează ping-ul în consolă
    return result.returncode == 0

if __name__ == "__main__":
    if ping():
        print("Ping OK")
    else:
        print("Ping FAIL")
