def name(f_name, l_name):
    new_fn = f_name.title()
    new_ln = l_name.title()
    print(f"Hi {new_fn} {new_ln}")

f_name = input("Fname: ")
l_name = input("Lname: ")
name(f_name, l_name)