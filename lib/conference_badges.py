def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = [f"Hello, my name is {name}." for name in names]
    return badges

def assign_rooms(names):
    new_list = [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(names)]
    return new_list

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
    return None
