# with open file lastlog.txt for read
# - read single line to variable lastlog
# assign current datetime to variable currlog
# with open file lastlog.txt for write 
# - write currlog as first and only line
# assign currlog-lastlog to variable logdiff
# with open file history.txt for append
# - if logdiff > 15 mins
# - - write currlog+'-'+lastlog+'='+logdiff
# - else:
# - - write currlog
# 
# Comment
