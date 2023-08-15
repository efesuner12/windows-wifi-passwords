import subprocess

def display_wifi_pass():
    passwords = ""

    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            
            try:
                passwords += "{:<30}|  {:<}\n".format(i, results[0])
            except IndexError:
                passwords += "{:<30}|  {:<}\n".format(i, "")

        except subprocess.CalledProcessError:
            passwords += "{:<30}|  {:<}\n".format(i, "*****ENCODING ERROR*****")

    return passwords


if __name__ == "__main__":
    print(display_wifi_pass())
