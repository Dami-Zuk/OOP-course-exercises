# Author: Damian Zukowski

queue = ["Matti", "Riikka", "Antti", "Jenni", "Anu", "Ville", "Jarno"]

# Check if the queue is empty
if queue:
    # First person in the queue leaves after paying
    first_served = queue.pop(0)
    print("First customer, leaving: ", first_served)
    print("1. Remaining people: ", queue)


    # Ville recruits Anni to queue on his behalf
    for i, person in enumerate(queue):
        if person == "Ville":
            queue[i] = "Anni"
            is_ville = True

    if not is_ville:
        print("Ville is not in the queue!")

    print("2. Remaining people: ", queue)


    # Jarno leaves the queue
    jarno_leaves = queue.pop()
    print("3. Remaining people: ", queue)


    # Marjo joins the end of the queue
    Marjo_joins = queue.append("Marjo")
    print("4. Remaining people: ", queue)


    # Antti lets 2 people behind him go ahead of him
    antti_gentleman = queue.pop((queue.index("Antti")))

    for i in range(2):
        remove_last_two = queue.pop()

    fixing_queue = queue.extend(["Antti", "Anni", "Marjo"])
    print("5. Remaining people: ", queue)

else:
    print("Empty queue!")

# Jenni is still in the queue, she´s in the 2nd place. The third last person is Antti.
