#!/usr/bin/env sh

######################################################################
# @author      : alex (alex@archpad)
# @file        : automated-tests
# @created     : venerdì ott 15, 2021 11:20:39 CEST
#
# @description : 
######################################################################

#echo "Running automated-tests"
#echo "..."

## run unit tests in virtualenv
#$PYENV -m pytest --verbose --junitxml=test-reports/pytest.xml \
#	    			tests/test_unittest.py --disable-warnings
#if [ $? -ne 0  ]; then
#echo “unit tests failed”
#  exit 1
#fi

FOLDER="pihole_api"

# black check:
python -m black --diff $FOLDER/ #$PYFILE #--check $PYFILE

# bandit static code analysis
python -m bandit -r $FOLDER/.*py --verbose -l

if [ $? -ne 0  ]; then
 echo “bandit failed”
  exit 1
fi

# pylint
python -m pylint $FOLDER/*.py --fail-under=8 

if [ $? -ne 0 ]; then
	echo "Pylint test failed"
	exit 1
fi

echo "Test completed!"
