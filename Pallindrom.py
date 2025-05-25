from collections import deque
import os


#функція очищення консолі перед наступною ітерацією
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#функція на перевірку списку на паліндроність
def check_palindrom(parametr):
    symbols = {'(':')', '[' : ']', '{':'}', '\\' : '/'}
    while len(parametr) > 1:
        left = parametr[0]
        right = parametr[-1]
        if left in symbols:
            if symbols[left] != right:
                print("Список не паліндромний")
                return
        else:
            if left!= right:
                print("Список не паліндромний")
                return
        #видалення першого і останнього елементу в списку        
        parametr.pop()
        parametr.popleft()
    print("Список паліндромний")
    
def main():
    try:
        while True:
            clear_console() # очищення консолі перед наступною ітерацією
            user_list_input = input("Введіть слово або набір символів для перевірки на паліндромність, або exit для виходу:")
            if user_list_input.lower() == 'exit':
                print("завершення програми")
                break
            d = deque(user_list_input)
            check_palindrom(d)
            input("\nНатисніть Enter, щоб продовжити...")
     
    except KeyboardInterrupt:
        print("The End")
        
if __name__ == "__main__":
    main()


            
          
           
            