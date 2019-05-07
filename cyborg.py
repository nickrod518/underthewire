from ssh_helper import test_solutions

# username: (command, password)
solutions = {
    "cyborg1": ("(Get-ADUser -Filter {Surname -eq 'Rogers' -and GivenName -eq 'Chris'} -Properties State).State", "cyborg1"),
    "cyborg2": (None, "kansas"),
    "cyborg3": (None, None)
}

test_solutions("cyborg.underthewire.tech", solutions)
