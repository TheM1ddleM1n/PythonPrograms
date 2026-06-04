def Find(Phrase, Word):
    Start = Phrase.find(Word)
    End = Start + len(Word) - 1
    return Start, End


Phrase = "Clean code always looks like it was written by someone who cares."
Word = "written"
Start, End = Find(Phrase, Word)
print(
    "'{}' can be found between characters {} and {} in '{}'.".format(
        Word, Start, End, Phrase
    )
)
