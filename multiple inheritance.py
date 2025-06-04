'''
multiple inheritance
'''
class father:
    def father_method():
        return "This is father method"
class mother:
    def mother_method():
        return "This is mother method"
class child(father,mother):
    def child_method():
        return "I have properties of mother and father"
    
father_obj=father
mother_obj=mother
child_obj=child
print(father_obj.father_method())
print(mother_obj.mother_method())
print(child_obj.father_method())
print(child_obj.mother_method())
print(child_obj.child_method())