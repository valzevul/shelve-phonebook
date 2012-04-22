# -*- coding: utf-8 -*-

import sys, shelve

filename = 'phonebook.tp'
AskNumber = "Введите номер телефона: "
AskName = "Введите имя: "
AskLocation = "Введите адрес: "
SayNothing = "Ничего не найдено!\n"
SayNumberInfo = "Номер '%s' принадлежит контакту %s, проживающему по адресу: %s.\n"
SayNameInfo = "Контакту %s, проживающему по адресу: %s, принадлежит номер '%s'.\n"
ErrorLocation = "В телефонной книге обнаружено несколько пользователей с таким именем. Пожалуйста, укажите адрес:\n"
SayAll = "%s проживает по адресу: %s. Его номер: %s.\n"
Welcome = "Ваш выбор:\n"
menu = "Добро пожаловать в телефонную книгу!\nГлавное меню\nНажмите —\n'1' чтобы добавить номер в телефонную книгу\n'2' чтобы удалить номер из телефонной книги\n'3' чтобы найти номер по имени в телефонной книге\n'4' чтобы просмотреть все записи\n'5' чтобы найти имя по номеру в телефонной книге\n'0' чтобы выйти из телефонной книги\n"


db = shelve.open(filename)

def add(db):
	name = input(AskName)
	phone = input(AskNumber)
	location = input(AskLocation)
	db[phone] = {'name': name, 'location': location}

def delete(db):
	del db[input(AskNumber)]

def searchByPhone(db):
	phone = input(AskNumber)
	if (phone in db):
		name = str(db[phone]['name'])
		location = str(db[phone]['location'])
		return SayNumberInfo % (phone, name, location)
	else:
		return SayNothing

def searchByName(db):
	name = input(AskName)
	flag, answer, count = False, [], 0
	for phone in db:
		if (name == db[phone]['name']):
			flag = True
			count += 1
			location = str(db[phone]['location'])
			answer.append(SayNameInfo % (name, location, phone))
	if (count > 1):
		location = str(input(ErrorLocation))
		for i in range(len(answer)):
			if (location in answer[i]):
				return answer[i]
	if (not flag):
		return SayNothing
	else:
		return answer[0]

def show(db):
	phones = list(db.keys())
	phones.sort()
	for phone in phones:
		name = str(db[phone]['name'])
		location = str(db[phone]['location'])
		print(SayAll % (name, location, phone))

def main():
	while True:
		print(menu)
		choice = int(input(Welcome))
		if choice == 1:
			add(db)
		elif choice == 2:
			delete(db)
		elif choice == 3:
			print(searchByName(db))
		elif choice == 4:
			show(db)
		elif choice == 5:
			print(searchByPhone(db))
		elif choice == 0:
			db.close()
			sys.exit(0)

if __name__ == "__main__":
    main()
