# allows access to media and fresh_tomatoes files
import fresh_tomatoes
import media

# content for movie class and fresh_tomatoes open movies page
oceans_eleven = media.Movie("Ocean's Eleven",
                            "Danny Ocean gathers a group of friends to rob a bank.",
                            "https://thedinglehopper.files.wordpress.com/2014/08/oe01.jpeg",
                            "https://www.youtube.com/watch?v=imm6OR605UI",)


out_of_time = media.Movie("Out of Time",
                          "A Florida police chief must solve a vicious double homicide before he himself falls under suspicion.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/3/3a/Out_of_timeposter.jpg/220px-Out_of_timeposter.jpg",
                          "https://www.youtube.com/watch?v=I3GeAu_b05I",)

oceans_twelve = media.Movie("Ocean's Twelve",
                            "Danny Ocean (George Clooney) and his crew of thieves have big problems. ",
                            "https://www.imfdb.org/images/d/d9/O12-dvd.jpg",
                            "https://www.youtube.com/watch?v=k5CZa3X4yF4",)

deja_vu = media.Movie("Deva Vu",
                      "The team of top-secret program brings ATF agent Doug Carlin (Denzel Washington) into its midst to capture the terrorist (Jim Caviezel) responsible for a ferry bombing that left hundreds dead.",
                      "https://images-na.ssl-images-amazon.com/images/I/51IJG6YR1-L.jpg",
                      "https://www.youtube.com/watch?v=uxdS8TP37I4",)

split = media.Movie("Split",
                    "Three girls are kidnapped by a man with a diagnosed 23 distinct personalities",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BZGM5NzI4YWEtNzlkYS00NWM1LTg4ZjctMDQ5ZmNlYTY0NjNmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=84TouqfIsiI",)

blow = media.Movie("Blow",
                   "The story of George Jung, the man who established the American cocaine market",
                   "https://resizing.flixster.com/T-gbdXVuwxz-C-wR6RiZ7Z0Z2x4=/800x1200/v1.bTsxMTE2NzkxNztqOzE3NDUxOzIwNDg7ODAwOzEyMDA",
                   "https://www.youtube.com/watch?v=scWkP1GdnuU",)

# individual movie data order for movies array
movies = [oceans_eleven, out_of_time, oceans_twelve, deja_vu, split, blow]

# adds content to fresh tomatos movies array and generate html file
fresh_tomatoes.open_movies_page(movies)
