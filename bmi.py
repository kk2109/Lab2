def calculate_bmi(height,weight):
    print("Height= " + str(height))
    print("Weight= " + str(weight))

    bmi= weight / (height*height)
    print("The Bmi is :" + str(bmi))

    if bmi <18.5:
        print("Under Weight")
        return_value=-1

    elif bmi>=18.5 and bmi<= 25.0:
        print("Normal Weight")
        return_value=0
    else:
        print("Over weight")
        return_value=1
    
    return (return_value)

    return(return_value)


#calculate_bmi(weight=57,height=1.73)