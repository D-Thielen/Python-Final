#Import the necessary libraries
import pandas as pd  
from tabulate import tabulate
from plotly.graph_objs import Bar, Layout
from plotly import offline


#Set a variable to read the data from a CSV file
df = pd.read_csv('final/pokemon.csv')

#set the index to match the number of the Pokemon
df = df.set_index('#')

#Set the option so that all rows of data are shown
pd.set_option('display.max_rows', None)  

#Set variables to call the information for the types of Pokemon
bug = df[(df['Type 1'] == 'Bug') | (df['Type 2'] == 'Bug')]
dark = df[(df['Type 1'] == 'Dark') | (df['Type 2'] == 'Dark')]
dragon = df[(df['Type 1'] == 'Dragon') | (df['Type 2'] == 'Dragon')]
electric = df[(df['Type 1'] == 'Electric') | (df['Type 2'] == 'Electric')]
fairy = df[(df['Type 1'] == 'Fairy') | (df['Type 2'] == 'Fairy')]
fighting = df[(df['Type 1'] == 'Fighting') | (df['Type 2'] == 'Fighting')]
fire = df[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Fire')]
flying = df[(df['Type 1'] == 'Flying') | (df['Type 2'] == 'Flying')]
ghost = df[(df['Type 1'] == 'Ghost') | (df['Type 2'] == 'Ghost')]
grass = df[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Grass')]
ground = df[(df['Type 1'] == 'Ground') | (df['Type 2'] == 'Ground')]
ice = df[(df['Type 1'] == 'Ice') | (df['Type 2'] == 'Ice')]
normal = df[(df['Type 1'] == 'Normal') | (df['Type 2'] == 'Normal')]
poison = df[(df['Type 1'] == 'Poison') | (df['Type 2'] == 'Poison')]
psychic = df[(df['Type 1'] == 'Psychic') | (df['Type 2'] == 'Psychic')]
rock = df[(df['Type 1'] == 'Rock') | (df['Type 2'] == 'Rock')]
steel = df[(df['Type 1'] == 'Steel') | (df['Type 2'] == 'Steel')]
water = df[(df['Type 1'] == 'Water') | (df['Type 2'] == 'Water')]

#Create a list of all the types of Pokemon
all_types = ['1. Bug', '2. Dark' , '3. Dragon' , '4. Electric' , '5. Fairy', '6. Fighting', '7. Fire', '8. Flying', '9. Ghost', '10. Grass', 
'11. Ground', '12. Ice', '13. Normal', '14. Poison', '15. Psychic', '16. Rock', '17. Steel', '18. Water']


def main():
    """Function that ist the main screen of the program"""
    while True:

        print("\nWelcome to the Pokemon database! Please select an option from below:\n")
        print("\t1. Lookup stats for a specific Pokemon.\n")
        print("\t2. Get a list of all Pokemon of the same type with a total.\n")
        print("\t3. Graph of the totals of all the types.\n")
        print("\t4. Exit the program.\n")
    
        choice = input()
        if choice == '4':
            break

        elif choice == '1':
            get_pokemon()
            continue

        elif choice == '2':
            get_type_list()
            continue

        elif choice == '3':
            get_type_graph()
            continue
        
        else:
            print("That is not a valid entry.\n")



def get_pokemon():
    """This function takes the user input and returns the stats for the users choice. """

    print("\nLet's find that Pokemon for you!\n")
    
    while True:

        #Get input from the user.
        choice = input("Enter 'quit' to finish your search.\nPlease enter the name of the Pokemon: \n")

        #Set a variable to store the list of names in the dataframe.
        names = df['Name'].tolist()

        #Set a variable to store the ntaching choice of the user from the dataframe.
        pokemon = df[df['Name'] == choice.title()]

        if choice == 'quit':
            break

        elif choice.title() in names:
            #Print the correct information and formatted in a way that is a bit nicer than just the 
            #basic dataframe output.
            print(tabulate(pokemon, headers= 'keys', tablefmt='fancy_grid'))
            continue

        else:
            print("That is not a valid entry.\n")


def get_type_list():
    """This function returns a list of all the pokemon of a chosen type with the totals as well."""

    print("\nLet's find that list for you!\n")
    
    while True:
        
        #Neatly print the list of types.
        for type in all_types:
            print(type)

        #Get input from the user.  
        choice = input("\nEnter 'quit' to finish your search.\nPlease choose the type of the Pokemon: \n")
        
        #For each elif statement, print the list of all the pokemon as well as the total of the chosen type.
        if choice == 'quit':
            break

        elif choice.lower() == 'bug':
            print(tabulate(bug, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {bug.shape[0]} Bug type Pokemon\n")
            continue

        elif choice.lower() == 'dark':
            print(tabulate(dark, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {dark.shape[0]} Dark type Pokemon\n")
            continue

        elif choice.lower() == 'dragon':
            print(tabulate(dragon, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {dragon.shape[0]} Dragon type Pokemon\n")
            continue

        elif choice.lower() == 'electric':
            print(tabulate(electric, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {electric.shape[0]} Electric type Pokemon\n")
            continue

        elif choice.lower() == 'fairy':
            print(tabulate(fairy, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {fairy.shape[0]} Fairy type Pokemon\n")
            continue

        elif choice.lower() == 'fighting':
            print(tabulate(fighting, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {fighting.shape[0]} Fighting type Pokemon\n")
            continue

        elif choice.lower() == 'fire':
            print(tabulate(fire, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {fire.shape[0]} Fire type Pokemon\n")
            continue

        elif choice.lower() == 'flying':
            print(tabulate(flying, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {flying.shape[0]} Flying type Pokemon\n")
            continue

        elif choice.lower() == 'ghost':
            print(tabulate(ghost, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {ghost.shape[0]} Ghost type Pokemon\n")
            continue

        elif choice.lower() == 'grass':
            print(tabulate(grass, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {grass.shape[0]} Grass type Pokemon\n")
            continue

        elif choice.lower() == 'ground':
            print(tabulate(ground, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {ground.shape[0]} Ground type Pokemon\n")
            continue

        elif choice.lower() == 'ice':
            print(tabulate(ice, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {ice.shape[0]} Ice type Pokemon\n")
            continue

        elif choice.lower() == 'normal':
            print(tabulate(normal, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {normal.shape[0]} Normal type Pokemon\n")
            continue

        elif choice.lower() == 'poison':
            print(tabulate(poison, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {poison.shape[0]} Poison type Pokemon\n")
            continue

        elif choice.lower() == 'psychic':
            print(tabulate(psychic, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {psychic.shape[0]} Psychic type Pokemon\n")
            continue

        elif choice.lower() == 'rock':
            print(tabulate(rock, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {rock.shape[0]} Rock type Pokemon\n")
            continue

        elif choice.lower() == 'steel':
            print(tabulate(steel, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {steel.shape[0]} Steel type Pokemon\n")
            continue

        elif choice.lower() == 'water':
            print(tabulate(water, headers= 'keys', tablefmt='fancy_grid'))
            print(f"\nThere is a total of {water.shape[0]} Water type Pokemon\n")
            continue
        else:
            print("That is not a valid entry.\n")


def get_type_graph():
    """This function retuns a simple graph that shows the totals of all the different types."""

    #Create a list of all the totals.
    totals = []

    #Add each type total to the list.
    totals.append(bug.shape[0])
    totals.append(dark.shape[0])
    totals.append(dragon.shape[0])
    totals.append(electric.shape[0])
    totals.append(fairy.shape[0])
    totals.append(fighting.shape[0])
    totals.append(fire.shape[0])
    totals.append(flying.shape[0])
    totals.append(ghost.shape[0])
    totals.append(grass.shape[0])
    totals.append(ground.shape[0])
    totals.append(ice.shape[0])
    totals.append(normal.shape[0])
    totals.append(poison.shape[0])
    totals.append(psychic.shape[0])
    totals.append(rock.shape[0])
    totals.append(steel.shape[0])
    totals.append(water.shape[0])

    #Set the parameters for the graph.
    data = [Bar(x=all_types, y=totals)]
    x_axis_config = {'title': 'Types', 'dtick': 1}
    y_axis_config = {'title': 'Total of Each Type'}
    my_layout = Layout(title='Totals of Each Pokemon Type',
            xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='pokemon_totals.html')

    


main()
