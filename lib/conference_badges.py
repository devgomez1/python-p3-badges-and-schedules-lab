def badge_maker(name):
    greeting = "Hello, my name is " + name + "."
    return greeting

def batch_badge_creator(names):
    list = []
    for name in names:
        greeting = badge_maker(name)
        list.append(greeting)
    return list

def assign_rooms(names):
    list = []
    for name in names:
        room = names.index(name) + 1
        greeting = "Hello, " + name + "! You'll be assigned to room " + str(room) + "!"
        list.append(greeting)
    return list


def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)