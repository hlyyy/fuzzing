def branch_coverage(trace):
    coverage = set()
    line_p = None
    for line in trace:
        if line_p != None:
            coverage.add((line_p, line))
        line_p = line
    return coverage

class BranchCoverage(Coverage):
    def coverage(self) -> Set[location]:
        return branch_coverage(self.trace())
        
    