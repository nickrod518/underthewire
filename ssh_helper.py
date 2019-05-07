from fabric import Connection
from invoke import UnexpectedExit
import paramiko


def login_and_execute(host, usr, pwd, cmd="hostname"):
    lpwd = str(pwd).lower()
    print("Trying username ", end='')
    print(bcolors.BOLD + usr + bcolors.ENDC, end='')
    print(" and password ", end='')
    print(bcolors.BOLD + lpwd + bcolors.ENDC, end='')
    print("...", end='')

    try:
        c = Connection(host=host, user=usr, connect_kwargs={"password": lpwd})
        # hide stderr and stdout
        result = c.run(cmd, hide=True)
        print(bcolors.OKGREEN + "success." + bcolors.ENDC)
        c.close()

    except paramiko.ssh_exception.AuthenticationException as e:
        print(bcolors.FAIL + str(e).lower() + bcolors.ENDC)
        return None

    except UnexpectedExit as e:
        print(bcolors.FAIL + str(e).lower() + bcolors.ENDC)
        return None

    lines = result.stdout.splitlines()

    if len(lines) > 1:
        # the second line contains our cmd output
        out = lines[1]

        if out is not None and out != "":
            return out
        else:
            print(bcolors.WARNING + "Command produced no output:" + bcolors.ENDC)
            print(bcolors.HEADER + cmd + bcolors.ENDC)
            return None


def test_solutions(host, solutions, last_only=False):
    print("\nUsing hostname ", end='')
    print(bcolors.BOLD + host + bcolors.ENDC)

    if last_only == True:
        # only test the final solution
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

            if pwd is not None:
                if cmd is not None:
                    next_pwd = login_and_execute(host, usr, pwd, cmd)
                else:
                    next_pwd = None
                    login_and_execute(host, usr, pwd)
            else:
                print("exiting...")
                return


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
