#!/usr/local/bin/python
import argparse
import sys

VERSION = "1.0.0"


# VARIABLES
# ----------------------------------------

if sys.argv[1] == '-v':
    print(VERSION)
    sys.exit(0)

parser = argparse.ArgumentParser(
    description="Calculate new version",
    usage="hera <version in format int.int.int> [-M int] [-m int] [-p int]"
)

parser.add_argument("-v", action="store_true", help="binary version")
parser.add_argument('version', help='base version')
parser.add_argument('-M', help='Major', default=0)
parser.add_argument('-m', help='Menor', default=0)
parser.add_argument('-p', help='Patch', default=0)

args = parser.parse_args()


try:
    major = int(args.M)
    minor = int(args.m)
    patch = int(args.p)
    version = args.version

except Exception as e:
    print('Error on type then must be int')
    sys.exit(1)


# SCRIPT
# ----------------------------------------

try:
    version_major = int(str(version).split('.')[0])
    version_minor = int(str(version).split('.')[1])
    version_patch = int(str(version).split('.')[2])

except Exception as e:
    print('Error ono format then must be: int.int.int')
    sys.exit(1)


if major != 0:
    version_major += major
    version_minor = 0
    version_patch = 0

if minor != 0:
    version_minor += minor
    version_patch = 0

if patch != 0:
    version_patch += patch


version_patch = version_patch if version_patch > 0 else 0
version_minor = version_minor if version_minor > 0 else 0
version_major = version_major if version_major > 0 else 0

print(f"{version_major}.{version_minor}.{version_patch}")
