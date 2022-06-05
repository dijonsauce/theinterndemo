#intern quest & achievement system
#or QuestList

init python:
    import renpy.store as store
    import renpy.exports as renpy

    class Task (store.object):
        def __init__(self, name, description, available = False, started = False, completed = False):
            self.name = name
            self.description = description
            self.available = available
            self.started = started
            self.completed = completed

    class TaskList (store.object):
        def __init__(self):
            self.task_list = []

        def addTask(self, task):
            self.task_list.append(task)

        def removeTask(self, task):
            self.task_list.remove(task)

######
#default task_first_day = Task("The Interview", "Help a friend in need.")
#default task_conference = Task("VIP Lounge", "Tidy up the Conference room.")
#default task_research = Task("The Matchmaker", "Do some Research & Developement.")

#conference cleaner
default task_cleanup_samplebox = Task("", "",True)
default task_cleanup_jacket = Task("", "",True)
default task_cleanup_shoes = Task("", "",True)
default task_cleanup_books = Task("", "",True)
default task_cleanup_writing = Task("", "",True)

default my_task = TaskList()
