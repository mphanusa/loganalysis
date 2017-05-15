# Log Analysis

## Summary
This Python program analyzes log records from a website.  In addition to the log-records table, the database also contains two other tables about authors and articles that they wrote.  The goal for this program is to answer three questions:
1) What are the most popular 3 articles viewed of all time?
2) Who are the most popular article authors of all time?
3) On which days did more than 1% of requests lead to errors?

A database named 'news' is set up with:
1) 3 tables articles, authors, and logs.
2) Views will be created to facilitate queries in the program.

The program uses SQL statements to do most the work for performance reason.  Output of the program is listed in the last section.

## Installation

 - Follow instruction to install a [Virtual Machine and vagrant](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0).  The instructions show tools like vagrant and Virtual Box to install and manage the VM-  This will provide the PostgreSQL database and support software needed for this project.
 - Bring the virtual machine back online (with **vagrant up**), do so now. Then log into it with **vagrant ssh**.
 - [Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) Unzip and extract a file called *newsdata.sql*-  Put this file into the *vagrant* directory, which is shared with your virtual machine.
 - Load the data, use the command *psql -d news -f newsdata.sql*.  This will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
 - The following views need to be created by running psql news

	1. create view articleViewCount as select title, count(path) from articles join log on substring(path from 10) = articles.slug where status='200 OK' group by title order by count desc;

	2. create view titleToAuthor as select articles.title, authors.name from articles join authors on author=authors.id;

	3. create view view_days_with_requests as select to_char(time, 'Mon-DD-YYYY') as day_with_requests, count(*) as total_Requests from log group by day_with_requests;

	4. create view view_days_with_errors as select to_char(time, 'Mon-DD-YYYY') as day_with_errors, count(*) as total_errors   from log where status <> '200 OK' group by day_with_errors;

	5. create view view_dailyErrorPercent as select day_with_errors, (total_errors*100.0/total_requests) as errorpercent, total_requests, total_errors from view_days_with_errors, view_days_with_requests where day_with_errors = day_with_requests;

 - Fork this [repository](https://github.com/mphanusa/loganalysis.git) to create your own copy in GitHub. Then clone your loganalysis repository to run this project locally on your computer.  Note: the files must be inside the **/vagrant/** directory.
 - Run the program: python logs.py


 # Ouput

 vagrant@vagrant:/vagrant/Logs Analysis$ python3 logs.py

Report for answers on 3 questions generated on 5/14/2017

The most popular 3 articles viewed of all time:
        Candidate is jerk, alleges rival - 338647 views
        Bears love berries, alleges bear - 253801 views
        Bad things gone, say good people - 170098 views

The most popular article authors:
        Ursula La Multa - 507594 views
        Rudolf von Treppenwitz - 423457 views
        Anonymous Contributor - 170098 views
        Markoff Chaney - 84557 views

Day(s) when more than 1% of requests led to errors:
        Jul-17-2016 - 2.3% errors
