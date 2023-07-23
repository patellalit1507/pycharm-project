
def Bubble_sort(elements,key):
    l=len(elements)
    for j in range(l-1):
     for i in range(l-1-j):
         #swap=False
          if elements[i][key]>elements[i+1][key]:
              temp=elements[i+1]
              elements[i+1]=elements[i]
              elements[i]=temp


    return elements



if __name__ == '__main__':
    elements = [
        {'name': 'mona', 't_a': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 't_a': 400, 'device': 'google pixel'},
        {'name': 'kathy', 't_a': 200, 'device': 'vivo'},
        {'name': 'aamir', 't_a': 800, 'device': 'iphone-8'},
    ]


    print(Bubble_sort(elements,key="t_a"))



