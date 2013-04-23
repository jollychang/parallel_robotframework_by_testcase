# -*- coding: utf-8 -*-
from robot.parsing import TestCaseFile
from robot import run
import os, re

def print_parallel_testcase_name(testfile, include_tag='core', exclude_tag='regression'):
    suite = TestCaseFile(source=testfile).populate()
    for test in suite.testcase_table:
        if test.tags and include_tag in test.tags.value and exclude_tag not in test.tags.value:
            print test.name

def print_dir_parallel_testcase_name(folder="/Users/jollychang/Work/shire/webtests/", include_tag='core', exclude_tag=''):
    #print folder
    for root, dirs, files in os.walk(folder):
        for f in files:
            if bool(re.match('test\_.*\.txt$', f)):
                absoulte_path = os.sep.join([root, f])
                print_parallel_testcase_name(absoulte_path, include_tag, exclude_tag)

def parallel_run(testname=u'用户应该可以发表日记'):
    run('/Users/jollychang/Work/shire/webtests/test_base.txt', test=testname, variable=['SELENIUM_HOST:qa-shire-rc.intra.douban.com', 'SELENIUM_PORT:4444', 'DEFAULT_INIT_TIMEOUT:60', 'AJAX_TIMEOUT:15','remote:yes', 'NOT_INIT:yes', 'DEFAULT_TIMEOUT:30', 'HOST:http://qa-dev.intra.douban.com:10190', 'CONTROL_HOST:http://qa-dev.intra.douban.com:10191', 'DOUBAN_MOVIE:http://movie.qa-dev.intra.douban.com:10190', 'DOUBAN_TOWN:http://alphatown.qa-dev.intra.douban.com:10190', 'DOUBAN_SITE:http://site.qa-dev.intra.douban.com:10190', 'DOUBAN_BOOK:http://book.qa-dev.intra.douban.com:10190', 'DOUBAN_MUSIC:http://music.qa-dev.intra.douban.com:10190', 'DOUBAN_FM:http://qa-dev.intra.douban.fm:10190', 'DOUBAN_DOU:http://dou.qa-dev.intra.douban.com:10190'])



if __name__ == '__main__':
    #print_dir_parallel_testcase_name(folder="/Users/jollychang/Work/shire/", include_tag='core', exclude_tag='')
    parallel_run()