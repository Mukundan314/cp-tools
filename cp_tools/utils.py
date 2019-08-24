import subprocess
import sys
import traceback

if sys.version_info[0] >= 3:
    from io import StringIO as stream
else:
    from io import BytesIO as stream


def sol2func(func):
    def new_func(inp):
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        old_stderr = sys.stderr

        sys.stdin = stream(inp)
        sys.stdout = stream()
        sys.stderr = stream()

        try:
            exit_code = func() or 0
        except SystemExit as e:
            exit_code = e.code
        except Exception:
            traceback.print_exc()
            exit_code = 1
        finally:
            out = sys.stdout.getvalue()
            err = sys.stderr.getvalue()

            sys.stdin = old_stdin
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        return out, err, exit_code

    return new_func


def cmd2func(cmd):
    def func(inp):
        with subprocess.Popen(cmd,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE) as process:
            out, err = process.communicate(inp.encode())
            exit_code = process.poll()

        return out.decode(), err.decode(), exit_code

    return func
