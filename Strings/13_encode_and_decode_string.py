def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s

    return res


def decode(str):
    res, i = [], 0

    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j+1 : j+1+length])
        i = j+1+length
    
    return res





if __name__ == "__main__":
    
    X = ["Hello","everyone","have","a", "great", "day"]
    Y = "5#Hello8#everyone4#have1#a5#great3#day"
    print(encode(X))
    print(decode(Y))
    
    print("\n")

    Z = ["we", "say", ":", "yes"]
    A = "2#we3#say1#:3#yes"
    print(encode(Z))
    print(decode(A))

