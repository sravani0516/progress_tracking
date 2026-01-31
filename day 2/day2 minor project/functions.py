def profile_generator(**kwargs):
    lst=[]
    for key,value in kwargs.items():
        lst.append(f"{key}:{value}")
    return lst


def total(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
