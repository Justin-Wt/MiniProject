#PROGRAM BY JUSTIN :)
#The total of 8 hours of making this

#Colors for fun (only works when go to Tools>Build System>Python Terminal) :)
RED = '\033[31m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
GREEN = '\033[32m'
BRIGHT_RED = '\033[91m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_YELLOW = '\033[93m'
BG_BRIGHT_WHITE = '\033[107m'
BRIGHT_WHITE = '\033[97m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_BLACK = '\033[40m'
BG_CYAN = '\033[46m'
RESET = '\033[0m'

#Font Styles
BOLD = '\033[1m'
STRIKETHROUGH = '\033[9m'

#Declaring todo list array
todo_list=[]

#Declaring Definitions
def Add_Task():
	print()
	task=input(f"{BG_BRIGHT_WHITE}{CYAN}Enter the new task:{RESET}{CYAN}")
	todo_list.append(task)
	print(f"{RESET}{RESET}{BRIGHT_WHITE}{BG_GREEN}Task {BRIGHT_RED}{BOLD}'{task}'{RESET}{BG_GREEN}{BRIGHT_WHITE} added!{RESET}")
def View_Task():
	print()
	print(f"{RED}---Current To-Do List---{RESET}")
	for xxxx, task in enumerate(todo_list):
		print(f"{BRIGHT_BLUE}{xxxx+1}. {task}{RESET}")
	print(f"{RED}------------------------{RESET}")
def Complete_Task():
	print()
	View_Task()
	desicion=input(f"{YELLOW}Enter the task to mark as complete: {RESET}")
	print()
	deside=int(desicion)-1
	total=len(todo_list)
	try:
		print(f"{BG_BRIGHT_WHITE}{CYAN}Task {BRIGHT_RED}{STRIKETHROUGH}'{todo_list[deside]}'{RESET}{BG_BRIGHT_WHITE}{CYAN} marked as completed and removed!{RESET}")
		del todo_list[deside]
		print()
	except Exception as e:
		print(f"{BG_RED}{BRIGHT_WHITE}There arent that many to do list")
		print(f"{e}{RESET}")
		print()

#Main Menu
while True:
	print(f"{RED}---To-Do List Manager---{RESET}")
	print(f"{GREEN}1.Add a task{RESET}")
	print(f"{BRIGHT_BLUE}2.View Tasks{RESET}")
	print(f"{BRIGHT_YELLOW}3.Mark a Task Complete{RESET}")
	print(f"{BRIGHT_RED}4.Exit{RESET}")
	print()

#User Interface
	imputs=input(f"{BRIGHT_WHITE}enter your choice (1-4): ")
	choice=int(imputs)
	if choice==1:
		Add_Task()
		print()
	if choice==2:
		View_Task()
		print()
	if choice==3:
		Complete_Task()
		print()
	if choice==4:
		print()
		print(f"{BRIGHT_YELLOW}Goodbye! Have a productive day! {RESET}")
		input("")
		print()
		break