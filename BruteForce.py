import rarfile
import sys

rarfile.UNRAR_TOOL = "UnRAR.exe"

rar_filename = input("Enter RAR file name: ")
wordlist_filename = input("Enter password list file: ")

rar_file = rarfile.RarFile(rar_filename)
wordlist_file = open(wordlist_filename, errors='ignore')

print("**")

is_password_found = False
counter = 0
current_password = ""

for line in wordlist_file:
    counter = counter + 1
    current_password = line.strip()
    print("{} PASSWORDS TRIED.".format(counter))

    try:
        rar_file.setpassword(current_password)
        rar_file.testrar()
        print("**")
        print("PASSWORD FOUND AFTER {} ATTEMPTS.".format(counter))
        is_password_found = True
        break
    except:
        continue

if is_password_found:
    print("PASSWORD -> {}".format(current_password))
    sys.exit()
else:
    print("**")
    print("Damn, couldn't find it.")