def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for listadd in range(len(participant)-len(completion)):
        completion.append("0")
    for i in range(len(participant)):
        if completion[i] != participant[i]:
            answer+= participant.pop(i)
            participant.append("0")  
            
    return answer