class Tester:
    def __init__(self, solution):
        self.solution = solution

    def handle(self, inp, out, ans=None, verdict=None, checker_log=None):
        print("exit code:", out[2])
        if verdict is not None:
            print("verdict:", verdict)
        print()

        print("Input")
        print(inp)

        print("Output")
        print(out[0])

        if out[1]:
            print("Error")
            print(out[1])

        if ans is not None:
            print("Answer")
            print(ans)

        if checker_log is not None:
            print("Checker Log")
            print(checker_log)

        print("-" * 80)

    def run_testcases(self, testcases):
        for testcase in testcases:
            out = self.solution(testcase[0])

            if out[2]:
                verdict = "RUNTIME ERROR"
            elif out[0] == testcase[1]:
                verdict = "OK"
            else:
                verdict = "WRONG ANSWER"

            self.handle(testcase[0], out, testcase[1], verdict)

    def run_inputs(self, inputs, checker=None):
        checker = (lambda inp, out:
                   (None, None)) if checker is None else checker

        for inp in inputs:
            out = self.solution(inp)

            if out[2]:
                verdict = "RUNTIME ERROR"
            else:
                verdict, checker_log = checker(inp, out[0])

            self.handle(inp, out, verdict=verdict, checker_log=checker_log)
