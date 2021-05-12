import cvrt_module
h=input("your height(feet)?")
height=float(h)
result=cvrt_module.feet_to_cm(height)
print("your height convert %4.1f cm"%(result))
