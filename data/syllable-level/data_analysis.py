import os

if __name__ == "__main__":
    datadir = "train"
    
    with open(os.path.join(datadir, "seq.in"), "r") as f:
        sequences = []
        for line in f:
            sequences.append(line.strip().split())
    with open(os.path.join(datadir, "label"), "r") as f:
        intents = []
        for line in f:
            intents.append(line.strip())
    with open(os.path.join(datadir, "seq.out"), "r") as f:
        slots = []
        for line in f:
            slots.append(line.strip().split())
    total = len(intents)
    with open(os.path.join(datadir, "data.txt"), "w") as f:
        for i in range(total):
            assert len(slots[i])==len(sequences[i]), "len(slots[i])!=len(sequences[i])"
            line = " ".join(sequences[i])+"\t"+intents[i]+"\t"
            for j in range(len(slots[i])):
               line  = line + "[{}:{}] ".format(sequences[i][j], slots[i][j])
            f.write(line.strip()+"\n")