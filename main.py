from automata.fa.dfa import DFA

from visual_automata.fa.dfa import VisualDFA

dfa = DFA(
    states={'q0', 'q1', 'q2', 'd'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'd', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q1'},
        'q2': {'0': 'q2', '1': 'q1'},
        'd': {'0': 'd', '1': 'd'},
    },
    initial_state='q0',
    final_states={'q2'}
)


import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("DFA")
root.resizable(False, False)
root.configure(bg='#33FFBD')

States = tkinter.Entry(root, width=40, font=('Arial 12'), )
StartingState = tkinter.Entry(root, width=40, font=('Arial 12'), )
InputSymbols = tkinter.Entry(root, width=40, font=('Arial 12'), )
InputSymbols = tkinter.Entry(root, width=40, font=('Arial 12'), )
InputTransitions = tkinter.Text(root,
                   height = 5,
                   width = 40, font=('Arial 12'))
InitialState = tkinter.Entry(root, width=40, font=('Arial 12'), )
InitialState = tkinter.Entry(root, width=40, font=('Arial 12'), )
FinalState = tkinter.Entry(root, width=40, font=('Arial 12'), )
FinalState = tkinter.Entry(root, width=40, font=('Arial 12'), )
InputString = tkinter.Entry(root, width=40, font=('Arial 12'), )
# ee = tkinter.Entry(root, width=40)

States.grid(row=0, column=4, columnspan=4)
InputSymbols.grid(row=1, column=4, columnspan=4)
InputTransitions.grid(row=2, column=4, columnspan=4)
InitialState.grid(row=3, column=4, columnspan=4)
FinalState.grid(row=4, column=4, columnspan=4)
L1 = tkinter.Label(root, text="Enter states: ", background="#33FFBD")
L1.grid(row=0, column=0, columnspan=4)
L2 = tkinter.Label(root, text="Enter input symbols: ", background="#33FFBD")
L2.grid(row=1, column=0, columnspan=4)
L3 = tkinter.Label(root, text="Enter transitions: ", background="#33FFBD")
L3.grid(row=2, column=0, columnspan=4)
L4 = tkinter.Label(root, text="Enter initial state: ", background="#33FFBD")
L4.grid(row=3, column=0, columnspan=4)
L5 = tkinter.Label(root, text="Enter final states: ", background="#33FFBD")
L5.grid(row=4, column=0, columnspan=4)
L6 = tkinter.Label(root, text="Enter input string: ", background="#33FFBD")
L6.grid(row=7, column=0, columnspan=4)


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct



def build():
    h = []
    dic = {}
    # <!-- states -->
    inputStates = States.get()
    inputStates_list = inputStates.split(' ')
    inputStates_set = set(inputStates_list)

    # <!-- inputs symbols -->
    input_Symbols = InputSymbols.get()
    input_Symbols_list = input_Symbols.split(' ')
    input_Symbols_list_set = set(input_Symbols_list)

    input_transitions = InputTransitions.get("1.0", 'end-1c')

    d = input_transitions
    e = d.split('\n')
    for i in e:
        h.append(i.split(' '))
    for j in h:
        temp = j[0]
        j.pop(0)
        dic[temp] = j
    for m, n in dic.items():
        dic[m] = Convert(n)

    #           <!-- initial state -->
    input_initialstate = InitialState.get()

    # <!-- final state  -->
    input_finalstate = FinalState.get()
    input_finalstate_list = input_finalstate.split(' ')
    input_finalstate_set = set(input_finalstate_list)

    global dfa
    dfa = DFA(
        states=inputStates_set,
        input_symbols=input_Symbols_list_set,
        transitions=dic,
        initial_state=input_initialstate,
        final_states=input_finalstate_set
    )


    dfaVisual = VisualDFA(dfa)
    g1=dfaVisual.show_diagram()
    g1.view()

def check():

    if(dfa.accepts_input(InputString.get())):
        messagebox.showinfo("status", "Accepted")

    else:
        messagebox.showinfo("status", "Rejected")

button_Build = tkinter.Button(root, text="Build", height=3, bg="blue", activebackground='lime', font=('Arial 12'), command=lambda: build())  # command=lambda: getResult()
button_Check = tkinter.Button(root, text="Check", height=3, bg="blue", activebackground='lime', font=('Arial 12'), command=lambda: check())
button_Build.grid(row=6, column=0, columnspan=4, sticky="WE", )
button_Check.grid(row=6, column=6, columnspan=2, sticky="WE")

InputString.grid(row=7, column=4, columnspan=4, sticky="WE")


root.mainloop()