def accuracy(true, preds):
    return sum(1 for t, p in zip(true, preds) if t.lower() == p.lower().split('\n')[-1])/len(true)


def ner_accuracy(true, preds):
    total = 0
    correct = 0
    for t, p in zip(true, preds):
        clean_preds = [x.strip() for x in p.lower().split('\n')[-1].split(',')]
        for t1 in t:
            if t1.lower().strip() in clean_preds:
                correct += 1
            total += 1
    return correct/total