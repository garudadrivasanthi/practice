'''
Hybrid inheritance'''

class Grand_father:
    def grand_father_method():
        return "This is Grand father method"
class Father(Grand_father):
    def father_method():
        return "This is father method"
class Mother:
    def mother_method():
        return "This is mother method"
class child(Father,Mother,Grand_father):
    def child():
        return "I have properties of all"
grand_father_obj=Grand_father
father_obj=Father
mother_obj=Mother
child_obj=child
print(grand_father_obj.grand_father_method())
print(father_obj.grand_father_method())   
print(father_obj.father_method())
print(child_obj.grand_father_method())
print(child_obj.mother_method())
print(child_obj.father_method())