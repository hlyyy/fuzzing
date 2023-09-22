with BranchCoverage() as cov:
    cgi_decode("a+b")
print(cov.coverage())

with BranchCoverage() as cov_plus:
    cgi_decode("a+b")
with BranchCoverage() as cov_standard:
    cgi_decode("abc")
print(cov_plus.coverage() - cov_standard.coverage())

with BranchCoverage() as cov_max:
    cgi_decode('+')
    cgi_decode('%20')
    cgi_decode('abc')
    try:
        cgi_decode('%?a')
    except Exception:
        pass
print(cov_max.coverage() - cov_plus.coverage())