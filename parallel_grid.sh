rm -rf static/webtest_report/
find webtests/SNS/ -iname "*test_*.txt" | parallel --tty -j10 pybot -v remote:yes -v SELENIUM_HOST:qa-dev -v SELENIUM_PORT:4444 -v DEFAULT_INIT_TIMEOUT:60 -v AJAX_TIMEOUT:15 -v NOT_INIT:yes -v DEFAULT_TIMEOUT:30  -v HOST:http://qa-dev.intra.douban.com:10110 -v CONTROL_HOST:http://qa-dev.intra.douban.com:10111 -v DOUBAN_MOVIE:http://movie.qa-dev.intra.douban.com:10110 -v DOUBAN_TOWN:http://alphatown.qa-dev.intra.douban.com:10110 -v DOUBAN_SITE:http://site.qa-dev.intra.douban.com:10110 -v DOUBAN_BOOK:http://book.qa-dev.intra.douban.com:10110 -v DOUBAN_MUSIC:http://music.qa-dev.intra.douban.com:10110 -v DOUBAN_FM:http://qa-dev.intra.douban.fm:10110 -v DOUBAN_DOU:http://dou.qa-dev.intra.douban.com:10110 -i core --timestampoutputs --outputdir static/webtest_report/regression/{} {}\; {0..255}\>/dev/null

cd static/webtest_report/regression
xml_list=`find webtests/SNS/ -iname '*.xml'`
rebot $xml_list
find webtests/ -iname '*.png*' -exec ln -s {} ./ \;