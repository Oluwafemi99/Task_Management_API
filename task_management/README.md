This is a task management app thats helps manage tasks effectively.
Necessary permissions are utilized to give user confidence and also help secure thier tasks
task have different priority levels which are 'low', 'medium', and 'high'
task status can also be change from 'pending' to 'completed'


some of the end points tested are as follows

using Patch or put method this end point change the status to comleted 
http://127.0.0.1:8000/task_management/tasks/pk/complete/

changing to pending status with this
http://127.0.0.1:8000/task_management/tasks/pk/incomplete/


using Get method this get the user details
http://127.0.0.1:8000/task_management/user/pk/details/


using Delete Method this delete the task
http://127.0.0.1:8000/task_management/tasks/pk/delete/


using Post method this Create the task
http://127.0.0.1:8000/task_management/tasks/create/

using get method, this get the user list Admin authorised only
http://127.0.0.1:8000/task_management/user/list/


using post method this is the Login view
http://127.0.0.1:8000/task_management/login/


using Post method this get you logout
http://127.0.0.1:8000/task_management/logout/


using Get method this is is the task list
user dont have access to other user task
http://127.0.0.1:8000/task_management/tasks/list/