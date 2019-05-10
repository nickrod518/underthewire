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
    "oracle3": (None, "2f5c4")
}

test_solutions("oracle.underthewire.tech", solutions, False)
