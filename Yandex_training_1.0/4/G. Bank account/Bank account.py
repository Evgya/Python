def balance(line):
    print(clients.get(line[0], "ERROR"))


def deposit(line):
    clients[line[0]] = clients.setdefault(line[0], 0) + int(line[1])


def transfer(line):
    clients[line[0]] = clients.setdefault(line[0], 0) - int(line[2])
    clients[line[1]] = clients.setdefault(line[1], 0) + int(line[2])


def income(line):
    for key in clients.keys():
        if clients[key] > 0:
            clients[key] += int(clients[key]*(int(line[0])/100))


def withdraw(line):
    clients[line[0]] = clients.setdefault(line[0], 0) - int(line[1])


operations = {
    "DEPOSIT": deposit,
    "WITHDRAW": withdraw,
    "TRANSFER": transfer,
    "INCOME": income,
    "BALANCE": balance
}

clients = dict()
_file = open("input.txt")

for line in _file:
    _line = line.split()
    operations[_line[0]](_line[1:])

_file.close()
