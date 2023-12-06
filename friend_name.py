def get_friend_name():
    first_letter = input("Enter the first letter of your friend's name: ").upper()
    friends = {'S': "Sakthi", 'I':"Issac",'H': "Hari"}
    if first_letter in friends:
        full_name = friends[first_letter]
        print(f"Your friend's full name is {full_name}.")
    else:
        print("Try another letter")
get_friend_name()
