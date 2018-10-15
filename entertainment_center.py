import media
import fresh_tomatoes


# Creating Objects from Movie class
movie1 = media.Movie("Saw", "A psychopath who tortures bad persons",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcT2L"
                     "c3VR5L0ajhixAgsm9xD6qqLA6C48k_kZI3TmNcpURwFsU9u",
                     "https://www.youtube.com/watch?v=HKPy5RWuqNA")

movie2 = media.Movie("Avatar", "A marine on an alien planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmv"
                     "rE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

movie3 = media.Movie("Inception", "A thief, who steals corporate "
                     "secrets through the use of dream-sharingtechnology",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vf"
                     "JCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                     "https://www.youtube.com/watch?v=d3A3-zSOBT4")

# Storing objects in list data structure
movies = [movie1, movie2, movie3]

# Calling open_movies_page() function
fresh_tomatoes.open_movies_page(movies)
