if __name__ == '__main__':
    l = []
    same_scores = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        scores.add(score)
    second_lowest = sorted(scores)[1]
    
    for name,score in l:
        if score == second_lowest:
            same_scores.append(name)
    for name in sorted(same_scores):
        print(name)
    

        