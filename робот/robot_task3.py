import robot

r = robot.rmap()
r.lm('task3')


def task():
    for i in range(4):
        r.rt(2)
        if r.wu():
            r.dn()
            r.up()


r.start(task)
