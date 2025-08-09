

1. Why **if __name__=='__main__':** is used in some python files?<br>
   The if __name__ == '__main__': construct in Python is used to define a block of code that will only be executed when the script is run directly, and not when it is imported as a module into another script.<br>
   Consider this below python code:<br>
   <img width="358" height="452" alt="image" src="https://github.com/user-attachments/assets/5a519ccc-1f78-4e0b-9421-068434324da5" /><br>
   As soon as its imported and run, it calls and print the methods which should have been called only for stand-alone run:<br>
   <img width="557" height="295" alt="image" src="https://github.com/user-attachments/assets/bf6303a0-7057-4528-870b-8bca2b57c1c7" /><br>
   

