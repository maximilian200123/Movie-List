movies = []


def text():
    print("Here are your options:")
    print("1.Add movies to the list.")
    print("2.Show the movies list.")
    print("3.Find movies in the list.")
    print("4.Quit the programme.")


def add_movie():
    print()
    movie_name = input("Please enter the movie name: ").strip().title()
    movie_director = input("Please enter the director of the movie: ").strip().title()
    release_year = input("Please enter the release year of the movie: ")
    dictionary = {
        'name': movie_name,
        'director': movie_director,
        'release year': release_year
    }
    movies.append(dictionary)
    while True:
        option = input("Do you want to keep adding movies? Y/N      ").strip().lower()
        if option == 'y':
            add_movie()
            break
        elif option == 'n':
            print("Going back to the menu...")
            break
        else:
            print("Select from y or n.")
    return


def show_movies():
    print()
    if not movies:
        print("The list is empty!")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}.{movie['name']} by {movie['director']} ({movie['release year']})")
    print()

#This fucntion finds the movie only if you type the movie's whole name correctly
def find_movie():
    print()
    user_name = input("Please enter the title of the movie you want to search: ")
    search_name = user_name.strip().title()
    for index, movie in enumerate(movies, start=1):
        if search_name == movie['name'].strip().title():
            print(f"{index}.{movie['name']} by {movie['director']} ({movie['release year']})")
    print()


user_options = {
    '1': add_movie,
    '2': show_movies,
    '3': find_movie,
}


def menu():
    text()
    user_input = input("Please choose the number of the option: ")

    while user_input != '4':

        if user_input in user_options:
            selected_function = user_options[user_input]
            selected_function()
        else:
            print("Please select a valid option!", "\n")
        text()
        user_input = input("Please choose the number of the option: ")
    if user_input == '4':
        print("Exiting the programme..")


menu()
