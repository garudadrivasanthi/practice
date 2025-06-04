{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1688159a-bbb2-43b3-9dfc-d51d4b21a064",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is father method\n",
      "this is child method\n",
      "this is father method\n"
     ]
    }
   ],
   "source": [
    "class father:\n",
    "    def father_method():\n",
    "        return \"this is father method\"\n",
    "class child(father):\n",
    "    def child_method():\n",
    "        return \"this is child method\"\n",
    "parent_object=father\n",
    "child_object=child\n",
    "print(parent_object.father_method())\n",
    "print(child_object.child_method())\n",
    "print(child_object.father_method())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "611df723-e56c-48d7-89e0-c82752c83d40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is father method\n",
      "this is mother method\n",
      "I have properties of mother and father\n",
      "this is father method\n",
      "this is mother method\n"
     ]
    }
   ],
   "source": [
    "class father:\n",
    "    def father_method():\n",
    "        return \"this is father method\"\n",
    "class mother:\n",
    "    def mother_method():\n",
    "        return \"this is mother method\"\n",
    "class child(father,mother):\n",
    "    def child_method():\n",
    "        return\"I have properties of mother and father\"\n",
    "father_obj=father\n",
    "mother_obj=mother\n",
    "child_obj=child\n",
    "print(father_obj.father_method())\n",
    "print(mother_obj.mother_method())\n",
    "print(child_obj.child_method())\n",
    "print(child_obj.father_method())\n",
    "print(child_obj.mother_method())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "825251d4-5af3-474e-b13e-6cf2a5752fc1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is grandfather method\n",
      "this is father method\n",
      "this is child method\n",
      "this is grandfather method\n",
      "this is father method\n"
     ]
    }
   ],
   "source": [
    "class grandfather:\n",
    "    def grandfather_method():\n",
    "        return \"this is grandfather method\"\n",
    "class father(grandfather):\n",
    "    def father_method():\n",
    "        return \"this is father method\"\n",
    "class child(father):\n",
    "    def child_method():\n",
    "        return \"this is child method\"\n",
    "grandfather_obj=grandfather\n",
    "father_obj=father\n",
    "child_obj=child\n",
    "print(grandfather_obj.grandfather_method())\n",
    "print(father_obj.father_method())\n",
    "print(child_obj.child_method())\n",
    "print(child_obj.grandfather_method())\n",
    "print(child_obj.father_method())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7835fa5-a8ea-4820-8203-07a6ed707cdf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
