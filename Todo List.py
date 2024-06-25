tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list!! Make sure to complete it! ૮₍ • ˕ - ₎ა♡") 

def listTasks():
    if not tasks:
        print("There are currently no tasks.. let's add some! (ㅅ´ ˘ `)")
    else:
        print("""
════════════════ஓ๑♡๑ஓ════════════════
 Your Current Tasks: """)
        for index, task in enumerate(tasks):
            print(f"""  Task #{index + 1}. {task}""")
        print("════════════════ஓ๑♡๑ஓ════════════════")

def deleteTask():
    listTasks()
    try: 
        taskToDelete = int(input("Enter the # you want to remove: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete - 1)
            print(f"Great job!!! Here's a cute flower for getting '{taskToDelete}' done! (*ᴗ͈ˬᴗ͈)ꕤ") or print(f"Awesome work soldier ദ്ദി ˉ͈̀꒳ˉ͈́ )✧ here's some energy to replenish for completing '{taskToDelete}'!")
    except:
        print("Erm I don't think that's a valid task number! Try again!")



if __name__ == "__main__":
    print("Welcome to the To-Do List App! Bunny is so happy to have you here ૮ ˶ᵔ ᵕ ᵔ˶ ა !")
    while True:
        print("\n")
        print(""" 
              ╭────────────────── · · ୨୧ · · ──────────────────╮
                  Please select one of the following options!
                 ---------------------------------------------
                  1. Add a task
                  2. Delete a task
                  3. List tasks
                  4. Quit app
                 ---------------------------------------------
                   ⸜(｡˃ ᵕ ˂ )⸝♡ \"What's your pick?? Tell mee!\" 
              ╰────────────────── · · ୨୧ · · ──────────────────╯
              """)
        
        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()

        elif(choice == "2"):
            deleteTask()

        elif(choice == "3"):
            listTasks()
            
        elif(choice == "4"):
            break

        else:
            print("That's not an option...(っ- ‸ - ς) pick a real one! <(￣︶￣)↗ (1, 2, 3, 4)") or print("That's not an option...(っ- ‸ - ς) c'mon let's pick a real one! (σﾟﾛﾟ)σ (1, 2, 3, 4)")


print("So sad to see you go... here's a heart to take with you (੭ ˊ^ˋ)੭ ♡")