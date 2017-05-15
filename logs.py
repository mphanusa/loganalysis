# This program analyze logs recorded by a website.  The goal is to answer three questions:
# 1) What are the most popular 3 articles viewed of all time?
# 2) Who are the most popular article author of all time?
# 3) On which days did more than 1% of requests lead to errors?

# A database 'news' is set up with:
# 1) 3 tables articles, authors, and logs
# 2) Views will be created to facilitate queries in the program

# This Python program is to use SQL statements and views to do most the work for performance reason.

import psycopg2

dbConn = psycopg2.connect("dbname=news")
tabl = dbConn.cursor()


print("\nReport for answers on 3 questions generated on 5/14/2017")

# 1) What are the most popular 3 articles viewed of all time?
print("\nThe most popular 3 articles viewed of all time:")
a1Select = "select title, count from articleViewCount limit 3;"
tabl.execute(a1Select)
for row in tabl:
    article = row[0]
    numOfViews = row[1]
    print("\t%s - %d views" % (article, numOfViews))


# 2) Who are the most popular article authors of all time?
print("\nThe most popular article authors:")
a2Select = """select titleToAuthor.name, sum(articleViewCount.count)
           from articleVIewCount join titleToAuthor
           on titleToAuthor.title=articleViewCount.title
           group by titleToAuthor.name
           order by sum desc;"""
tabl.execute(a2Select)
for row in tabl:
    name = row[0]
    numOfViews = row[1]
    print("\t%s - %d views" % (name, numOfViews))

# 3) On which days did more than 1% of requests lead to errors?
print("\nDay(s) when more than 1% of requests led to errors:")
a3Select = "select * from view_dailyErrorPercent where errorPercent > 1.0"
tabl.execute(a3Select)
for row in tabl:
    onDay = row[0]
    errorPercent = row[1]
    print("\t%s - %.1f%% errors" % (onDay, errorPercent))

print("\n")

# close down table and database connections
tabl.close()
dbConn.close()