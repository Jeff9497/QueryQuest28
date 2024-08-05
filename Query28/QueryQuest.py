from googlesearch import search
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def google_search():
    # Default settings
    default_language = 'en'
    default_num_results = 5
    default_region = 'ke'
    
    print(f"{Fore.YELLOW + Style.BRIGHT}Welcome to QueryQuest28, your next magical search engine!")
    
    while True:
        # Ask the user if they want to use the default settings
        use_default = input(f"{Fore.BLUE + Style.BRIGHT}Do you want to run on default settings? (yes/no): ").strip().lower()
        
        if use_default == 'yes':
            query = input("Enter what you want to search for: ")
            results = search(query, num_results=default_num_results, lang=default_language, region=default_region, advanced=True)
        else:
            query = input("Enter what you want to search for: ")
            num_results = int(input("Enter the number of results you want: "))
            language = input("Enter the language code (e.g., 'en' for English, 'fr' for French): ")
            region = input("Enter the region code (e.g., 'us' for United States, 'ke' for Kenya): ")
            
            results = search(query, num_results=num_results, lang=language, region=region, advanced=True)
        
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result.title}")
            print(f"   {result.url}")
            print(f"   {result.description}\n")
        
        # Ask if the user wants to search again
        search_again = input(f"{Fore.BLUE + Style.BRIGHT}Do you want to search again? (yes/no): ").strip().lower()
        if search_again != 'yes':
            break

if __name__ == "__main__":
    google_search()
