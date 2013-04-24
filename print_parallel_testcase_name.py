# -*- coding: utf-8 -*-
from robot.parsing import TestCaseFile
from robot import run
import os, re, multiprocessing

testcases = []
folder='/Users/jollychang/Work/shire/webtests/SNS/note'
def print_parallel_testcase_name(testfile, include_tag='core', exclude_tag='regression'):
    suite = TestCaseFile(source=testfile).populate()
    for test in suite.testcase_table:
        if test.tags and include_tag in test.tags.value and exclude_tag not in test.tags.value:
                testcases.append(test.name)

def print_dir_parallel_testcase_name(folder="/Users/jollychang/Work/shire/webtests/", include_tag='core', exclude_tag=''):
    for root, dirs, files in os.walk(folder):
        for f in files:
            if bool(re.match('test\_.*\.txt$', f)):
                absoulte_path = os.sep.join([root, f])
                print_parallel_testcase_name(absoulte_path, include_tag, exclude_tag)


def parallel_run(folder, testname):
    run(folder, test=testname, variable=['SELENIUM_HOST:qa-shire-rc.intra.douban.com', 'SELENIUM_PORT:4444', 'DEFAULT_INIT_TIMEOUT:60', 'AJAX_TIMEOUT:15','remote:yes', 'NOT_INIT:yes', 'DEFAULT_TIMEOUT:30', 'HOST:http://qa-dev.intra.douban.com:10190', 'CONTROL_HOST:http://qa-dev.intra.douban.com:10191', 'DOUBAN_MOVIE:http://movie.qa-dev.intra.douban.com:10190', 'DOUBAN_TOWN:http://alphatown.qa-dev.intra.douban.com:10190', 'DOUBAN_SITE:http://site.qa-dev.intra.douban.com:10190', 'DOUBAN_BOOK:http://book.qa-dev.intra.douban.com:10190', 'DOUBAN_MUSIC:http://music.qa-dev.intra.douban.com:10190', 'DOUBAN_FM:http://qa-dev.intra.douban.fm:10190', 'DOUBAN_DOU:http://dou.qa-dev.intra.douban.com:10190'], report="%s_report.html" % testname, log='%s_log.html' % testname, output='%s_output.xml' % testname)

if __name__=="__main__":
    folder='/Users/jollychang/Work/shire/webtests/SNS/note'
    print_dir_parallel_testcase_name(folder=folder, include_tag='core', exclude_tag='')
    pool = multiprocessing.Pool(processes=4)
    for testcase in testcases:
        pool.apply_async(parallel_run, (folder, testcase, ))
    pool.close()
    pool.join()    