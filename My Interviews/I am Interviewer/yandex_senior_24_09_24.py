if is_valid() == True:
    ...


if is_valid() is True:
    ...


if is_valid():
    ...


if a is None:
    ...


class CustomIterator:
    def __init__():
        list_obj = [1, 2, 3]
        cur_pos = -1
        
    def __next__():
        self.cur_pos += 1
        if self.cur_pos >= list_obj:
            raise StopIteration
            
        return list_obj[self.cur_pos]   
    
    def __iter__():
        self.cur_pos = -1
        return self


def get_gen():
    yield db_get_next_page()


a = get_gen()
while True():
    print(next(a))


a = CustomIterator()

for item in a:
    print(item)
    

for item in a:
    print(item)
     

s = set()
var in s:
    ...
O(1)


l = []
var in l:
    ...
O(n)
      

class User:    
    self.id: UUID
    self.name: str
    

users = get_users()

name = "Влад"


def log(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response is None:
            print('No resp from func')
        return response
    return wrapper


@log
def some_code():
    for user in users:
        if user.name == name:
            return user


my_user = some_code()
if my_user is None:
    print('No such user')


        
# чему будет равно значение переменной count после исполнения кода?
from threading import Thread, Lock


lock = Lock()
count = 0


def inc():
    sleep(1)
    with lock():
        global count
        count += 1


threads = []
for i in range(100):
    thread = Thread(inc)
    threads.append(thread)


for t in threads:
    t.join()    


print(count)




     85
8       242



Есть 2 сервиса, биллинговый и сервис бронирования комнаты гостиницы.


Пользователь бронирует компанату гостиницы, отсылая запрос в указанный сервис. (POST /reservation), 
сервис гостиницы должен списать деньги у пользователя в сервисе биллинга (POST /draw-money). 
Как это реализовать с поддержанием консистентности.

// reserve_service.reservation (Python) | DB Postgres
...
lock_for_update(room)
success = try_payment(sum, timeout=5)
if success:
    update(room)
unlock(room)


// payment_service.draw-money (Java) | MongoDB
...
