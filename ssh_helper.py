from fabric import Connection


def login_and_execute(host, usr, pwd, cmd="hostname"):
    print("{} = {}".format(usr, pwd))

    c = Connection(host=host, user=usr, connect_kwargs={"password": pwd})
    # hide stderr and stdout
    result = c.run(cmd, hide=True)
    c.close()

    # only return the second line, which contains our command output
    return result.stdout.splitlines()[1]


def test_solutions(host, solutions, last_only=False):
    print("\n\nhost = {}\n".format(host))

    if last_only == True:
        last_sol = list(solutions.keys())[-2]
        next_sol = list(solutions.keys())[-1]

        pwd = login_and_execute(
            host, last_sol, solutions[last_sol][1], solutions[last_sol][0])

        login_and_execute(host, next_sol, pwd)

    else:
        next_pwd = solutions.get((list(solutions.keys()))[0])[1]

        for usr, val in solutions.items():
            cmd = val[0]
            pwd = next_pwd

            if cmd is not None:
                next_pwd = login_and_execute(host, usr, pwd, cmd)
            else:
                login_and_execute(host, usr, pwd)
