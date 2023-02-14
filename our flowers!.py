my_flower1 = input()
my_flower2 = input()
my_flower3 = input()


your_flower1 = input()
your_flower2 = input()

your_list = [your_flower1, your_flower2]

their_flower = input()

my_list = [my_flower1, my_flower2, my_flower3]

our_list = my_list + your_list

print(our_list)

our_list.append(their_flower)

print(our_list)

# 5. TODO: Replace my_flower2 in our_list with their_flower

our_list[1] = their_flower

print(our_list)

our_list.remove(their_flower)
# 6. TODO: Remove the first occurrence of their_flower from
# our_list without using index()

print(our_list)
our_list.remove(our_list[1])
# 7. TODO: Remove the second element of our_list

print(our_list)
