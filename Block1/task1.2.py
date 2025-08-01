class Codec():

    '''

    '''

    def encode(self, list_of_commands):
        # Each command is encoded as: '#' + command  ex. #Push#Box,box#Push#Overtake
        encoded_string = ''.join(f"#{command}" for command in list_of_commands)
        return encoded_string
    
    def decode(self, encoded_string):
        original_list = encoded_string.split('#')
        return original_list[1:]  # as first element will always be '' 
    
    def __str__(self):
        pass
    

coach_commands = Codec()


list_of_commands = ["Push","Box,box","Push","Overtake"]
print(f'original commands: {list_of_commands}', "\n")

encoded_str = coach_commands.encode(list_of_commands)
print(f'encoded string : {encoded_str}', "\n")

decoded_commands = coach_commands.decode(encoded_str)
print(f'decoded commands: {decoded_commands}', "\n")

# checker 
if (decoded_commands == list_of_commands):
    print ("succesfully works")


print("---"*30)
# advanced testing case 
list_of_commands2 = ["  yalla", "", "Box, box ", "Push!!!", "3aash", "overtake", "  "]
print(f'original commands: {list_of_commands2}', "\n")

encoded_str2 = coach_commands.encode(list_of_commands2)
print(f'encoded string :{encoded_str2}', "\n")

decoded_commands2 = coach_commands.decode(encoded_str2)
print(f'decoded commands: {decoded_commands2}', "\n")


if (decoded_commands2 == list_of_commands2):
    print ("succesfully works")


'''
note: 
it fails only if command have # 
solution:
- can use more complex delimiter ex. #$$# imperically there's no command will contain this sequence 
- can use length of command with the delimiter
'''