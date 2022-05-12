#!/usr/local/bin/python
import argparse
from distutils.log import error

# VARIABLES
# ----------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument('version', help='version a modificar')
parser.add_argument('-M', '--major', help='Major', default=0)
parser.add_argument('-m', '--menor', help='Menor', default=0)
parser.add_argument('-p', '--patch', help='Patch', default=0)

args = parser.parse_args()


try:
    major = int(args.major)
    minor = int(args.menor)
    patch = int(args.patch)
    version = args.version
except Exception as e:
    print('Tipo incorrecto, debe ser de tipo int')
    exit(1)


# SCRIPT
# ----------------------------------------


try:
    version_major = int(str(version).split('.')[0])
    version_minor = int(str(version).split('.')[1])
    version_patch = int(str(version).split('.')[2])
except Exception as e:
    print('Formato incorrecto, debe ser: int.int.int')
    exit(1)


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
