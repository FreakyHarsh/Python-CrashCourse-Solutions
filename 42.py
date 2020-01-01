guest = ["Nayan", "Yusuf", "Pratik", "Arbaaz", "Fahim"]


def invitation():
    for i in guest:
        print(f"Hello {i}, You are invited to my party.")


invitation()

print(f"\n{guest[2]} won't be able to come to the party")
guest.remove("Pratik")
guest.insert(2, "Harsh")

invitation()

print("\nI found a bigger table so will invite three more people")
guest.insert(0, "Teena")
guest.insert(5, "Palak")
guest.append("Hui")

invitation()

print("\nLo siento! I can only invite two people now")
for i in range(2, len(guest)):
    print(f"{guest.pop()} I am sorry but you are not invited")

invitation()
