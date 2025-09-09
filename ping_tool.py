import platform
import subprocess

def ping_host(host="127.0.0.1"):
    is_windows = platform.system().lower() == "windows"
    count_flag = "-n" if is_windows else "-c"
    timeout_flag = "-w" if is_windows else "-W"
    # 1 pachet, timeout 1s (pe Linux -W e secunde)
    cmd = ["ping", count_flag, "1", timeout_flag, "1", host]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(out.stdout)
        return "Ping OK"
    except subprocess.CalledProcessError as e:
        print(e.stdout or e.stderr)
        return "Ping FAIL"
