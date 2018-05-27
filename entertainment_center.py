#!/usr/bin/python
# -*- coding: utf-8 -*-

import fresh_tomatoes
import media

# Create multiple instances of movie class

toy_story = media.Movie('Toy Story',
                        'The story of a boy who loved his toys',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg'
                        , 'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     'The story of a marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg'
                     , 'https://www.youtube.com/watch?v=d1_JBMrrYw8')

sultan = media.Movie('Sultan',
                     'The story of a wrestler who suffers from a bruised ego.'
                     ,
                     'https://upload.wikimedia.org/wikipedia/en/1/1f/Sultan_film_poster.jpg'
                     , 'https://www.youtube.com/watch?v=wPxqcq6Byq0')

finding_nemo = media.Movie('Finding Nemo',
                           'The story of a clownfish who searches for his son Nemo'
                           ,
                           'https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg'
                           ,
                           'https://www.youtube.com/watch?v=wZdpNglLbt8'
                           )

dangal = media.Movie('Dangal',
                     'The story of a wrestler who trains his daughters to follow his footsteps'
                     ,
                     'https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg'
                     , 'https://www.youtube.com/watch?v=x_7YlGv9u1g')

raees = media.Movie('Raees', 'The story of a criminal',
                    'https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg'
                    , 'https://www.youtube.com/watch?v=8iv3ksZs0hk')

# Create a list of instances of class

movies = [
    toy_story,
    avatar,
    sultan,
    finding_nemo,
    dangal,
    raees,
    ]

# pass movies list to open_movies_page method

fresh_tomatoes.open_movies_page(movies)


            