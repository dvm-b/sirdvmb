import requests
import sys
import time

api = "https://dumb-members-checker-api.vercel.app/api/"

ch = "@unsely"

RED = "\033[31m";GREEN = "\033[32m";CYAN = "\033[36m";RESET = "\033[0m"

def userid():
    while True:
        try:
            return int(input(f"{GREEN}Enter your Telegram User ID: {CYAN}"))
        except ValueError:
            print(f"{RED}Invalid input. Please enter a numeric Telegram User ID.{RESET}")

def mem(uid):
    try:
        response = requests.get(api, params={"user_id": uid}, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"{RED}[✖] Failed to reach API: {e}{RESET}")
        sys.exit(1)
    except ValueError:
        print(f"{RED}[✖] Invalid JSON response from API.{RESET}")
        sys.exit(1)

    if data.get("ok") and data.get("member"):
        print(f"{GREEN}[✔] Access Granted: User is a member ({data.get('status')}){RESET}")
    else:

        print(f"{RED}[✖] Access Denied: Please join required channel {ch} so you can use this tool.{RESET}")
        sys.exit(0)

print(f"{CYAN}Telegram Channel Access Verification via Vercel API{RESET}")
uid = userid()
print(f"{CYAN}Verifying access for User ID: {uid}...{RESET}")


print(f"{GREEN}Membership verified successfully. You may now use this tool.{RESET}")

print(f"{GREEN}Starting main tool...{RESET}")
