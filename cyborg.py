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
    "cyborg10": (
        """
            $a = (Get-AppLockerPolicy -Effective).RuleCollections.Description
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "onita99"
    ),
    "cyborg11": (
        """
            $log = gci C:\inetpub\logs\logfiles -File -Recurse
            $content = gc $log.FullName
            $pass = $content | %{ ($_.Split(' '))[12] } | where { $_ -notlike "*mozilla*" -and $_ -notlike "*opera*" }
            $pass[-1].Split(':')[1]
        """,
        "terminated!99"
    ),
    "cyborg12": (
        """
            $path = (Get-WmiObject win32_service | where Name -eq 'i_heart_robots').PathName
            $bytes = [System.Text.Encoding]::UTF8.GetBytes($path)
            $a = [System.Convert]::ToBase64String($bytes).Substring(0, 4)
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "spaceballs"
    ),
    "cyborg13": (
        """
            $a = (Get-DnsServerZoneAging -ZoneName underthewire.tech).RefreshInterval.Days.ToString()
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "yzpc_heart"
    ),
    "cyborg14": (
        """
            $a = (Get-WmiObject -Class "Win32_DCOMApplication" -Namespace "root\CIMV2" | where AppID -eq '{59B8AFA0-229E-46D9-B980-DDA2C817EC7E}').Caption
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "22_days"
    ),
    "cyborg15": (None, "propshts_obj")
}

test_solutions("cyborg.underthewire.tech", solutions, True)
