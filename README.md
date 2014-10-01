###**About:**

This is a simple django-haystack example that uses Solr as the backend. It is based on the official django-haystack tutorial (http://django-haystack.readthedocs.org/en/latest/tutorial.html). Here, we’ll be adding **search functionality to a simple note-taking application.**


####**Basic Setup:**####

* Django
* django-haystack
* pysolr

Install the following using the commands:

```
$ pip install django
$ pip install django-haystack
$ pip install pysolr
```

#####**Solr setup:**#####

For haystack connections, i am using Solr as the backend so Solr needs to be setup.To run the Solr server, Java must be installed on your machine. If you don't have Java installed in your system, first install it using the steps below:

```
 $ sudo add-apt-repository ppa:webupd8team/java
 $ sudo apt-get update
 $ sudo apt-get install oracle-java7-installer
 $ sudo apt-get install oracle-java7-set-default
 $ java -version
```
After installing java, download Solr from its official site (https://lucene.apache.org/solr/downloads.html) and extract it. I used Apache Solr 4.10.1. It is not necessary that it must reside in the project directory. Now after extracting it, go to the extracted folder in terminal.
```
 $ cd <extracted_folder_path>/solr-4.10.1/example/
 $ java -jar start.jar
```
 This will start Solr server on port 8983. You can check if the Solr server has started by typing `http://127.0.0.1:8983/solr/` on your browser.


####**Running the project**####

 1.  **Download** and in the terminal, move into the project simple_django_haystack_solr_example.
     ```
     $ cd <your_project_path>/simple_django_haystack_solr_example/
     ```

 2.  **Setup the database:**

    I have used mysql as the database for the project. For that ,you will have to create a database in mysql using       its shell. You can use any name for your database but then change the database name  in your project's settings.py file accordingly.
     ```
     mysql> create database solr_tutorial character set utf8
     ```

    Now move into the simple_django_haystack_solr_example folder in your terminal.
    ```
    $ cd <your_project_path>/simple_django_haystack_solr_example/
    $ python manage.py syncdb
    ```
    This will create all the database tables for our project.

 3.  **Generate the schema**

     Solr’s configuration is XML-based, so we’ll need to manually regenerate the schema. Run the following command first from your project inside terminal, drop the XML output in your Solr’s schema.xml file and restart your Solr  server.

     ```
     $ python manage.py build_solr_schema
     ```
     Solr's xml file can be found at the following path:
     ```
     <extracted_folder_path>/solr-4.10.1/example/solr/collection1/conf/schema.xml
     ```
     I have added my Solr conf file for schema.xml in case you get stuck here.

 4.  **Create some test data** for creating the indexes.

 5.  **Start solr server:**

     ```
     $ sudo java -jar start.jar
     ```
 6.  **Build solr index:**

     ```
     $ python manage.py rebuild_index
     ```
     By doing this, you’ll get some totals of how many models were processed and placed in the index.

 7. **Run the Django development server:**

     ```
     $ python manage.py runserver
     ```
 8. **Go to search page:**

     ```
     http://localhost:8000/search
     ```
