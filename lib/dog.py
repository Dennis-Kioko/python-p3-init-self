#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

snoopy = Dog("Snoopy")
print(snoopy.name)