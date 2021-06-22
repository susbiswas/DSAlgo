def ramanujan(n):
    found = False
    for a in range (0,n):
        cube_a = a*a*a

        for b in range(a,n):
            cube_b = b*b*b
           
            for c in range (a,n):
                cube_c = c*c*c
                if(cube_c > cube_a + cube_b):
                    break

                for d in range (c, n):
                    cube_d = d*d*d
                    if(cube_c+ cube_d > cube_a + cube_b):
                        break

                    if (cube_a + cube_b == cube_c + cube_d) and (a+b+c+d == n):
                        found = True
                        print(a,b,c,d)    
                        break

    if found == False:
        print("No such tuple found")             
                        
ramanujan(20)   
