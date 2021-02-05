#!/usr/bin/env python
import subprocess
from subprocess import PIPE
import sys

args = sys.argv

proc = subprocess.run("sls deploy -f pre_predict", shell=True, stdout=PIPE, stderr=PIPE, text=True)
date = proc.stdout
print('STDOUT: {}'.format(date))
proc = subprocess.run("aws lambda invoke --function-name pre_predict out --log-type Tail \
# --query 'LogResult' --output text |  base64 -d ", shell=True, stdout=PIPE, stderr=PIPE, text=True)
date = proc.stdout
print('STDOUT: {}'.format(date))

proc = subprocess.run("serverless logs -f pre_predict ", shell=True, stdout=PIPE, stderr=PIPE, text=True)
date = proc.stdout
print('STDOUT: {}'.format(date))
