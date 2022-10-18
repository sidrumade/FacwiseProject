
# Technology Selection: 
### Django REST Framework : 


## User Base
#### CREATE USER  | Method: POST
###### http://localhost:8000/user_base/create_user/

        :param request: A json string with the user details
        {
          "name" : "<user_name>",
          "display_name" : "<display name>"
        }
        :return: A json string with the response {"id" : "<user_id>"}

        Constraint:
            * user name must be unique
            * name can be max 64 characters
            * display name can be max 64 characters

##### payload
 { "name" : "siddhesh","display_name" : "Siddhesh Rumade" }
##### Response:
    """
    {
    "name": "siddhesh",
    "display_name": "Siddhesh Rumade",
    "creation_time": "1665919055000"
    }
    """

#### LIST USERS  | Method: GET
###### http://localhost:8000/user_base/list_user/

        :return: A json list with the response
        [
          {
            "name" : "<user_name>",
            "display_name" : "<display name>",
            "creation_time" : "<some date:time format>"
          }
        ]

##### Response:
    [
    {
        "name": "siddhesh",
        "display_name": "Siddhesh Rumade",
        "creation_time": "1665919055000"
    },
    {
        "name": "vishal",
        "display_name": "Vishal Vide",
        "creation_time": "1665919490000"
    },
    {
        "name": "hitesh",
        "display_name": "Hitesh Mohite",
        "creation_time": "1665919519000"
    },
    {
        "name": "roshan",
        "display_name": "Roshan Morya",
        "creation_time": "1665919553000"
    },
    {
        "name": "kuldeep",
        "display_name": "Kuldeep Gavade",
        "creation_time": "1665919572000"
    },
    {
        "name": "mitul",
        "display_name": "Mitul Desai",
        "creation_time": "1665919590000"
    },
    {
        "name": "vibhu",
        "display_name": "Vibhu Goel",
        "creation_time": "1665919646000"
    }
    ]


#### DESCRIBE USERS  | Method: POST
###### http://localhost:8000/user_base/describe_user/

        :param request: A json string with the user details
        {
          "id" : "<user_id>"
        }

        :return: A json string with the response

        {
          "name" : "<user_name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>"
        }

##### payload:
{
    "id": 2
}
##### Response:
{
    "name": "siddhesh",
    "display_name": "Siddhesh Rumade",
    "creation_time": "1665919055000"
}

#### UPDATE USER | Method:PUT
###### http://localhost:8000/user_base/update_user/

        :param request: A json string with the user details
        {
          "id" : "<user_id>",
          "user" : {
            "name" : "<user_name>",
            "display_name" : "<display name>"
          }
        }

        :return:

        Constraint:
            * user name cannot be updated
            * name can be max 64 characters
            * display name can be max 128 characters

##### payload :
        {
          "id" : 8,
          "user" : {
            "name" : "vibhu",
            "display_name" : "Vibhu__Goel"
          }
        }

##### Response : 
    {
    "name": "vibhu",
    "display_name": "Vibhu__Goel",
    "creation_time": "1665919646000"
    }


#### GET_USER_TEAM  | Method : POST
##### http://localhost:8000/user_base/get_user_teams/
        :param request:
        {
          "id" : "<user_id>"
        }

        :return: A json list with the response.
        [
          {
            "name" : "<team_name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>"
          }
        ]

##### Payload :
    {
    "id": 1
    }

##### Response:
    {
    "id": 2,
    "name": "b-devs",
    "description": "Back End Developer",
    "creation_time": "1665922337000",
    "admin": 1
    }


#### TEAM BASE
##### CREATE TEAM | Method : POST
        :param request: A json string with the team details
        {
          "name" : "<team_name>",
          "description" : "<some description>",
          "admin": "<id of a user>"
        }
        :return: A json string with the response {"id" : "<team_id>"}

        Constraint:
            * Team name must be unique
            * Name can be max 64 characters
            * Description can be max 128 characters
        
##### Payload :
{
          "name" : "b-devs",
          "description" : "Back End Developer",
          "admin": 1
        }
##### Response :

    {
    "id": 2,
    "name": "b-devs",
    "description": "Back End Developer",
    "creation_time": "1665922337000",
    "admin": 1
    }

#### LIST TEAMS  | Method : GET
##### http://localhost:8000/team_base/list_team/

        :return: A json list with the response.
        [
          {
            "name" : "<team_name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>",
            "admin": "<id of a user>"
          }
        ]

##### Response :
    [
    {
        "id": 1,
        "name": "devops",
        "description": "Dev Ops",
        "creation_time": "1665914562000",
        "admin": 1
    },
    {
        "id": 2,
        "name": "b-devs",
        "description": "Back End Developer",
        "creation_time": "1665922337000",
        "admin": 1
    },
    {
        "id": 3,
        "name": "ds-team",
        "description": "Data Scientist",
        "creation_time": "1665923905000",
        "admin": 8
    }
    ]

#### DESCRIBE TEAM  | Method : POST
##### http://localhost:8000/team_base/describe_team/

        :param request: A json string with the team details
        {
          "id" : "<team_id>"
        }

        :return: A json string with the response

        {
          "name" : "<team_name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>",
          "admin": "<id of a user>"
        }

