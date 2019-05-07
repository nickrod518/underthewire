from ssh_helper import test_solutions

# username: (command, password)
solutions = {
    "cyborg1": ("(Get-ADUser -Filter *)", "cyborg1"),
    "cyborg2": ("hostname", None)
}

test_solutions("cyborg.underthewire.tech", solutions)
