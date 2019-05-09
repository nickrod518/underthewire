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
        """
            $a = gc (gci ~\Desktop).FullName
            [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($a))
        """,
        "rowray_timer"
    ),
    "cyborg7": (
        """
            $key = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
            $propName = (Get-Item $key).Property
            $path = (Get-ItemProperty $key).$propName
            [io.path]::GetFileNameWithoutExtension($path)
        """,
        "cybergeddon"
    ),
    "cyborg8": ("(gci ~\Desktop | Get-Content -Stream Zone.Identifier)[-1][-1]", "skynet"),
    "cyborg9": (
        """
            $a = (Get-ADUser -Filter {OfficePhone -eq '876-5309'}).GivenName
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "4"
    ),
    "cyborg10": (None, "Onita")
}

test_solutions("cyborg.underthewire.tech", solutions, True)
