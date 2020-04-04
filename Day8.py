def get_pairs():
    
    t = int(input())
    phoneBook = {}
    for i in range(t):
        name, number = input().split()
        phoneBook[name] = number
    
    query = input()
    while(query):
        if(query in phoneBook.keys()):
            print(query, '=', phoneBook[query], sep='')
        else:
            print('Not found')
        try:
            query = input()
        except EOFError:
            break

        
get_pairs()