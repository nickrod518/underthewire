from ssh_helper import test_solutions

# username: (command, password)
solutions = {
    "century1": ("$PSVersionTable.BuildVersion.ToString()", "century1"),
    "century2": ("'invoke-webrequest' + (gci ~\Desktop).Name", "10.0.14393.2791"),
    "century3": ("(gci ~\Desktop).Count", "invoke-webrequest443"),
    "century4": ("(gci ~\Desktop -Directory | gci).Name", "123"),
    "century5": ("$env:USERDOMAIN + (gci ~\Desktop).Name", "61580"),
    "century6": ("(gci ~\Desktop -Directory).Count", "underthewire3347"),
    "century7": ("gc (gci $env:HOME -File -Recurse).FullName", "197"),
    "century8": ("(gci ~\Desktop -File | %{ gc $_.FullName} | Get-Unique).Count", "7points"),
    "century9": ("(gc (gci ~\Desktop -File -Recurse).FullName).Split(" ")[160]", "696"),
    "century10": (
        """
            $a = (gwmi win32_service | where name -eq wuauserv).Description.Split(' ')
            $b = (gci ~\Desktop).Name
            $a[9] + $a[7] + $b
        """,
        "pierid"
    ),
    "century11": ("(gci $env:HOME | gci -Hidden -File).Name", "windowsupdates110"),
    "century12": (
        """
            $a = ((Get-ADComputer -Filter * -Properties Description |
                where DistinguishedName -eq (Get-ADDomainController).ComputerObjectDN).Description)
            $b = (gci ~\Desktop -File).Name
            $a + $b
        """,
        "secret_sauce"
    ),
    "century13": ("(gc (gci ~\Desktop -File).FullName).Split(" ").Count", "i_authenticate_things"),
    "century14": ("((gc (gci ~\Desktop -File).FullName).Split(" ") | where {$_ -eq 'polo'}).Count", "755"),
    "century15": (None, "153")
}

test_solutions("century.underthewire.tech", solutions)
