from fabric import Connection
import warnings
warnings.filterwarnings(action='ignore', module='.paramiko.')


def login_and_execute(host, usr, pwd, cmd):
    print("{} = {}".format(usr, pwd))

    c = Connection(host=host, user=usr, connect_kwargs={"password": pwd})
    result = c.run(cmd, hide=True)
    c.close()

    # only return the second line, which contains our command output
    return result.stdout.splitlines()[1]


solutions = {
    "century1": ("$PSVersionTable.BuildVersion.ToString()", "century1"),
    "century2": ("'invoke-webrequest' + (gci ~\Desktop | select -exp Name)", "10.0.14393.2791"),
    "century3": ("(gci ~\Desktop).Count", "invoke-webrequest443"),
    "century4": ("(gci ~\Desktop -Directory | gci | select -exp Name).ToLower()", "123"),
    "century5": ("$env:USERDOMAIN + (gci ~\Desktop | select -exp Name)", "61580"),
    "century6": ("(gci ~\Desktop -Directory).Count", "underthewire3347"),
    "century7": ("gc (gci $env:HOME -File -Recurse).FullName", "197"),
    "century8": ("(gci ~\Desktop -File | %{ gc $_.FullName} | Get-Unique).Count", "7points"),
    "century9": ("(gc (gci ~\Desktop -File -Recurse).FullName).Split(" ")[160].ToLower()", "696"),
    "century10": ("$d = (gwmi win32_service | where name -eq wuauserv | select -exp Description) -split ' ';($d[9] + $d[7] + (gci ~\Desktop | select -exp Name)).ToLower()", "pierid"),
    "century11": ("gci $env:HOME | gci -Hidden -File | select -exp Name", "windowsupdates110"),
    "century12": ("(((Get-ADComputer -Filter * -Properties Description | where DistinguishedName -eq (Get-ADDomainController).ComputerObjectDN).Description) + (gci ~\Desktop -File).Name).ToLower()", "secret_sauce"),
    "century13": ("(gc (gci ~\Desktop -File).FullName).Split(" ").Count", "i_authenticate_things"),
    "century14": ("((gc (gci ~\Desktop -File).FullName).Split(" ") | where {$_ -eq 'polo'}).Count", "755"),
    "century15": (None, "153")
}

only_test_last_sol = False

host = "century.underthewire.tech"
print("\n\nhost = {}\n".format(host))

if only_test_last_sol == True:
    last_sol = list(solutions.keys())[-2]
    next_sol = list(solutions.keys())[-1]
    pwd = login_and_execute(
        host, last_sol, solutions[last_sol][1], solutions[last_sol][0])
    login_and_execute(host, next_sol, pwd, "hostname")
else:
    next_pwd = solutions.get((list(solutions.keys()))[0])[1]

    for usr, val in solutions.items():
        cmd = val[0]
        pwd = next_pwd

        if cmd is not None:
            next_pwd = login_and_execute(host, usr, pwd, cmd)
        else:
            login_and_execute(host, usr, pwd, "hostname")
