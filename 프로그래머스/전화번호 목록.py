def solution(phone_book):
    hashMap = {}
    for pb in phone_book:
        hashMap[pb] = True
    answer = True
    for pb in phone_book:
        jd = ""
        for p in pb:
            jd += p
            if jd != pb and hashMap.get(jd, False) != False:
                answer = False
    return answer


def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


print(solution2(["12", "123", "1235", "567", "88"]))
