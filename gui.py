import functions_todo
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:   # create a file if it doesn't exist
        pass

sg.theme("Dark Amber 2")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

#to make the add button with image
#add_button = sg.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add todo", key="add")

#edit
list_box = sg.Listbox(values=functions_todo.get_todos(), key="todos",
                      enable_events=True, size=[40, 20])

edit_button = sg.Button("Edit")

#complete
done_button = sg.Button("Done")

#exit button
exit_button = sg.Button("Exit")

window = sg.Window('Prathu to-do App', layout=[[clock],
                                               [label],
                                               [input, add_button],
                                               [list_box, edit_button, done_button],
                                               [exit_button]],
                   font=('Times New Roman', 15))
while True:
    event, values = window.read(timeout=200)
    print(f"Event: {event} Values: {values}")
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            try:
                todos = functions_todo.get_todos() #get the todos from the file
                print(todos)
                new_todo = values['todo'] + "\n" # add the new todo
                todos.append(new_todo)
                functions_todo.write_todos(todos) # write the new todo into the file
                window['todos'].update(values=todos)
            except ValueError:
                sg.popup("Please add the todo", font=("Times New Roman", 15))
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = functions_todo.get_todos()  # get the list
                index = todos.index(todo_to_edit)  # get the index you want to edit
                todos[index] = new_todo  # edit the todo
                functions_todo.write_todos(todos)  # save the new updated list
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("You should select a todo to edit first...", title="Error", font=("Times New Roman", 15))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Done":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions_todo.get_todos()
                todos.remove(todo_to_complete)
                functions_todo.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("You should select a todo to complete...", title="Error", font=("Times New Roman", 15))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
            
#close the window
print("Bye")
window.close()
