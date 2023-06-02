import Holiday
import Pokemon
import random
import sys

def main():
    ran_num = random.randrange(1, 146)

    try:
        holiday = Holiday.Holiday(ran_num)
        holiday.get()

        pokemon = Pokemon.Pokemon(ran_num)
        pokemon.get()
        
        print(f"If your favorite holiday is {holiday}, then your spirit Pokemon is {pokemon}!")
    
    except:
        print("Error", sys.exc_info()[0], "occured...")
        
main()