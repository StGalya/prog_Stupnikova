import robot

r = robot.rmap()
r.lm('task2')


def task():
    for i in range(5):
        r.up()
        r.pt()
        r.up()
        r.rt()
        r.pt()
        r.dn(2)
        r.pt()
        r.rt()
        r.up()
        r.pt()
        r.dn()
        if r.fr():
            r.rt()


r.start(task)
