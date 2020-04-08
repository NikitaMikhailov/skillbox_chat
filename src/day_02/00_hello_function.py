"""
Пример программы для работы с функциями

Сделать
- функцию hello, которая выводит текст приветствия клиенту
"""

def hello_clients(clients: list):
    for user in clients:
        print(f"Hello, {user}")

clients = ['John', 'David', 'Kate', 'Alex']
hello_clients(clients)

clients_two = ['Nikita']
hello_clients(clients_two)

