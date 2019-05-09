from ssh_helper import test_solutions

# username: (command, password)
solutions = {
    "cyborg1": ("(Get-ADUser -Filter {Surname -eq 'Rogers' -and GivenName -eq 'Chris'} -Properties State).State", "cyborg1"),
    "cyborg2": (
        """
            $a = (Get-DnsServerResourceRecord -RRType A -ZoneName underthewire.tech -Name CYBORG718W100N).RecordData.IPv4Address.IPAddressToString
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "kansas"),
    "cyborg3": ("(Get-ADGroupMember Cyborg -Recursive).Count.ToString() + (gci ~\Desktop).Name", "172.31.45.167_ipv4"),
    "cyborg4": ("(Get-Command | where Version -eq '8.9.8.9').Source + (gci ~\Desktop).Name", "88_objects"),
    "cyborg5": (
        """
            $a = (Get-ADUser -Filter {LogonHours -like '*' -and Enabled -ne $true} -Properties LogonHours).Surname
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "bacon_eggs"
    ),
    "cyborg6": (
        None, "rowray_timer"
    )
}

test_solutions("cyborg.underthewire.tech", solutions, False)
