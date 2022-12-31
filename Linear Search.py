
linear_search = ["-","Ahmed","0","Emaad","-"]
search_name = input("Enter Data: ")

for x in range(len(linear_search)):
    if linear_search[x] == search_name:
        print(f"Name found: {linear_search[x] }")
        quit()
print("Not present in Array")
