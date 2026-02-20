# from scrt.core.menu import show_menu

# def main():
#     print("Brainrot Production is alive 🔥")
#     show_menu()

# if __name__ == "__main__":
#     main()




from scrt.database.db import create_tables, add_resident, get_all_residents

def main():
    create_tables()
    print(get_all_residents())

if __name__ == "__main__":
    main()