import os
import re
def delete():
    os.system('cls' if os.name == 'nt' else 'clear')

import curses

import sys
import msvcrt
import re

# ANSI colors for Windows Terminal
COLORS = {
    "{black}":   "\033[30m",
    "{red}":     "\033[31m",
    "{green}":   "\033[32m",
    "{yellow}":  "\033[33m",
    "{blue}":    "\033[34m",
    "{magenta}": "\033[35m",
    "{cyan}":    "\033[36m",
    "{white}":    "\033[37m",
    "{end}":     "\033[0m",
}

def colorize(s):
    for tag, code in COLORS.items():
        s = s.replace(tag, code)
    return s

def inline_input(template):
    if "{input}" not in template:
        raise ValueError("Template must contain {input}")

    start, end = template.split("{input}")
    start_c = colorize(start)
    end_c = colorize(end)
    

    # plain text lengths (without ANSI)
    start_len = len(re.sub(r"\033\[[0-9;]*m", "", start_c))
    end_len   = len(re.sub(r"\033\[[0-9;]*m", "", end_c))

    user = ""
    mode="plain"
    while True:
        sys.stdout.write("\r")
        sys.stdout.write(start_c + user + end_c)
        sys.stdout.write("\033[K")   # clear to end
        sys.stdout.flush()

        # Move cursor to after start + user
        sys.stdout.write(f"\r\033[{start_len + len(user)}C")
        sys.stdout.flush()

        # Read one key
        ch = msvcrt.getwch()

        if ch == "\r":     # Enter
            break
        elif ch == "\x08":  # Backspace
            if user:
                user = user[:-1]
        else:
            user += ch

    print()
    return start+user+end

GRAY = "\033[1;30m"
RED = "\033[0;31m]"
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
END = "\033[0m"
ORANGE = "\33[38;5;208m"
my_code=[]
running_code=[]
var_print=[]
Variables_Dict={}
dialogue_config=True
def menu():
	print("hello, what you want to do?")
	print("1.print")
	print("2.make a variable")
	print("3.space")
	print("4.input")
	print("0.tutorials")
	print("see code")
	print("run")
	print(f"dialogue={dialogue_config}")

def tutorial():
	print("hey there. im here to help you in using this code! its pretty similiar on coding in python.")
	print("let me know your name")
	your_name=input(">")
	print(f"so your name is {your_name}? thats a wonderful name")
	input("click enter to continue")
	delete()
	while True:
		print("so heres some option to helps you in coding")
		print(f"1.print tutorials")
		print(f"{GRAY}2.about variable and how to execute it")
		print(f"3.about inputs{END}")
		your_option=input(">")
		try:
			your_option=int(your_option)
		except ValueError:
			print("that wasnt a number")
		else:
			if your_option==1:
				delete()
				print("print code is the most basic code that you will use alot in python")
				print('print is always declared with print("your input")')
				print("to make you more understand about it. lets do it right away")
				input("click enter to continue")
				delete()
				while True:
					print(f"{GRAY}hello, what you want to do?{END}")
					print("1.print")
					print(f"{GRAY}2.make a variable")
					print("3.space")
					print("4.input")
					print("0.tutorials")
					print("see code")
					print("run")
					print(f"dialogue={dialogue_config}{END}")
					print()
					print("this is the menu you saw from before. enter number '1'")
					your_inputs=input(">")
					try:
						your_inputs=int(your_inputs)
					except ValueError:
						print("enter a number")
						input("click enter to continue")
						delete()
						continue
					else:
						if your_inputs != 1:
							delete()
							continue
						if your_inputs == 1:
							delete()
							if dialogue_config==True:
								print("enter anything you want to print")
							printing=inline_input('{blue}print{end}({cyan}\"{green}{input}{cyan}\"{end})')
							start='{blue}print({cyan}\"{green}'
							end='{cyan}\"{blue}){end}'
							raw_input=printing[len(start):-len(end)]
							if raw_input in Variables_Dict:
								function=Variables_Dict[raw_input]
								running_code.append(f"print({raw_input})")
								my_code.append(f'{BLUE}print{END}({raw_input})')
							else:
								try:
									input_print=int(raw_input)
								except ValueError:
									my_code.append(f'{BLUE}print{END}({CYAN}"{GREEN}{raw_input}{CYAN}"{END})')
									running_code.append(f'print("{raw_input}")')
								else:
									variable_print=raw_input
									my_code.append(f'{BLUE}print{END}({ORANGE}{variable_print}{END})')
									running_code.append(f'print({raw_input})')
							delete()
							while True:
								print(f"{GRAY}hello, what you want to do?")
								print("1.print")
								print("2.make a variable")
								print("3.space")
								print("4.input")
								print(f"0.tutorials{END}")
								print("see code")
								print(f"{GRAY}run")
								print(f"dialogue={dialogue_config}{END}")
								print()
								print("now enter 'see code' to check your code")
								your_inputs=input(">")
								if your_inputs != 'see code':
									delete()
									continue
								if your_inputs == 'see code':
									if not my_code:
										print("you didnt make any code yet")
										print()
									else:
										for layer, codes in enumerate(my_code, start=1):
											print(f"{layer}. {codes}")
									print()
									print("this is your current code")
									print("as you can see, the first line is the print code you make earlier")
									input("click enter to continue")
									delete()
									while True:
										print(f"{GRAY}hello, what you want to do?")
										print("1.print")
										print("2.make a variable")
										print("3.space")
										print("4.input")
										print(f"0.tutorials")
										print(f"see code{END}")
										print(f"run")
										print(f"{GRAY}dialogue={dialogue_config}{END}")
										print()
										print("now lets run the code. type 'run'")
										your_inputs=input(">")
										print()
										if your_inputs != 'run':
											delete()
											continue
										if your_inputs == 'run':
											for a, run_code in enumerate(running_code):
												try:
													exec(run_code)
												except ValueError:
													print(f"{RED}{run_code}{END}")
													print("^^^^^^^^^^^^")
													print(f"theres something wrong in line {a+1}")
											print()
											print(f"as you can see. the output of your code is {raw_input}")
											input("click enter to continue")
											delete()
											print("congrats. you finished your first tutorial!")
											input("click enter to continue")
											return
