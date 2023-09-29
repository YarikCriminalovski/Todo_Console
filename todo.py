# Модулі
import sys
import json

# Змінні

# Системні змінні
running = True 
dont_show = False

# Змінна доступних функцій
avaible_functions = (
					'Додати задачу', 'Подивитися задачі',
					'Відмітити задачу як виконану',
					'Видалити задачу', 'Відкрити задачі',
					'Вихід'
					)

# Змінна списку задач
tasks = {}
completed_tasks = []

# Функції

# Функція збереження задач
def save_file(tasks:dict):
	with open("list.txt", "w") as file:
		for key, value in tasks.items():
			file.write(f"{key}:{value}\n")


# Функція збереження всіх виконаних задач
def save_completed(completed_tasks:list):
	with open("completed.txt", "w") as file:
		for i in completed_tasks:
			file.write(f"{i}\n")


def load_completed(completed_tasks:list):
	with open("completed.txt", "r") as file:
		for line in file:
			value = line.strip()
			completed_tasks.append(value)

	print(completed_tasks)
	return completed_tasks

# Функція для відкриття задач
def open_file(tasks:dict) -> dict:
	with open("list.txt", "r") as file:
		for line in file:
			key, value = line.strip().split(':')

			tasks[key] = value

	return tasks

# Функція виводу всіх можливостей задачника
def printing_functions(avaible_functions:tuple) -> str:
	print("\n")
	# Вивід всіх функцій
	for i in enumerate(avaible_functions):
		print(f"{i[0]+1}. {i[1]}")


# Функція управління вибором
def choose_function():
	printing_functions(avaible_functions)
	temp_answer = input("\nЩо зробити?: ")
	if (temp_answer == 'Додати задачу' or 
			temp_answer == 'додати задачу'):
		add_task(tasks)
	elif (temp_answer == 'Подивитися задачі' or
			temp_answer == 'подивитися задачі'):
		show_tasks(tasks,completed_tasks)
	elif (temp_answer == 'Відмітити задачу як виконану' or
			temp_answer == 'відмітити задачу як виконану'):
		mark_task(tasks,completed_tasks)
	elif (temp_answer == 'Видалити задачу' or
			temp_answer == 'видалити задачу'):
		delete_task(tasks,completed_tasks)
	elif (temp_answer == 'Відкрити задачі' or
			temp_answer == 'відкрити задачі'):
		open_file(tasks)
		load_completed(completed_tasks)
	elif (temp_answer == 'Вихід' or temp_answer == 'вихід'):
		program_exit()


# Функція для додавання задач
def add_task(tasks:dict) -> dict:
	print("\nВведіть назву задачі: ")
	temp_name = input("\n")
	print("\nВведіть опис задачі: ")
	temp_description = input("\n")
	tasks[temp_name] = temp_description
	print("\nЗадача додана!")

	save_file(tasks)

	return tasks


# Функція для показу задач
def show_tasks(tasks:dict, completed_tasks:list) -> dict:
	for key in tasks:
		if key in completed_tasks:
			print(f"\n{key}: {tasks[key]}. Виконані: так.")
		elif key not in completed_tasks:
			print(f"\n{key}: {tasks[key]}. Виконані: ні.")

	return tasks


# Функція для відмітки задачі
def mark_task(tasks:dict,completed_tasks:list) -> dict:
	temp_index = input("\nВведіть назву задачі: ")
	for key in tasks:
		if temp_index == key:
			print("\nЗадача знайдена! Бажаєте її позначити як виконану?")
			temp_answer = input("\n(Так/Ні): ")
			if temp_answer == 'Так' or temp_answer == 'так':
				print(f"Задачу {key} позначено як виконану!")
				completed_tasks.append(key)
			elif temp_answer == 'Ні' or temp_answer == 'ні':
				print("Ви не захотіли позначати її як виконану.")
			else:
				break

	save_file(tasks)
	save_completed(completed_tasks)

	return tasks


# Функція для виходу з программи
def program_exit() -> bool:
	running = False
	sys.exit()

	return running

# Функція для видалення задачі
def delete_task(tasks:dict,completed_tasks:list) -> dict:
	temp_index = input("\nВведіть назву задачі: ")
	keys_to_delete = []

	for key in tasks:
		if temp_index == key:
			print("\nЗадача знайдена! Бажаєте її видалити?")
			temp_answer = input("\n(Так/Ні): ")
			if temp_answer == 'Так' or temp_answer == 'так':
				print(f"Задачу {key} було видалено!")
				keys_to_delete.append(key)
			elif temp_answer == 'Ні' or temp_answer == 'ні':
				print("Ви не захотіли видаляти задачу.")
			else:
				break

	for key in keys_to_delete:
		del tasks[key]

	for i in keys_to_delete:
		del completed_tasks[completed_tasks.index(i)]
		
	save_file(tasks)
	save_completed(completed_tasks)

	return tasks

while running:
	choose_function()