
#TP 7

def bubble_sort(input_list):
    n = len(input_list)

    for i in range(n):
        # Flag to track if any swap is made in this pass
        swap_made = False

        # Compare elements and swap them if they are in the wrong order
        for j in range( n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j] 
                swap_made = True

        # If no swap is made in this pass, the list is already sorted
        if not swap_made:
            break


numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)

print("Lista en orden ascendente:")
print(numbers)

#Ejericio 2
 
def selection_sort(word_list):
    n = len(word_list)

    for i in range(n):
        # Encontrar el índice del elemento mínimo en el resto de la lista
        min_index = i
        for j in range(i + 1, n):
            if word_list[j] < word_list[min_index]:
                min_index = j

        # Swap the minimum element with the element at the current position
        word_list[i], word_list[min_index] = word_list[min_index], word_list[i]


words = ["banana", "cherry", "apple", "date"]
selection_sort(words)

print("Lista de palabras ordenada alfabéticamente en orden ascendente:")
print(words)

#Ejericio 3
#function to obtain the title of a book
def get_tittle(books):
    return books["titulo"]

books = [
    {
        "titulo": "El Hobbit",
        "autor": "J.R.R. Tolkien",
        "año_publicación": 1937,
        "género": "Fantasía",
        
    },
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año_publicación": 1967,
        "género": "Realismo mágico",
        
    },
    {
        "titulo": "El Gran Gatsby",
        "autor": "F. Scott Fitzgerald",
        "año_publicación": 1925,
        "género": "Novela",
        
    }
]

books_sorted=sorted(books,key=get_tittle)
print("Orden de titulos por orden alfabetico")  
for book in books_sorted: 
 print("Titulo",book["titulo"])           
        

