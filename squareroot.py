def newtonSqrt(n, base): #Function to return the square root of a number using Newtons method where base is decimal
    approx_root = 0.5 * n #initial approximation
    for i in range(base):
        better_approx = 0.5 * (approx_root + n/approx_root) #compute a better approximation
        approx_root = better_approx
    return better_approx

n = input("Enter a positive number or enter: ")
n = float(n)
print("the square root of (n) is",newtonSqrt(n, 10))

 

 

#https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx=
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
