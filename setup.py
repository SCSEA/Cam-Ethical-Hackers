import os

print("""[0] pip\n[1] pip3\nWhich one you wanna to use ?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install requests")
    os.system("pip install colorama")

elif c == "1":
    os.system("pip install requests")
    os.system("pip install colorama")

if os.name == "nt":
    pass
else:
    os.system("pip install requests")
    os.system("pip install colorama")

print("Done.")
