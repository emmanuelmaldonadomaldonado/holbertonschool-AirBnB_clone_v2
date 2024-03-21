<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions. [ORIGINAL CLONE AUTHORS](https://github.com/justinmajetich/AirBnB_clone) Click here to view the original console version.

The *UPDATES* section contains all the major changes made to the console that involve implementing the new database (db) using sqlalchemy as the ORM and MySQL as our database. For the new usage of the project you will need some enviroment variables first.

| env_var | value |
| ----- | ----- |
| HBNB_MYSQL_DB| <db_name>|
| HBNB_MYSQL_USER| <db_user>|
| HBNB_MYSQL_PWD| <db_password>|
|HBNB_MYSQL_HOST | <host_for_db>|
|HBNB_TYPE_STORAGE| <'file'> for local and <'db'> for database|
| HBNB_ENV| for development <'dev'> or for testing <'test'>|

Important to replace the values of these env_var with yours. HBNB_TYPE_STORAGE will be either 'file' if you want to use the local storage or 'db' for the database'.
HBNB_ENV will be 'dev' for development or 'test' to make tests with another database for testing. Make sure to have 2 databases, one for development and one for testing.







## UPDATES

The storage system has been implemented with ORM using SQLAlchemy. The console can now interact with either **file_storage.py** or **db_storage.py**. This duality enables data to be saved locally to a JSON file or to the database, depending on the value of the environment variable `HBNB_TYPE_STORAGE ('db' or 'file')`. All classes for the models have been mapped and relationships between them established. This ensures proper handling of cases where a certain row may be deleted from the database and manages deletions that should follow in case of certain relationships.

###### Example : Create an object for db
Usage: create <class_name> <par="value"> <par=value> <par=value>
```
(hbnb) create State name="california"
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) all
["[State] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000002677FF8C400>, 'updated_at': datetime.datetime(2024, 3, 20, 0, 44, 6),
'name': 'Arizona', 'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2024, 3, 20, 0, 44, 6)}"]
(hbnb) quit


```
###### Example: Show all objects for db
Usage: all <class_name> or all
```
(hbnb) all
["[State] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000002677FF8C400>, 'updated_at': datetime.datetime(2024, 3, 20, 0, 44, 6),
'name': 'Arizona', 'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2024, 3, 20, 0, 44, 6)}"]
(hbnb) quit

```

---

<center><h3>Repository Contents by Project Versions</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Unit Testing | [/tests](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/tree/master/tests) | Unitests for models and storage |
| 2. Updated BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/blob/master/models/base_model.py) | Functionality to recreate an instance of a class from .json or db. Also serves as super class for other classes|
| 3. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) [/models/engine/db_storage.py](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/blob/master/models/engine/db_storage.py)| Defines a class to manage persistent file storage system |
| 4. Console | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 5. Console Updated DB | [console.py](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/blob/master/console.py)|   Update the console with methods allowing the user to create, destroy, show, and update stored data |                                                                           |      |
| 6. Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/blob/master/models/place.py) [/models/city.py](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/blob/master/models/city.py) [/models/amenity.py](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/blob/master/models/amenity.py) [/models/state.py](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/blob/master/models/state.py) [/models/review.py](https://github.com/Antoniofdjs/holbertonschool-AirBnB_clone_v2/blob/master/models/review.py) | Dynamically implements more classes |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>
