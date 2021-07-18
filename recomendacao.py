avaliacoes = {'Lucas': 
		{'Rock II': 2.5, 
		 'Avatar': 3.5,
		 'Star Wars II': 3.0, 
		 'Exterminador do Futuro': 3.5, 
		 'O Todo Poderoso': 2.5, 
		 'Star Wars': 3.0},
	 
	  'Marlon': 
		{'Rock II': 3.0, 
		 'Avatar': 2.5, 
		 'Star Wars II': 1.5, 
		 'Exterminador do Futuro': 5.0, 
		 'Star Wars': 3.0, 
		 'O Todo Poderoso': 3.5}, 

	  'Emanoel': 
                {'Rock II': 2.5, 
		 'Avatar': 3.0,
                 'Star Wars II': 1.5,
		 'Exterminador do Futuro': 3.5,
                 'O Todo Poderoso': 3.5,
		 'Star Wars': 4.0},
			 
	  'Gustavo': 
		{'Avatar': 3.5, 
		 'Star Wars II': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'O Todo Poderoso': 2.5},
				 
	  'Adriano': 
		{'Rock II': 3.0, 
		 'Avatar': 4.0, 
		 'Star Wars II': 3.0, 
		 'Exterminador do Futuro': 3.0, 
		 'Star Wars': 3.0,
		 'O Todo Poderoso': 3.5}, 

	  'Otavio': 
	     {'Rock II': 3.0, 
	      'Avatar': 4.0,
              'Star Wars':3.0,
	      'Star Wars II': 3.0, 
	      'Exterminador do Futuro': 3.0, 
	      'O Todo Poderoso': 3.5},
			  
	  'Henrique': 
	    {'Avatar':4.5,
             'O Todo Poderoso':1.0,
	     'Exterminador do Futuro':4.0}
}

from math import sqrt

def euclidiana (Pessoa1,Pessoa2):
    similaridade={}
    for item in avaliacoes[Pessoa1]:
        if item in avaliacoes[Pessoa2]:similaridade[item]=1

        if len(similaridade)==0:return 0
        
        soma = sum([pow(avaliacoes[Pessoa1][item] - avaliacoes[Pessoa2][item],2)
                    for item in avaliacoes[Pessoa1]if item in avaliacoes[Pessoa2]])
        return 1/(1+sqrt (soma))


def ObjetosSimilares(Pessoas):
    similaridades = [( euclidiana(Pessoas,outro),outro)
                    for outro in avaliacoes if outro != Pessoas]
    similaridades.sort()
    similaridades.reverse()
    return similaridades
                
