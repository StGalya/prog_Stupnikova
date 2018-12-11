import robot

r = robot.rmap()
r.lm('task4')


def task():
    while r.fr():
        r.rt()
    while r.fu():
        r.up()
    r.dn()
    r.lt()
    for i in range(3):
        for i in range(4):
            r.pt()
            r.dn()
            r.lt()
        r.pt()
        r.up(2)
        r.rt(4)


r.start(task)
