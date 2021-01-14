from ipywidgets import interact, interactive, fixed
import ipywidets as widgets

def func(x):
	return x**2

interact (func,x=True)

def funcText(y):
	return x**2

@interact(x=True, y=1.0)
def funcPoint(x,y):
	return x**2
