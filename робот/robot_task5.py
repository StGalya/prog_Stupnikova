import robot

r = robot.rmap()
r.lm('task5')


def part():
    r.pt()
    r.dn()
    r.rt()
    r.pt()
    r.up()
    r.rt()
    r.pt()
    if r.fr():
        r.rt(2)


def task():
    for i in range(3):
        for j in range(4):
            part()
        r.dn(3)
        r.lt(14)


r.start(task)
