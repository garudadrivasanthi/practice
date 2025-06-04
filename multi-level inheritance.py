'''
multi-level inheritance'''

class Grand_father:
    def grand_father_method():
        return "This is the Grand Father Method"
class Father(Grand_father):
    def father_method():
        return "This is the Father method"
class child(Grand_father,Father):
    def child_method():
        return "I have properties of both Grand father and father"
grand_father_obj=Grand_father
father_obj=Father
child_obj=child
print(child_obj.grand_father_method())
print(child_obj.father_method())
print(child_obj.child_method())