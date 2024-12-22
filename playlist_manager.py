def display_menu():
    print("\n=== Playlist Manager ===")
    print("1. View Playlist")
    print("2. Add Song")
    print("3. Remove Song")
    print("4. Sort Playlist")
    print("5. Search for a Song")
    print("6. Exit")


def view_playlist(playlist):
    if not playlist:
        print("\nYour playlist is empty.")
    else:
        print("\nYour Playlist:")
        for i, song in enumerate(playlist, start=1):
            print(f"{i}. {song['name']} by {song['artist']}")


def add_song(playlist):
    song_name = input("Enter the song name: ")
    artist_name = input("Enter the artist name: ")
    playlist.append({"name": song_name, "artist": artist_name})
    print(f"Added '{song_name}' by {artist_name} to the playlist.")


def remove_song(playlist):
    if not playlist:
        print("\nYour playlist is empty.")
        return

    view_playlist(playlist)
    try:
        song_number = int(input("Enter the number of the song to remove: "))
        if 1 <= song_number <= len(playlist):
            removed_song = playlist.pop(song_number - 1)
            print(f"Removed '{removed_song['name']}' by {removed_song['artist']} from the playlist.")
        else:
            print("Invalid song number.")
    except ValueError:
        print("Please enter a valid number.")


def sort_playlist(playlist):
    if not playlist:
        print("\nYour playlist is empty.")
        return

    print("\nSort by:")
    print("1. Song Name")
    print("2. Artist Name")
    choice = input("Choose an option: ")

    if choice == "1":
        playlist.sort(key=lambda song: song['name'].lower())
        print("Playlist sorted by song name.")
    elif choice == "2":
        playlist.sort(key=lambda song: song['artist'].lower())
        print("Playlist sorted by artist name.")
    else:
        print("Invalid choice. Returning to the main menu.")


def search_song(playlist):
    if not playlist:
        print("\nYour playlist is empty.")
        return

    query = input("Enter the song name or artist to search: ").lower()
    results = [song for song in playlist if query in song['name'].lower() or query in song['artist'].lower()]

    if results:
        print("\nSearch Results:")
        for i, song in enumerate(results, start=1):
            print(f"{i}. {song['name']} by {song['artist']}")
    else:
        print("No matching songs found.")


def main():
    playlist = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_playlist(playlist)
        elif choice == "2":
            add_song(playlist)
        elif choice == "3":
            remove_song(playlist)
        elif choice == "4":
            sort_playlist(playlist)
        elif choice == "5":
            search_song(playlist)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