while True:
	delete()
	print("hello, what you want to do?")
	print("1.print")
	print("2.make a variable")
	print("3.space")
	print("4.input")
	print("0.tutorials")
	print("see code")
	print("run")
	print(f"dialogue={dialogue_config}")
	imput=input(">")
	if imput=='1':
		print()
		if dialogue_config==True:
			print("what do you want to print?")
		printing=inline_input('{blue}print{end}({cyan}\"{green}{input}{cyan}\"{end})')
		start='{blue}print{end}({cyan}\"{green}'
		end='{cyan}\"{end})'
		raw_input=printing[len(start):-len(end)]
		if raw_input in Variables_Dict:
			function=Variables_Dict[raw_input]
			running_code.append(f"print({raw_input})")
			my_code.append(f'{BLUE}print{END}({raw_input})')
		else:
			try:
				input_print=int(raw_input)
			except ValueError:
				my_code.append(f'{BLUE}print{END}({CYAN}"{GREEN}{raw_input}{CYAN}"{END})')
				running_code.append(f'print("{raw_input}")')
			else:
				variable_print=raw_input
				my_code.append(f'{BLUE}print{END}({ORANGE}{variable_print}{END})')
				running_code.append(f'print({raw_input})')

	if imput=='2':
		print()
		if dialogue_config==True:
			print("what the name of the variable?")
		input_var=input("")
		print()
		if dialogue_config==True:
			print("what do you want to put")
		variable_input=input(f"{input_var} = ")
		try:
			var_input=int(variable_input)
		except ValueError:
			Variables_Dict[input_var]=variable_input
			my_code.append(f'{input_var} = "{variable_input}"')
		else:
			Variables_Dict[input_var]=variable_input
			my_code.append(f'{input_var} = {variable_input}')
	if imput=='3':
		my_code.append(" ")
	if imput=='4':
		if dialogue_config==True:
			print("what input you want to use? int() or just normal input")
		inputting=inline_input('{blue}print({cyan}\"{green}{input}{cyan}\"{blue}){end}')
		start='{blue}print({cyan}\"{green}'
		end='{cyan}\"{blue}){end}'
		your_input=inputting[len(start):-len(end)]		
		if "int(" in your_input:
			if ')"' not in your_input:
				your_input=your_input+'")'
			running_code.append((f'{BLUE}input{END}({your_input})'))
			your_input=your_input.replace('int("',f'{BLUE}int{END}({CYAN}"{GREEN}')
			your_input=your_input.replace('")' , f'{END}{CYAN}"{END})')
			my_code.append(f"input({your_input})")
		else:
			running_code.append(f'input("{your_input}")')
			my_code.append(f'{BLUE}input{END}({CYAN}"{GREEN}{your_input}{CYAN}"{END})')
		print(running_code)
		input("")
	if imput=='0':
		tutorial()
	if imput=='see code':
		print()
		if not my_code:
			print("you didnt make any code yet")
			print()
		else:
			for layer, codes in enumerate(my_code, start=1):
				print(f"{layer}. {codes}")
			print()
			input("click enter to continue")
	if imput=='run':
			print()
			for a, run_code in enumerate(running_code):
				try:
					exec(run_code)
				except ValueError:
					print(f"{RED}{run_code}{END}")
					print("^^^^^^^^^^^^")
					print(f"theres something wrong in line {a+1}")
			print()
			input("click enter to continue")
	if imput=='dialogue':
		dialogue_config=False

