# -*- coding: utf-8 -*-
from robot.parsing import TestCaseFile
import os, re

def print_parallel_testcase_name(testfile, include_tag='core', exclude_tag='regression'):
    suite = TestCaseFile(source=testfile).populate()
    for test in suite.testcase_table:
        if test.tags and include_tag in test.tags.value and exclude_tag not in test.tags.value:
            print test.name, test.tags.value


def print_dir_parallel_testcase_name(folder="/Users/jollychang/Work/shire/webtests/", include_tag='core', exclude_tag=''):
    #print folder
    for root, dirs, files in os.walk(folder):
        for f in files:
            if bool(re.match('test\_.*\.txt$', f)):
                absoulte_path = os.sep.join([root, f])
                print_parallel_testcase_name(absoulte_path, include_tag, exclude_tag)

if __name__ == '__main__':
    print_dir_parallel_testcase_name(folder="/Users/jollychang/Work/shire/webtests/", include_tag='core')