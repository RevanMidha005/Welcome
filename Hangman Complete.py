def generate_movie():
    
    import random

    movie_set = {'Pathaan', 'Bholaa', 'Bhediya', 'PK',
                 'Dhoom', 'Happy New Year', 'Bang Bang',
                 'Jersey', 'Radhe', 'Dilwale'}
    
    Movie = random.choice(list(movie_set))

    word = ''
    for alpha in Movie:
        if alpha.lower() in 'aeiou':
            word += alpha

        elif alpha.isspace():
            word += ' '

        else:
            word += '_'

    return word, Movie

def guess_movie_name():
    
    import sys
    
    play = 'y'
    
    while play in 'yY':
        Alpha = []
        for i in range(65,91):
            if chr(i).lower() not in 'aeiou':
                Alpha.append(chr(i).lower())

        hidden_movie, actual_movie = generate_movie()
        
        hidden_movie = hidden_movie.lower()
        actual_movie = actual_movie.lower()

        lh_movie = list(hidden_movie)
        la_movie = list(actual_movie)

        body = ['_________','|','|','|','|','|','---------']

        d = {0:'_________',1:'|   |',2:'|   o',3:'| /',4:'|  | |',5:'|',6:'---------'}
        
        print('\n'.join(body))
        print()

        chances = 7

        print(hidden_movie)
        print(f'\nYou have {chances} chances left!\n')
        
        while chances != 0:

            print('You can use these alphabets: "' + ' '.join(Alpha) + '"')
            print()
            
            guess = input('Enter alphabet except vowels: ').lower()
            print()

            if len(guess) == 0 or len(guess) > 1:
                input('Invalid input ... Press ANY key to continue!')
                print()
                continue            

            if guess.isdigit():                
                input('Digits not allowed ... Press ANY key to continue!')
                print()
                continue

            if not guess.isalnum():                
                input('Only non-vowel alphabets are allowed ... Press ANY key to continue!')
                print()
                continue

            if guess in 'aeiou':
                input('Vowels not allowed ... Press ANY key to continue!')
                print()
                continue

            if guess not in Alpha:
                input('You have already used this alphabet.... Press ANY key to continue')
                print()
                continue
            
            flag = False
        
            for i in range(len(la_movie)):
                if guess == la_movie[i]:
                    lh_movie[i] = guess
                    flag = True

            Alpha.remove(guess)
            
            if not flag:
                chances -= 1

                print('That was a wrong guess!\n')

                if chances == 3:
                    d = {0:'_________',1:'|   |',2:'|   o',3:'| / |',4:'|',5:'|',6:'---------'}
                elif chances == 2:
                    d = {0:'_________',1:'|   |',2:'|   o',3:'| / | \\',4:'|',5:'|',6:'---------'}
                elif chances == 1:
                    d = {0:'_________',1:'|   |',2:'|   o',3:'| / | \\',4:'| |',5:'|',6:'---------'}
                elif chances == 0:
                    d = {0:'_________',1:'|   |',2:'|   o',3:'| / | \\',4:'|  | |',5:'|',6:'---------'}
                    
                for i in range(0, min(len(d), 7-chances+1)):
                    body[i]=d[i]
                    print(body[i])

                print('\n'.join(body[i+1:]))
                print()            
                       
                print(f'You have {chances} chances left!\n')
                continue

            hidden_movie = ''.join(lh_movie)

            if actual_movie == hidden_movie:
                print('You Win!\n')
                break
            else:
                print(hidden_movie)
                print('\n'.join(body))
                
        else:
            print('You Lose!\n')

        play = input("Want to play again (y/n): ")
        print()

guess_movie_name() 

        
