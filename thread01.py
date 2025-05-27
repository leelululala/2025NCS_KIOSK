import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1.5)

# print_numbers()
# print_letters()

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads are done!")

# function based
# import threading
#
# def worker():
#     print("work")
#
# t = threading.Thread(target=worker)
# t.start()

# class based
# import threading
#
# class MyThread(threading.Thread):
#     def run(self):
#         print("work")
# t = MyThread()
# t.start()
# t.join() join: 모든 스레드가 작업이 끝날 때까지 메인 스레드가 기다려줌??