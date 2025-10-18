Import requests
import sys

def check_channel_membership(user_id):
    try:
        api_url = f"https://py-today-member-checker.vercel.app/?token=7391593372:AAFhLbgDhxgNmMZwlLIzB1VuxNnxykV83XQ&channel=@unsely&userid={user_id}"
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if data.get("is_member", False):
            print("\033[1;32m[✓] User is a member of @unsely. Access granted.\033[0m")
            return True
        else:
            print("\033[1;31m[✗] User is not a member of @unsely.")
            print("\033[1;31mPlease join @unsely and restart the tool.\033[0m")
            sys.exit(1)
    except requests.RequestException as e:
        print(f"\033[1;31m[✗] Error checking membership: {e}\033[0m")
        sys.exit(1)
    except ValueError:
        print(f"\033[1;31m[✗] Invalid response from API: {data.get('error', 'Unknown error')}\033[0m")
        sys.exit(1)

try:
    check_channel_membership(ID)
except NameError:
    print("\033[1;31m[✗] Required variable (ID) not provided.\033[0m")
    sys.exit(1)