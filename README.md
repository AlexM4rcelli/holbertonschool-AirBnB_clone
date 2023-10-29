<h1 align ="center">
<img src="https://holbertonschool.uy/wp-content/themes/holberton/assets/img/logo.png" height="60%" width="50%">
</h1>

<h1 align ="center">
<img src="https://camo.githubusercontent.com/dd07bdb5f1d850f43898037ed8f72e1d53af03841b08cabf09303f5902c3509f/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67" height="60%" width="50%">
</h1>

<div align="center">
<h1>What is this project about?</h1>
</div>

<span style="font-size: 24px;">The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.
You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.</span>

<span style="font-size: 24px;">After 4 months, you will have a complete web application composed by:</span>

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

<div align="center">
  <h1>Classes</h1>
</div>

## The project will use the following classes for its correct functioning:

|     | BaseModel | FileStorage | User | Amenity | City | State | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| Public instance attributes | id<br>created_at<br>updated_at | | Inherits from BaseModel | Inherits from BaseModel | Inherits from BaseModel | Inherits from BaseModel | Inherits from BaseModel | Inherits from BaseModel |
| Public instance methods | save<br>to_dict | all<br>new<br>save<br>reload |  |  |  |  |  |  |
| Public class attributes | | | email<br>password<br>first_name<br>last_name| name | name_id<br>name | name | city_id<br>user_id<br>name<br>description<br>number_rooms<br>number_bathrooms<br>max_guest<br>price_by_night<br>latitude<br>longitude<br>amenity_ids | place_id<br>user_id<br>text |
| Private class attributes | | file_path<br>objects | | | | | | |


<div align="center">
  <h1>Console</h1>
</div>
The console is a Command Line Interface (CLI) tool that serves as a backend utility. It provides the capability to interact with and manage all the pre-defined classes that have been previously loaded into the storage object.

<p align="center">
  <img src="https://camo.githubusercontent.com/7af0e655c34b0f4fac08af12c02b47ae017dcbc4fcaa06117b81234bb5f3c7fc/68747470733a2f2f692e696d6775722e636f6d2f6c675a6e5a727a2e706e67" alt="storage">
</p>

## Console description.

* ```quit``` - exits console
* ```create``` - Creates a new instance of ```BaseModel```, saves it (to the JSON file) and prints the id.

* ```destroy``` - Deletes an instance based on the class name and id (save the change into the JSON file).
* ```show``` - Prints the string representation of an instance based on the class name and id.
* ```all``` - Prints all string representation of all instances based or not on the class name.
* ```update``` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).


<div align="Center">
  <h1>Examples</h1>
</div>


- Run console in interactive mode:

```$ 
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

- Run console in Non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Authors
| [<img src="https://avatars.githubusercontent.com/u/135631203?v=4" width=115><br><sub> Franco Doldan </sub>](https://github.com/FrancoDoldan0) |  [<img src="https://avatars.githubusercontent.com/u/135648091?v=4" width=115><br><sub>Alex Marcelli </sub>](https://github.com/AlexM4rcelli) |
| :---: | :---: |