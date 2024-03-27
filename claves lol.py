import random
def gen(aaa):

    waos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contra = "".join(random.choice(waos) for i in range(aaa))
    print("La clave generada es:", contra)
    return contra
aa= int(input("Longitud clave: "))
test= gen(aa)