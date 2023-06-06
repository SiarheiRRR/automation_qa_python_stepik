import browsercookie

cookies = browsercookie.chrome(cookie_file='C:\\Users\\37061\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Network\\Cookies')
cookies = browsercookie.chrome()
print(cookies)
for cookie in cookies:
    print("Name:", cookie.name)
    print("Value:", cookie.value)
    print("Domain:", cookie.domain)
    print("Path:", cookie.path)
    print("Secure:", cookie.secure)
    print("Expires:", cookie.expires)
    print("--------------------------------------------------")
# import os
# file_path = 'C:\\Users\\37061\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Network\\'
# print(os.listdir(file_path))
# # with open(file_path) as file:
# #     lst = file.readlines()
# #     print(lst)