init python:
    import renpy.store as store
    import renpy.exports as renpy

    class Task (store.object):
        def __init__(self, name, description, available = True, started = False, completed = False):
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

default task_eat_your_first_food = Task("Eat!!!", "Eat up man!")
default task_choose_best_girl = Task("Choose one!!!", "MAN up!")
default task_dont_be_greedy = Task("Greed is good", "Are you a greedy one?")
default task_survive_too_long = Task("Survived!", "Can you?")

default my_task = TaskList()

screen tasks_screen:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 130
        idle "menuUI/tasksmenu.png"
        action ShowMenu("task_list")

screen task_list:

    add "menuUI/bg grey.png"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 10
    
        vbox:
            spacing 40
            vbox:
                spacing 10
                text "{u}Task List{/u}" size 45
            vbox:
                spacing 5
                xalign 0.5
                yalign 0.5
                for task in my_task.task_list:
                    if not(task.completed):
                        text "[task.name]: [task.description] | [task.completed]" size 25
        
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle "menuUI/back_arrow.png"
        action Return()

