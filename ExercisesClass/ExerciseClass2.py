
# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.


age_of_user = int(input('How old are you?'))
age_raiting = str(input('What is the rating of the movie?'))

if age_raiting == '18':
    if age_of_user >= 18:
        print('You can watch the film')
    else:
        print('Sorry you need to be older')
elif age_raiting == '15':
    if age_of_user >= 15:
        print('You can watch the film')
    else:
        print('sorry you need to be older')
elif age_raiting == '12':
    if age_of_user >= 12:
        print('You can watch the film')
    else:
        print('Sorry you need to be older')
elif age_raiting == 'pg':
    print('You can watch it, but some scenes may be unsuitable for young children')
elif age_raiting == 'universal':
    print('You can watch the film')