import random
from rewards_list import rewards

loose_list = []
# Make a 50 set of loose word and append it on loose_list
for make_loose in range(50):
    loose = "loose"
    loose_list.append(loose)

# combining the reward list and loose list
for every_list in rewards:
    loose_list.append(every_list)

# printing the random choice inside the list
print(loose_list[random.randint(0, len(loose_list))])
