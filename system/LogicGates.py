from itertools import product
import time


def truth_table(num_vars, func, gate_name):
    if num_vars != func.__code__.co_argcount:
        raise ValueError(f"{gate_name} expects {func.__code__.co_argcount} inputs")

    var_names = [chr(ord("A") + i) for i in range(num_vars)]
    header = " | ".join(var_names) + " | OUT"
    print(f"\n=== {gate_name} ===")
    print(header)
    print("-" * len(header))

    for inputs in product([0, 1], repeat=num_vars):
        out = func(*inputs)
        row = " | ".join(str(x) for x in inputs)
        print(f"{row} | {out}")


def AND(A, B): return int(A and B)
def OR(A, B): return int(A or B)
def NOT(A): return int(1 - A)
def NAND(A, B): return int(not (A and B))
def NOR(A, B): return int(not (A or B))
def XOR(A, B): return int(A ^ B)
def XNOR(A, B): return int(not (A ^ B))


GATES = [
    ("AND", 2, AND),
    ("OR", 2, OR),
    ("NOT", 1, NOT),
    ("NAND", 2, NAND),
    ("NOR", 2, NOR),
    ("XOR", 2, XOR),
    ("XNOR", 2, XNOR),
]


def main():
    for i, (name, num_vars, func) in enumerate(GATES):
        truth_table(num_vars, func, name)

        if i < len(GATES) - 1:
            input("\nPlease press `Enter` to continue")
            print("---------------------------------")
            print("Please wait loading next table...")
            time.sleep(4)
        else:
            print("---------------------------------")
            print("End of LogicGate Demo!")


if __name__ == "__main__":
    main()
