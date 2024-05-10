def solution(text, ending):
    if text[-len(ending) :] == ending:
        return True
    else:
        return False
