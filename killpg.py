#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import signal
import sys

def kill(pid)
	os.killpg(os.getpgid(pid), signal.SIGTERM)

if( __name__ == '__main__' ):
	kill(int(sys.argv[1]))

# killpg
# https://getpocket.com/a/read/1646046964
