print(*(lambda k:(-1,)if(k<3)else((k*k//2,k*k//2+1)if(k%2)else((k*k//8*2,(k*k//8+1)*2)if(k//2)%2 else(3*(k//4),5*(k//4)))))(int(input())))
