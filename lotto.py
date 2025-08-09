
# Broj tiketa koji zeli da odigra

# 5 = 5 tiketa za lutriju sa nasumicnim brojevima (1-100)
# Bonus: Svaki broj mora biti jedinstven, 1 [2,5,6,55,22]

import random
import numpy as np

num_tickets = int(input("Unesite koliko tiketa zelite da kupite: "))
numbers_per_ticket = 7
tickets = []


# for _ in range(num_tickets):
#     ticket = []
#
#     while len(ticket) < numbers_per_ticket:
#         random_number = random.randint(1, 100)
#
#         if random_number in ticket:
#             continue
#
#         ticket.append(random_number)
#
#     tickets.append(ticket)
#
# print(tickets)

# Numpy lotto
for _ in range(num_tickets):
    ticket = np.random.choice(range(1, 100), size=numbers_per_ticket, replace=False)
    tickets.append(ticket)

print(tickets)