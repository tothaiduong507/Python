#Define the state of each cell of the garden to be: New Seed, Obstacle, Live Tree, Dead Tree, Warehouse
from Queue import Queue
N=1000#define N
R=0 #initiate the row size
C=0 #initiate the column size
matrix=[] #state of each cell [i][j] in the garden
move=[[0,1],[1,0],[-1,0],[0,-1]] #move we can conduct
#x,y  x move[i][0] y move[i][1]  for i in range(0,4)
step=[[0]*(N+1)for i in range(N+1)]#the step it takes to get to (i,j) from (0,0)
visited=[[False] * (N+1) for i in range(N+1)] #define that the cell is visited or not(initiate all to false at first)
#visite[x][y] kiem tra xem toa do [x][y] da duoc di den hay chua
percept_sequence= []
action=[]
stack=[]
total_steps=0
#----------------------------------------------------------------------------------------------
def Input(R,C):
    R=int(input("What is the row size? "))
    C=int(input("What is the column size? "))
    for i in range (0,R):
        a=[]
        for j in range(0,C):
            a.append(input())
        matrix.append(a)

    print(matrix)
    return[R,C]

def bfs(x,y):
    queue=Queue(list)
    queue.__init__(N)
    queue.enqueue([x, y])
    visited[x][y]= True
    while not queue.isEmpty() :
        [u, v]=queue.peek()
        print(u,v)
        queue.dequeue()
        for i in range(0,4):
            x=int(u+move[i][0])
            y=int(v+move[i][1])
            print(x,y)
            if (x>= 0) and (y>= 0) and (x< R) and (y< C) and (bool(visited[x][y]) == False) :
                if matrix[x][y] == 'Obstacle':
                    break
                elif matrix[x][y] == 'New Seed':
                    step[x][y] = step[u][v] + 1
                    print(step[x][y])
                    queue.enqueue([x, y])
                    print(queue)
                    visited[x][y] = True
                elif matrix[x][y] == 'Live Tree':
                    # Can use A* here
                    step[x][y] = step[u][v] + 1
                    #step[x][y]=step[x][y] *3
                    print(step[x][y])
                    queue.enqueue([x, y])
                    print(queue)
                    visited[x][y] = True
                elif matrix[x][y] == 'Dead Tree':
                    step[x][y] = step[u][v] + 1
                    #step[x][y] = step[x][y] *3
                    print(step[x][y])
                    queue.enqueue([x, y])
                    print(queue)
                    visited[x][y] = True
                else:
                    return
    return
def shortestPath(i,j) :
    pass
def dfs(x,y,total_steps) :
    stack.append([x,y])
    visited[x][y] = True
    #print(x,y)
    #print(stack)
    cnt_child=0
    #[u,v]=stack[-1]
    #print(u,v)
    for i in range(0,4):
        m = int(x + move[i][0])
        n = int(y + move[i][1])
        #print(m, n)
        if (m >= 0) and (n >= 0) and (m < R) and (n < C) and (bool(visited[m][n]) == False) and matrix[m][n] != 'Obstacle':
            if matrix[m][n] == 'New Seed':
                cnt_child+=1
                step[m][n]=step[x][y]+1
                #print("step is "+str(step[m][n]))
                total_steps+= 1
                #print("total step is "+ str(total_steps))
                #dfs(m,n)
                total_steps=int(dfs(m,n,total_steps)) #recursion in dfs
            elif matrix[m][n] == 'Live Tree':
                cnt_child += 1
                step[m][n] = step[x][y] + 1
                #print("step is "+str(step[m][n]))
                total_steps += int(1+2 * int(step[m][n]))
                #print("total step is "+ str(total_steps))
                #dfs(m,n)
                total_steps=int(dfs(m,n,total_steps))
            elif matrix[m][n] == 'Dead Tree':
                cnt_child += 1
                step[m][n] = step[x][y] + 1
                #print(step[m][n])
                total_steps += int(1+2 * int(step[m][n]))
                #print(total_steps)
                #dfs(m,n)
                total_steps=int(dfs(m,n,total_steps))
            else:
                visited[m][n]=True
                return
    #if cnt_child==0: thi totalstep+=1
    return total_steps
#main

[R,C]=Input(R,C)
#bfs(0,0)
#dfs(0,0,0)
print(dfs(0,0,0))
#total_steps=max(max(x) for x in step)
#print(total_steps)
