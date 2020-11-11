#!/usr/bin/env python3
from pathlib import Path
from subprocess import PIPE, run

GIT_VERSION_COMMAND = [
    'git',
    'describe',
    '--dirty',
    '--always',
    '--abbrev=12',
]
CPP_VERSION_TEMPLATE = 'constexpr char version[] = "{version}";'

def get_git_version() -> str:
    try:
        proc = run(GIT_VERSION_COMMAND, stdout=PIPE, check=True)
        git_version = proc.stdout.decode('utf-8').strip().lstrip('v')
        return git_version
    except Exception:
        return '?'

def main():
    repo_root = Path(__file__).parent.parent
    include_file = repo_root / 'include/SalmonVersion.hpp'
    git_version = get_git_version()
    print('Writing version', git_version, 'to', include_file)
    with open(include_file, 'w') as f:
        print(CPP_VERSION_TEMPLATE.format(version=git_version), file=f)

if __name__ == '__main__':
    main()
