A basic api using the CherryPy framework and Python 3.9.4.

Build it
==========

For building server image:

```
$ docker build -t data .
```

For building client image:

```
$ docker build -t tests .
```

Run it
========

Run it as follows:
for server:

```
$ docker run -d -p 8080:8080 data
```

for client:

```
$ docker run -d -p 8080:8080 tests
```

From your project directory, start up your application by running:
```
$ docker-compose up
```

You can point your browser to http://localhost:8080/ to see the database.

There you also can see the information only about users or departments here:
http://localhost:8080/users/ or http://localhost:8080/department/

If you want to find information about particular user by name or by department name, you can use this link as an example:
http://localhost:8080/users/username or http://localhost:8080/users/department 

You can stop the server as follows:
```
$ docker-compose down
```

You can view the logs like this:
```
$  cat -n example.log
```
