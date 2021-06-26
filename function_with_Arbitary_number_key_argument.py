#this function contain Arbitay number of keyword argument 
# uses is like fun(a="abc" ,b="myname")
# output will be a dict {a : "abc" , b : "myname"}
#function need to define with (**kwargs) --NOTE ** and kwargs unlike the normal 
# multi variable (*args)
#26-06-2021

def myfun(**kwargs):
    return kwargs

print(myfun(myname="chandramani" , lastname="shakya"))

'''
OUTPUT:-
{'myname': 'chandramani', 'lastname': 'shakya'}
'''
