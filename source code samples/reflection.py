
def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()

    if seq == emptySeq:
        return emptySeq

    #print("sequential vector = ", seq[1:])
    restrev = reverse(seq[1:])
    #print ("retrev = ", restrev)
    first = seq[0:1]
    #print ("first = ",first)
    restrev += first
    return restrev
        

def main():
    print(reverse([1,2, 3, 4]))
    #print(reverse("hello"))

if __name__ == "__main__":
    main()