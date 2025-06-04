class father:
    def father_method():
        return "this is father method"
class child(father):
    def child_method():
        return "this is child method"
parent_object=father
child_object=child
print(parent_object.father_method())
print(child_object.child_method())
print(child_object.father_method())
'''
'''
class father:
    def father_method():
        return "this is father method"
class mother:
    def mother_method():
        return "this is mother method"
class child(father,mother):
    def child_method():
        return"I have properties of mother and father"
father_obj=father
mother_obj=mother
child_obj=child
print(father_obj.father_method())
print(mother_obj.mother_method())
print(child_obj.child_method())
print(child_obj.father_method())
print(child_obj.mother_method())
'''
'''
class grandfather:
    def grandfather_method():
        return "this is grandfather method"
class father(grandfather):
    def father_method():
        return "this is father method"
class child(father):
    def child_method():
        return "this is child method"
grandfather_obj=grandfather
father_obj=father
child_obj=child
print(grandfather_obj.grandfather_method())
print(father_obj.father_method())
print(child_obj.child_method())
print(child_obj.grandfather_method())
print(child_obj.father_method())
'''
'''
class Animal:
    def speak():
        return "Animal is speaking"
class bird():
    def speak():
        return "bird is speaking"
animal_object=Animal
bird_object=bird
print(animal_object.speak())
'''
'''
class grandfather:
    def grandfather_method():
        return "this is grandfather method"
class mother():
    def mother_method():
        return "this is mother method"
class father(grandfather):
    def father_method():
        return "this is father method"
class child(father,mother):
    def child_method():
        return "this is child method"
grandfather_obj=grandfather
father_obj=father
child_obj=child
print(grandfather_obj.grandfather_method())
print(mother_obj.mother_method())
print(father_obj.father_method())
print(father_obj.grandfather_method())
print(child_obj.child_method())
print(child_obj.grandfather_method())
print(child_obj.father_method())
print(child_obj.mother_method())