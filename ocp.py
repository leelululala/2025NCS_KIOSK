import time

def time_measure_decorate(f):
    def wrapper(*args):
        s=time.time()
        r=f(*args)
        e=time.time()
        print(f"time: {e-s}")
        return r
    return wrapper

@time_measure_decorate
def one_to_n_loop(n):
    result=0
    for i in range(1,n+1):
        result=result+i
    return result

#@time_measure_decorate
def one_to_n_math(n):
    r=n*(n+1)//2
    return r

number=int(input("input number: "))

func=time_measure_decorate(one_to_n_math)
print(func(number))

print(one_to_n_loop(number))
#print(one_to_n_math(number))

"""
데코레이트를 붙이면 원래 함수 코드는 손 안대도 됨.
기존 코드를 수정하지 않고 확장 가능.

"""