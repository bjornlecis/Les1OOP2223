
# Turns a dictionary into a class
class Dict2Class(object):

    def __init__(self, my_dict):

        for key in my_dict:
            setattr(self, key, my_dict[key])
    def toon_info(self):
        print("Toont de info",self.Name)

# Driver Code
if __name__ == "__main__":

    # Creating the dictionary
    my_dict = {"Name": "Geeks",
               "Rank": "1223",
               "Subject": "Python"}

    result = Dict2Class(my_dict)

    # printing the result
    print("After Converting Dictionary to Class : ")
    print(result.Name, result.Rank, result.Subject)
    print(type(result))
    print(result.Rank)
    result.toon_info()


