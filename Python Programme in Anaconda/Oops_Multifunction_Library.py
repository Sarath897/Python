class multifunction():
    
    def subfields():
            print("sub-firlds in AI are:")
            print("Machine Learning")
            SubfieldsInAI="Machine Learning"
            print("Neural Networks")
            SubfieldsInAI="Neural Networks"  
            print("Vision")
            SubfieldsInAI="Vision"
            print("Robotics")
            SubfieldsInAI="Robotics"
            print("Speech Processing")
            SubfieldsInAI="Speech Processing"
            print("Natural Language Processing")
            SubfieldsInAI="Natural Language Processing"



    def oddEven():
            num=int(input("Enter the Number: "))
            if(num%2==1):
                print(num, "is ODD Number")
            else:
                print(num,"is EVEN Number")

    def __init__(self, gender, age):
            self.age = age
            self.gender = gender

    def eligible_for_marriage(self):
            if self.gender.lower() == 'male':
                return self.age >= 21
            elif self.gender.lower() == 'female':
                return self.age >= 18
            else:
                return elig



            Name = input("Enter your Name: ")
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            Marriage = Marriage(gender, age)
            
            if Marriage.eligible_for_marriage():
                print(Name,"is Eligible ")
            else:
                print(Name,"is Not Eligible ")
   

    def percentage():
            sub1=int(input("subject1="))
            sub2=int(input("subject2="))
            sub3=int(input("subject3="))
            sub4=int(input("subject4="))
            sub5=int(input("subject5="))
            total=sub1+sub2+sub3+sub4+sub5
            print("total:",total)
            print("Percentage",total/5,"%")    


    def triangle():
            Height=int(input("Height:"))
            breadth=int(input("Breadth:"))
            area=float((Height*breadth)/2)
            print("Area formula: (Height*Breadth)/2")
            print("∴ Area =",area)

            h1=int(input(" height1:"))
            h2=int(input(" height2:"))
            b1=int(input(" breadth:"))
            perimeter=h1+h2+b1
            print("∴ Perimeter of triangle =",perimeter)
