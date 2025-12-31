def plural_fsm(noun):
    state = "q0"
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        state = "q1"
    elif noun.endswith("y") and noun[-2] not in "aeiou":
        state = "q2"
    if state == "q1":
        plural = noun + "es"
    elif state == "q2":
        plural = noun[:-1] + "ies"
    else:
        plural = noun + "s"

    return plural
nouns = ["book", "bus", "box", "city", "baby", "dish", "boy"]
print("Singular\tPlural")
print("-----------------------")
for n in nouns:
    print(n, "\t\t", plural_fsm(n))

