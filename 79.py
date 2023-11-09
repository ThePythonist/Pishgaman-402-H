def send_warning(phonenumber, percent):
    print(f"Moshtarak gerami {phonenumber} shoma {percent}% az baste khod ra masraf karde eid.")


clients = ["09936458010", "09126338020", "09336458234"]

for i in clients:
    send_warning(i, "85")

