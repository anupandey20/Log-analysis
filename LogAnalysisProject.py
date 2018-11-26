#! /usr/bin/env python3

import psycopg2

DBNAME = "news"

request_1 = "What are the most popular three articles of all time?"

query_1 = ("SELECT title, count(*) as views FROM articles, log\n"
           "WHERE articles.slug = substring(log.path, 10) GROUP BY title\n"
           "ORDER BY views DESC LIMIT 3;")

request_2 = "Who are the most popular article authors of all time?"

query_2 = ("SELECT authors.name, count(*) as views FROM authors, articles, \n"
           "log WHERE authors.id = articles.author AND \n"
           "articles.slug = substring(log.path, 10) AND \n"
           "log.status = '200 OK' GROUP BY name ORDER BY views DESC;")

request_3 = "On which days did more than 1% of requests lead to errors?"

query_3 = ("SELECT * FROM (SELECT a.day, ROUND(CAST((100*b.requests) as \n"
           "numeric)/ CAST(a.requests as numeric), 2) as errp FROM\n"
           "(SELECT DATE(time) as day, COUNT(status) as requests FROM \n"
           "log GROUP BY day) as a INNER JOIN (SELECT DATE(time) as day, \n"
           "COUNT(status) as requests FROM log WHERE status != '200 OK' \n"
           "GROUP BY day) as b ON a.day = b.day) as t WHERE errp > 1.0;")


# Connect to the database and use above queries to get the results

def get_Results(my_query):
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.DatabaseError, e:
        print("Cannot connect to database")
    c = db.cursor()
    c.execute(my_query)
    results = c.fetchall()
    db.close()
    return results


result1 = get_Results(query_1)
result2 = get_Results(query_2)
result3 = get_Results(query_3)


# Create a function to print results


def print_results(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
    print("\n")


if __name__ == '__main__':
    print(request_1)
    print_results(result1)
    print(request_2)
    print_results(result2)
    print(request_3)
    print("\t" + str(result3[0][0]) + " - " + str(result3[0][1]) + "%")
