import subprocess


def run_tool(tool, args):
    command = " ".join([tool, *args])
    return subprocess.run(command, shell=True, check=True, capture_output=True)


def run_argv(argv):
    return subprocess.run(argv, check=True, capture_output=True)
