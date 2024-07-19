from nada_dsl import *

def nada_main():
    # Reference to the first program
    def first_program():
        party1 = Party(name="Party1")
        
        my_int1 = SecretInteger(Input(name="my_int1", party=party1))
        my_int2 = SecretInteger(Input(name="my_int2", party=party1))
        
        new_int = my_int1 + my_int2
        
        return new_int, party1

    # Getting the result of the first program
    new_int, party1 = first_program()
    
    # Additional operation on the result of new_int
    additional_value = SecretInteger(Input(name="additional_value", party=party1))
    final_result = new_int * additional_value
    
    return [Output(final_result, "final_output", party1)]
