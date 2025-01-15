import json

class ToDo:
    def __init__(self, file_name='ToDoFile.json'):
        self.file_name = file_name
        self.json_object = self.load_json()
        self.json_object={k.lower(): v.lower() for k, v in self.json_object.items()}
        
    def load_json(self):
        try:
            with open(self.file_name, 'r') as openfile:
                return json.load(openfile)
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: File '{self.file_name}' contains invalid JSON.")
            return {}
        
    def addTask(self, task):
        task=task.lower()
        self.json_object[task]="not done"
        return "Task added in todo list and is marked as not done by default."
    def viewTasks(self):
      if len(self.json_object)!=0:
         print("All tasks in todo list are listed below:\n\n")
         for key,value in self.json_object.items():
           print(key,value)
      else:
         print("Todo list is empty")
      
    def deleteTask(self, task):
     task=task.lower()
     if task in self.json_object:
       del self.json_object[task]
       self.viewTasks()
       return 'Task deleted.'
     else:
        return 'Task not present in todo list.'
    
    def updateTask(self, task):
      task=task.lower()
      if task in self.json_object:
       self.json_object[task]='done'
       return 'Task updated as done.'
      else:
        return 'Task not present in todo list'
       
    def writeToFile(self):
       with open('ToDoFile.json', 'w') as fp:
        json.dump(self.json_object, fp)
      

todo = ToDo()  # todo list object
check=True    #check to exit app if user wants
print("\n\n###################################    TODO LIST  ################################### ")
while check:
 operation=input("Enter the serial number of the operation you want to perform:\n 1)Add task \n 2)Delete Task\n 3)Update Task\n 4)View Tasks\n 5)Exit \n\n")

# Options for user to select to perform an operation
 if operation.isdigit():
     val=int(operation)
     if val==1:
         task=input("Enter task to be added: ")
         print(todo.addTask(task))
     elif val==2:
        task=input("Enter task to be deleted: ")
        print(todo.deleteTask(task))
     elif val==3:
         task=input("Enter task to be updated: ")
         print(todo.updateTask(task))
     elif val==4:
         todo.viewTasks()
     elif val==5: # exiting
          check=False
          todo.writeToFile()
          print("Thank you for using the ToDo app! Goodbye!")
     else:
       print("Serial number does not exist, enter a valid one please!!")
 else:
    print("Serial number does not exist, enter a valid one please!!")
  
        
#print(str(todo.json_object))

 

 
# # Data to be written
# dictionary = {
#     "Do basics": "Done",
#     "Do Advance": 'Not Done',
#     "Do git": 'Done',
#     "Do django": "Not Done"
# }
 
# with open("ToDoFile.json", "w") as outfile:
#     json.dump(dictionary, outfile)




 
# print(json_object)
# print(type(json_object))


# val = input("Enter task: ")
