cat = ""
ans = ""
hint = ""
out = list()
guessed = set()
lives = 10
score = 0
gameOver = False
def selectCategory():
    catalogue = ["Superheroes","Disney Characters"]
    print("Select Category:")
    for i in range(len(catalogue)): print(str(i+1)+".) "+catalogue[i])
    while True:
        global cat
        print("Category number: ",end = "")
        x = input().strip()
        if not x.isdigit():
            print("Invalid choice, try again.")
            continue
        x = int(x)
        if x < 1 or x > len(catalogue):
            print("Invalid choice, try again.")
            continue
        global cat
        cat = catalogue[x-1]
        print(cat,"is selected.",end = "\n\n")
        cat = "resources/" + cat + ".txt"
        initialize()
        return
    
def initialize():
    global ans
    global hint
    global out
    global guessed
    global lives
    global gameOver
    ans,hint = __import__("random").choice(list(open(cat))).strip().split(",")
    out = ["_" if c.isalpha() else c for c in ans]
    guessed = set()
    lives = 10
    gameOver = False
def reveal(x):
    global lives
    global guessed
    global score
    if x not in ans.lower():
        if x in guessed:
            print(x,"has already been guessed")
            return
        lives -= 1
        guessed.add(x)
        return
    if x in out:
        print(x, "is revealed")
        return
    for i in range(len(ans)):
        if ans.lower()[i] == x:
            out[i] = ans[i]
            score += 10
    
def output():
    global gameOver
    global score
    if "_" not in out:
        gameOver = True
        print("The answer is \"" + ans + "\"")
        print("You win!!")
    elif lives == 0:
        gameOver = True
        score = 0
        print("The answer is \"" + ans + "\"")
        print("You lose!!")
    else:
        print(" ".join(out), end = "   ")
        print("score",score,end="")
        print(", Remaining wrong guessed:", lives,end = "")
        print(", Wrong guessed:" , ", ".join(sorted(guessed)))

while True:
    selectCategory()
    print("Hint:",hint)
    output()
    while not gameOver:
        x = input().strip().lower()
        if len(x) != 1 or not x.isalpha():
            print("Please input single alphabet.")
            continue
        reveal(x)
        output()
    print("Do you wish to continue playing?[Y/N]: ", end = "")
    x = input().strip().upper()
    if x != "Y":
        print("Exiting game...")
        __import__("time").sleep(1)
        break
