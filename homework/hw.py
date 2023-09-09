from requests import get

class Pokemon():
    
    def __init__(self, pokemon):
        self.name = pokemon
        self.weight = None
        self.abilities = []
        self.types = []
        self.sprite = None
        self.evo_chain = []
        self.poke_api_call()
        
    def __repr__(self):
        return f'<Pokemon: {self.name}>'
    
    def poke_api_call(self):
        while True:
            res = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
            if res.ok:
                data = res.json()
                self.name = data['name']
                self.weight = data['weight']
                self.abilities = [ability['ability']['name'] for ability in data['abilities']]
                self.types = [poke_type['type']['name'] for poke_type in data['types']]
                self.sprite = self.get_sprite(data)
                break
            else:
                print(f'Invalid Request, status code {res.status_code}, Please enter valid pokemon')
                self.update_pokemon()
        if not self.evo_chain:
          self.find_evo_chain(data['species']['url'])
            
    def update_pokemon(self):
        self.name = input('Pokemon name: ')
        
    def get_sprite(self, data):
        animated = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
        return animated if animated else data['sprites']['front_default']
        
    def display_info(self):
        print(f'{self.name} Weight: {self.weight}')
        print('Types: ')
        for poke_type in self.types:
            print(poke_type)
        print('Abilities: ')
        for ability in self.abilities:
            print(ability)
        # self.display_img()
        
    def find_evo_chain(self, species_url):
        res = get(species_url)
        if res.ok:
            data = res.json()
            res = get(data['evolution_chain']['url'])
            if res.ok:
                data = res.json()
                self.populate_evo_chain(data['chain'])
                return
        print('Try again')
    
    def populate_evo_chain(self, evo_chain):
        self.evo_chain.append(evo_chain['species']['name'])
        if evo_chain['evolves_to']:
          self.populate_evo_chain(evo_chain['evolves_to'][0])
        else:
            print(self.evo_chain)
    
    def evolve(self):
        for i, pokemon in enumerate(self.evo_chain):
            if pokemon == self.name:
              if len(self.evo_chain) - 1 != i:
                 self.name = self.evo_chain[i + 1]
                 self.poke_api_call()
                 self.display_info()
                 break
              else:
                  print('This is your final form')
    
pokemon = Pokemon('squirtle')
pokemon.evolve()
pokemon.evolve()
pokemon.evolve()









class Move_Tutor:
    def __init__(self, pokemon):
        self.move_list = []
        self.name = pokemon
        
        
    def teach_move(self):
        import re
        if len(self.move_list) <= 4:
            while len(self.move_list) <= 4:
                if n_move in self.move_list:
                    print('Please enter valid input')
                    old_move = input('what move would you like to replace?')
                    self.move_list.pop(old_move)
                    n_move = input('Input new move')
                    self.move_list.append(n_move) 
                    print
            
            
            
                
        #         elif move not in self.move_list:
        #             self.move_list.appent()
        
        
        
        
        
pokemon.teach_move()
        