##### Payload :
    {
    "id": 2
    }

##### Response : 
    {
    "id": 2,
    "name": "b-devs",
    "description": "Back End Developer",
    "creation_time": "1665922337000",
    "admin": 1
    }

#### UPDATE TEAMS | Method : POST
##### http://localhost:8000/team_base/update_team/

        :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "team" : {
            "name" : "<team_name>",
            "description" : "<team_description>",
            "admin": "<id of a user>"
          }
        }

        :return:

        Constraint:
            * Team name must be unique
            * Name can be max 64 characters
            * Description can be max 128 characters

##### Payload :
    {
      "id" : 3,
      "team" : {
        "name" : "ds-team",
        "description" : "Data-Scientist",
        "admin": 8
      }
    }

##### Response : 
    {
    "id": 3,
    "name": "ds-team",
    "description": "Data-Scientist",
    "creation_time": "1665923905000",
    "admin": 8
    }

#### REMOVE USER FROM TEAM   | Method : PUT
##### http://localhost:8000/team_base/remove_users_from_team/

        :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "users" : ["user_id 1", "user_id2"]
        }

        :return:

        Constraint:
        * Cap the max users that can be added to 50

##### Payload :
        {
              "id" : 2,
              "users" : [3]
            }





##### LIST TEAMS USERS 
##### http://localhost:8000/team_base/list_team/

        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<user_id>",
            "name" : "<user_name>",
            "display_name" : "<display name>"
          }
        ]

##### Payload: 
    {
    "id": 2
    }

##### Response: 
    
    [
    {
        "name": "siddhesh",
        "display_name": "Siddhesh Rumade",
        "creation_time": "1665919055000"
    },
    {
        "name": "vishal",
        "display_name": "Vishal Vide",
        "creation_time": "1665919490000"
    }
    ]


### Project Board Base

#### CREATE BOARD |  Method : POST
##### http://localhost:8000/project_board_base/create_board/

        :param request: A json string with the board details.
        {
            "name" : "<board_name>",
            "description" : "<description>",
            "team_id" : "<team id>"
            "creation_time" : "<date:time when board was created>"
        }
        :return: A json string with the response {"id" : "<board_id>"}

        Constraint:
         * board name must be unique for a team
         * board name can be max 64 characters
         * description can be max 128 characters


##### Payload :
    {
        "name" : "Backend BUGS BOARD",
        "description" : "This Board contains all bugs related to Backend",
        "team_id" : 2 ,
        "creation_time" : 1665896892084
    }

##### Response:
    {
    "id": 3,
    "name": "Backend BUGS BOARD"
    }


#### LIST BOARDS  | Method : GET
##### http://localhost:8000/project_board_base/list_boards/

    :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<board_id>",
            "name" : "<board_name>"
          }
        ]
    
##### Response :
    [
    {
        "id": 6,
        "name": "Server BUGS BOARD",
        "team_id": 2
    },
    {
        "id": 7,
        "name": "Backend Bug Board",
        "team_id": 2
    },
    {
        "id": 8,
        "name": "Model Bug",
        "team_id": 3
    }
    ]

#### ADD TASK  | Method : POST
##### http://localhost:8000/project_board_base/add_task/

    :param request: A json string with the task details. Task is assigned to a user_id who works on the task
        {
            "title" : "<board_name>",
            "description" : "<description>",
            "user_id" : "<team id>"
            "creation_time" : "<date:time when task was created>"
        }
        :return: A json string with the response {"id" : "<task_id>"}

        Constraint:
         * task title must be unique for a board
         * title name can be max 64 characters
         * description can be max 128 characters

        Constraints:
        * Can only add task to an OPEN board

##### Payload:
        {
            "title" : "Pivot Issus",
            "description" : "Backend pivot table issue",
            "user_id" : 2 ,
            "creation_time" : "2022-10-16 13:33"
        }

##### Response:
    {
    "id": 5
    }

#### UPDATE TASK STATUS  | Method : PUT
##### http://localhost:8000/project_board_base/update_task_status/

    :param request: A json string with the user details
        {
            "id" : "<task_id>",
            "status" : "OPEN | IN_PROGRESS | COMPLETE"
        }

##### Payload :

        {
            "id" : 4,
            "status" : "COMPLETE"
        }


##### CLOSE BOARD   | Method :  POST
##### http://localhost:8000/project_board_base/close_board/

        :param request: A json string with the user details
        {
          "id" : "<board_id>"
        }

        :return:

        Constraint:
          * Set the board status to CLOSED and record the end_time date:time
          * You can only close boards with all tasks marked as COMPLETE

##### Payload :
    {
          "id" : 6
        }

##### Response:
    {
    "id": 6,
    "name": "Server BUGS BOARD",
    "team_id": 2
    }


#### Export Board  | Method : POST
##### http://localhost:8000/project_board_base/export_board/

        Export a board in the out folder. The output will be a txt file.
        We want you to be creative. Output a presentable view of the board and its tasks with the available data.
        :param request:
        {
          "id" : "<board_id>"
        }
        :return:
        {
          "out_file" : "<name of the file created>"
        }

##### Payload :
        {
          "id" : 7
        }

##### Response: 

    {
    "out_file": "output_2022-10-16 17:53:21.416853+00:00.txt"
    }
