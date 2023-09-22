from typing import Tuple, List, Any
import random

Outcome = str

class Runner:
    """Base class for testing inputs."""

    # Test outcomes
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"

    def __init__(self) -> None:
        """Initialize"""
        pass

    def run(self, inp: str) -> Any:
        """Run the runner with the given input"""
        return (inp, Runner.UNRESOLVED)
    
class PrintRunner(Runner):
    """Simple runner, printing the input."""

    def run(self, inp) -> Any:
        """Print the given input"""
        print(inp)
        return (inp, Runner.UNRESOLVED)

class TroffRunner(Runner):
    def __init__(self):
        self.check_1 = 0
        self.check_2 = 0
        self.check_3 = 0
        
    def run(self, inp):
        # try...except...will not end the program
        try:
            check_1(inp)
        except AssertionError:
            self.check_1 += 1
            
        try:
            check_2(inp)
        except AssertionError:
            self.check_2 += 1
            
        try:
            check_3(inp)
        except AssertionError:
            self.check_3 += 1
        return inp
    
class Fuzzer:
    """Base class for fuzzers."""

    def __init__(self) -> None:
        """Constructor"""
        pass

    def fuzz(self) -> str:
        """Return fuzz input"""
        return ""

    def run(self, runner: Runner = Runner()) \
            -> Tuple[subprocess.CompletedProcess, Outcome]:
        """Run `runner` with fuzz input"""
        return runner.run(self.fuzz())

    def runs(self, runner: Runner = PrintRunner(), trials: int = 10) \
            -> List[Tuple[subprocess.CompletedProcess, Outcome]]:
        """Run `runner` with fuzz input, `trials` times"""
        return [self.run(runner) for i in range(trials)]
    
class RandomFuzzer(Fuzzer):
    """Produce random inputs."""

    def __init__(self, min_length: int = 10, max_length: int = 100,
                 char_start: int = 32, char_range: int = 32) -> None:
        """Produce strings of `min_length` to `max_length` characters
           in the range [`char_start`, `char_start` + `char_range`)"""
        self.min_length = min_length
        self.max_length = max_length
        self.char_start = char_start
        self.char_range = char_range

    def fuzz(self) -> str:
        string_length = random.randrange(self.min_length, self.max_length + 1)
        out = ""
        for i in range(0, string_length):
            out += chr(random.randrange(self.char_start,
                                        self.char_start + self.char_range))
        return out
        
troffrun = TroffRunner()
random_fuzzer = RandomFuzzer(min_length = 10, max_length = 20, char_start = 0, char_range = 256)
for i in range(100000):
    random_fuzzer.run(troffrun)
print("check_1 failed " + str(troffrun.check_1))
print("check_2 failed " + str(troffrun.check_2))
print("check_3 failed " + str(troffrun.check_3))


#result:
#check_1 failed 3
#check_2 failed 2730
#check_3 failed 0