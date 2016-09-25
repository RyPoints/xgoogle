# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# This program does a Google search for "quick and dirty" and returns
# 50 results.
#
import sys
from xgoogle.search import GoogleSearch, SearchError
# Sets python to handle full Unicode
reload(sys)
sys.setdefaultencoding('utf-8')

try:
  gs = GoogleSearch("美華")
  gs.results_per_page = 50
  results = gs.get_results()
  for res in results:
    print res.title.encode('utf8')
    print res.desc.encode('utf8')
    print res.url.encode('utf8')
    print
except SearchError, e:
  print "Search failed: %s" % e

