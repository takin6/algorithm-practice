# Python program to print postorder  
# traversal from preorder and  
# inorder traversals 

postorder = []

def printpostorder(inorder, preorder, n): 
    print(inorder, preorder, n)

    if preorder[0] in inorder: 
        root = inorder.index(preorder[0]) 
          
    if root != 0: # left subtree exists 
        printpostorder(inorder[:root],  
                       preorder[1:root + 1],  
                       len(inorder[:root])) 
      
    if root != n - 1: # right subtree exists 
        printpostorder(inorder[root + 1:],   
                       preorder[root + 1:],  
                       len(inorder[root + 1:])) 
    
    postorder.append(preorder[0])
          

n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))
printpostorder(inorder, preorder, n)

print( " ".join( [ str(i) for i in postorder ]))