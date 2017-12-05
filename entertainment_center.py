import fresh_tomatoes
import media

# All movie data is placed as (title,story,poster,trailer)

# Movie 1/6
jl_cote = media.Movie("Justice League: Crisis on Two Earths",
                      "In an alternate universe, an heroic"
                      " Lex Luthor battles to save his planet"
                      " from an evil variation of the Justice"
                      " League! Now, to save his earth, Luthor"
                      " enlists the Justice League from his"
                      " universe's Crime Syndicate, a gang of"
                      " villains with superpowers evenly matched"
                      " with those of the Justice League.",
                      "https://images-na.ssl-images-amazon.com/"
                      "images/M/MV5BMzg0ODZjNjUtNmVhZi00NTYxLWE"
                      "xNWMtMWI3MDFiMjhiNjc2L2ltYWdlL2ltYWdlXk"
                      "EyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_"
                      "CR0,0,678,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=FNlYtU_x-dI")

# Movie 2/6
jl_gam = media.Movie("Justice League: Gods and Monsters",
                     "This thrilling animated feature explores a"
                     " newly conceived reality in the DC animated"
                     " universe in which Justice League members"
                     " Superman, Batman, Wonder Woman and others"
                     " exist as much darker versions of the superheroes"
                     " that people think they know.",
                     "https://images-na.ssl-images-amazon.com/images/M"
                     "/MV5BNzljNmZiNTktMTU4Ni00MTE2LWFmOTctYzY1NWJlY2"
                     "ZiZjA3XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_"
                     "CR0,0,666,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=yxL1Iw73azg")

# Movie 3/6
jl_tfp = media.Movie("Justice League: The Flashpoint Paradox",
                     "The Flash traverses time to right a violent,"
                     " decades-past crime against his mother, but"
                     " the ripples of his good intentions prove"
                     " disastrous, as a fractured, alternate reality"
                     " now exists in place of the familiar one.",
                     "https://images-na.ssl-images-amazon.com/images/"
                     "M/MV5BMTgwNTljYzgtOTU3ZC00ZjhhLTk0YzItY2RiMWU0M"
                     "GZlNzFjL2ltYWdlXkEyXkFqcGdeQXVyNDQ2MTMzODA@._V1"
                     "_SY1000_CR0,0,692,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=Q3tochTgPVc")

# Movie 4/6
jl_d = media.Movie("Justice League: Doom",
                   "This apocalyptic tale details the nefarious plot"
                   " of villain Vandal Savage, who discovers Batman's"
                   " contingency plan to defeat the Justice League"
                   " should any of them go rogue. Now, backed by his own"
                   " army of supervillains, Savage sets out to take down"
                   " the Justice League one hero at a time!",
                   "https://images-na.ssl-images-amazon.com/images/M/"
                   "MV5BNjgyODU5NDctYzY1Yy00YmQxLTlmMmYtM2ZhMG"
                   "MwZTFlOTE4XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_.jpg",
                   "https://www.youtube.com/watch?v=o3_bGJNxKVE")

# Movie 5/6
b_utrh = media.Movie("Batman: Under the Red Hood",
                     "Batman faces his ultimate challenge as the"
                     " mysterious Red Hood takes Gotham City by firestorm.",
                     "https://images-na.ssl-images-amazon.com/images/M/"
                     "MV5BYTdlODI0YTYtNjk5ZS00YzZjLTllZjktYmYzNWM4NmI5MmM"
                     "xXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,666,"
                     "1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=YLymYj2Thfc")

# Movie 6/6
b_gk = media.Movie("Batman: Gotham Knight",
                   "Six tales reveal Bruce Wayne's earliest adventures as"
                   " Batman, as he travels the globe to stop the villainous"
                   " Scarecrow, Killer Croc and Deadshot.",
                   "https://images-na.ssl-images-amazon.com/images/M/"
                   "MV5BM2I0YTFjOTUtMWYzNC00ZTgyLTk2NWEtMmE3N2VlYjEwN2JlX"
                   "kEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,666,1000"
                   "_AL_.jpg",
                   "https://www.youtube.com/watch?v=0beX8b4zX5E")

# List movies in order from top to bottom
movies = [jl_cote, jl_gam, jl_tfp, jl_d, b_utrh, b_gk]
fresh_tomatoes.open_movies_page(movies)
