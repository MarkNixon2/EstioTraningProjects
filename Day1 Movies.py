def search_guest(myname):
    guest_list = ["Mark", "James", "Robert", "Harry"]
    if myname in guest_list:
        print("Hi " + myname + ", You're on the guest list")
    else:
        print("Unfortunately " + myname + ", You're not on the guest list")

you = input("What is your name?: ")
search_guest(you)