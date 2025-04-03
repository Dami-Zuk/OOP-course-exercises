# Author: Damian Zukowski

# Task 1 - class Task
class Task:
    _id_count = 0     # class variable

    def __init__(self, desc: str, worker: str, workload: int):
        Task._id_count += 1
        self._id = Task._id_count
        self._desc = desc
        self._worker = worker
        self._workload = workload
        self._finished = False      # by default

    # Mark the task as finished
    def mark_finished(self):
        self._finished = True

    # Returns True or False about the task completion
    def is_finished(self):
        return self._finished

    def __str__(self):
        if self._finished:
            status = "The task is finished"
        else:
            status = "The task is not finished"

        return f"Task ID: {self._id}, Description: {self._desc}, Workload: {self._workload}h, Assigned to {self._worker}, Status: {status}"
    

# Tests
""" t1 = Task("do your OOP homework", "Damian", 55)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished()) """


# Part 2 - class OrderBook
class OrderBook:
    def __init__(self):
        self._orders = []

    # Adds a new task
    def add_order(self, desc: str, worker: str, workload: int):
        task = Task(desc, worker, workload)
        self._orders.append(task)

    # Returns all tasks
    def all_orders(self):
        return self._orders

    # Returns a list of programmers with tasks
    def programmers(self):
        return list(set(task._worker for task in self._orders))
    
    # Part 3 - Marks a task as finished by its ID
    def mark_finished(self, id: int):
        for task in self._orders:
            if task._id == id:
                task.mark_finished()
                return
            
            raise ValueError("No task exists with given ID")

    # Part 3 - Returns a list of all finished tasks
    def finished_orders(self):
        return [task for task in self._orders if task.is_finished()] # list comprehension, each task from self._orders if is_finished = True

    # Part 3 - Returns a list of all unfinished tasks
    def unfinished_orders(self):
        return [task for task in self._orders if not task.is_finished()]
    
    # Part 4 - Returns tuples with finished and unfinished tasks + their time estimations
    def status_of_programmer(self, worker: str):
        finished_tasks = [task for task in self._orders if task._worker == worker and task.is_finished()]
        unfinished_tasks = [task for task in self._orders if task._worker == worker and not task.is_finished()]
        
        finished_count = len(finished_tasks)
        finished_hours = sum(task._workload for task in finished_tasks)

        unfinished_count = len(unfinished_tasks)
        unfinished_hours = sum(task._workload for task in unfinished_tasks)

        return f"(tasks, hours) Finished: {(finished_count, finished_hours)}, Unfinished: {(unfinished_count, unfinished_hours)}"


# Tests
order_book = OrderBook()
order_book.add_order("More homeworks..", "Damian", 6)
order_book.add_order("Even more homeworks...", "Damian", 10)
print("Programmers with assigned tasks: ", order_book.programmers())
for task in order_book.all_orders():
    print(task)


order_book.mark_finished(1)
print("\nFinished Orders:")
for task in order_book.finished_orders():
    print(task)  

print("\nUnfinished Orders:")
for task in order_book.unfinished_orders():
    print(task)

print(order_book.status_of_programmer("Damian"))





