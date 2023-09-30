from  frequentWordsProblem import frequentWords, readData

def Main():
    #Read Dataset 1 & Save it as Text, K:
    Data = readData(1)
    Text = Data[0]
    Kmer = int(Data[1])
    #Run the frequent words problem with the choosen set:
    RepeatedPatterns = frequentWords(Text, Kmer)
    #Print the most frequent patterns:
    print("The maost frequent k-mers in dataset 1 are: ", RepeatedPatterns, "\n")

    #Read Dataset 2 & Save it as Text, K:
    Data = readData(2)
    Text = Data[0]
    Kmer = int(Data[1])
    #Run the frequent words problem with the choosen set:
    RepeatedPatterns = frequentWords(Text, Kmer)
    #Print the most frequent patterns:
    print("The maost frequent k-mers in dataset 2 are: ", RepeatedPatterns)

if __name__ == "__main__":
    Main()
