#!/usr/bin/pythoncustom

import sys
import os

print ('args:'+ str(sys.argv))
print ("bool param: "+ os.environ.get('VELOCITY_PARAM_booleanParam'))
print ("masked param: "+ os.environ.get('VELOCITY_PARAM_maskedParam'))
print ("integer param: "+ os.environ.get('VELOCITY_PARAM_integerParam'))
print ("double param: "+ os.environ.get('VELOCITY_PARAM_doubleParam'))
print ("test_custom param: "+ os.environ.get('VELOCITY_PARAM_test_custom'))
print ("secret param: "+ os.environ.get('VELOCITY_PARAM_secretParam'))