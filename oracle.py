from ssh_helper import test_solutions

# username: (command, password)
solutions = {
    "oracle1": ("(Get-TimeZone).Id", "oracle1"),
    "oracle2": (
        """
            $hashes = (gci ~\Desktop | Get-FileHash -Algorithm MD5).Hash | %{ $_.Substring($_.Length - 5) }
            $ht = @{}
            $hashes | %{$ht["$_"] += 1}
            $ht.keys | where {$ht["$_"] -gt 1}
        """,
        "utc"
    ),
    "oracle3": (
        """
            (Get-WinEvent -Path (gci ~\Desktop).FullName |
                where Id -eq 1102).TimeCreated | Get-Date -Format 'MM/dd/yyyy'
        """,
        "2f5c4"
    ),
    "oracle4": (
        """
            $a = Get-Gpo -All | sort CreationTime | select -exp DisplayName -Last 1
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "05/09/2017"
    ),
    "oracle5": (
        """
            $a = (Get-Gpo -All | where Description -eq 'I_AM_GROOT').DisplayName
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "alpha83"
    ),
    "oracle6": (
        """
            $a = (Get-ADOrganizationalUnit -Filter { Name -ne 'Groups' } | where {
                -not ($_ | Get-GPInheritance).GpoLinks
            }).Name
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "charlie1337"
    ),
    "oracle7": (
        """
            $a = (Get-ADTrust -Filter *).Name
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "t-50_97"
    ),
    "oracle8": (
        """
            $content = gc (gci ~\Desktop).FullName
            $dlPath = ($content | where { $_ -like '*guardian.galaxy.com*' }).Split(' ')[6]
            (Split-Path $dlPath -Leaf).Split('.')[0]
        """,
        "multiverse111"
    ),
    "oracle9": (
        """
            $a = (Get-DnsServerResourceRecord -ZoneName underthewire.tech -RRType Mx).HostName
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "star-lord"
    ),
    "oracle10": (
        """
            $a = Get-DnsClientCache | where Entry -like "*.biz*"
            $b = (gci ~\Desktop).Name
            $a + $b
        """,
        "utw_exch9229"
    )
}

test_solutions("oracle.underthewire.tech", solutions, True)
