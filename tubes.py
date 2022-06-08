import streamlit as st
import string

st.write("""Lexical Analyzer dan Parser""")

st.write('S = <noun> <verb> <noun>')
st.write('noun = agi | kaka | kitab | kasut | miso | bengkau | seluar')
st.write('verb = ngoge | man | pake')
st.write('contoh = kaka pake kasut')

sentence = st.text_input("Masukan kalimat: ", placeholder="Masukan kalimat noun verb noun")
validation = st.button("Validasi Grammar")

input_string = sentence.lower()+'#'
token = sentence.lower().split()
token.append('EOS')

#inisialisasi list akphabet
alphabet_list = list(string.ascii_lowercase)

#inisialisasi state
state_list = []
for i in range(44):
    state_list.append('q%s'%i)

#inisialisasi tabel transisi
transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

#tambah spasi sebelum input
transition_table['q0', ' '] = 'q0'

#transisi tabel untuk bengkau
transition_table['q0', 'b'] = 'q1'
transition_table['q1', 'e'] = 'q2'
transition_table['q2', 'n'] = 'q3'
transition_table['q3', 'g'] = 'q4'
transition_table['q4', 'k'] = 'q5'
transition_table['q5', 'a'] = 'q6'
transition_table['q6', 'u'] = 'q7'
transition_table['q7', ' '] = 'q8'
transition_table['q7', '#'] = 'accept'
transition_table['q8', ' '] = 'q8'
transition_table['q8', '#'] = 'accept'

#transisi tabel untuk ngoge
transition_table['q0', 'n'] = 'q9'
transition_table['q9', 'g'] = 'q10'
transition_table['q10', 'o'] = 'q11'
transition_table['q11', 'g'] = 'q12'
transition_table['q12', 'e'] = 'q13'

#transisi tabel untuk miso
transition_table['q0', 'm'] = 'q14'
transition_table['q14', 'i'] = 'q15'
transition_table['q15', 's'] = 'q16'
transition_table['q16', 'o'] = 'q17'
transition_table['q17', ' '] = 'q8'
transition_table['q17', '#'] = 'accept'
transition_table['q8', ' '] = 'q8'
transition_table['q8', '#'] = 'accept'

#transisi tabel untuk man
transition_table['q0', 'm'] = 'q14'
transition_table['q14', 'a'] = 'q18'
transition_table['q18', 'n'] = 'q19'
transition_table['q19', ' '] = 'q8'
transition_table['q19', '#'] = 'accept'
transition_table['q8', ''] = 'q8'
transition_table['q8', '#'] = 'accept'

#transisi untuk agi
transition_table['q0', 'a'] = 'q20'
transition_table['q20', 'g'] = 'q21'
transition_table['q21', 'i'] = 'q22'
transition_table['q22', ' '] = 'q8'
transition_table['q22', '#'] = 'accept'
transition_table['q8', ' '] = 'q8'
transition_table['q8', '#'] = 'accept'

#transisi untuk kaka
transition_table['q0', 'k'] = 'q23'
transition_table['q23', 'a'] = 'q24'
transition_table['q24', 'k'] = 'q25'
transition_table['q25', 'a'] = 'q26'
transition_table['q26', ' '] = 'q8'
transition_table['q26', '#'] = 'accept'
transition_table['q8', ' '] = 'q8'
transition_table['q20', '#'] = 'accept'

#transisi untuk kasut
transition_table['q0', 'k'] = 'q23'
transition_table['q23', 'a'] = 'q24'
transition_table['q24', 's'] = 'q27'
transition_table['q27', 'u'] = 'q28'
transition_table['q28', 't'] = 'q29'
transition_table['q29', ' '] = 'q8'
transition_table['q29', '#'] = 'accept'
transition_table['q8', ' '] = 'q8'
transition_table['q8', '#'] = 'accept'

#transisi untuk kitab
transition_table['q0', 'k'] = 'q23'
transition_table['q23', 'i'] = 'q30'
transition_table['q30', 't'] = 'q31'
transition_table['q31', 'a'] = 'q32'
transition_table['q32', 'b'] = 'q33'
transition_table['q33', ' '] = 'q8'
transition_table['q33', '#'] = 'accept'
transition_table['q8', ' '] = 'q8'
transition_table['q8', '#'] = 'accept'

#transisi untuk pake
transition_table['q0', 'p'] = 'q34'
transition_table['q34', 'a'] = 'q35'
transition_table['q35', 'k'] = 'q36'
transition_table['q36', 'e'] = 'q37'
transition_table['q37', ' '] = 'q8'
transition_table['q37', '#'] = 'accept'
transition_table['q8', ' '] = 'q8'
transition_table['q8', 'accept'] = 'accept'

#transisi tabel untuk seluar
transition_table['q0', 's'] = 'q38'
transition_table['q38', 'e'] = 'q39'
transition_table['q39', 'l'] = 'q40'
transition_table['q40', 'u'] = 'q41'
transition_table['q41', 'a'] = 'q42'
transition_table['q42', 'r'] = 'q43'
transition_table['q43', ' '] = 'q8'
transition_table['q43', '#'] = 'accept'
transition_table['q8', ' '] = 'q8'
transition_table['q8', '#'] = 'accept'


#transisi ke token baru
transition_table['q8', 'b'] = 'q1'
transition_table['q8', 'n'] = 'q9'
transition_table['q8', 'm'] = 'q14'
transition_table['q8', 'a'] = 'q20'
transition_table['q8', 'k'] = 'q23'
transition_table['q8', 'p'] = 'q34'
transition_table['q8', 's'] = 'q38'

#definisi untuk simbol terminal dan non terminal
terminal = ['agi', 'kaka', 'kitab', 'kasut', 'miso', 'bengkau', 'seluar', 'ngoge', 'man', 'pake']
non_terminal = ['S', 'NN', 'VB']


#definisi untuk parse tabel
parse_table = {}

#inisialisasi parse tabel S
parse_table[('S', 'agi')] = ['NN', 'VB', 'NN']
parse_table[('S', 'kaka')] = ['NN', 'VB', 'NN']
parse_table[('S', 'kitab')] = ['NN', 'VB', 'NN']
parse_table[('S', 'kasut')] = ['NN', 'VB', 'NN']
parse_table[('S', 'miso')] = ['NN', 'VB', 'NN']
parse_table[('S', 'bengkau')] = ['NN', 'VB', 'NN']
parse_table[('S', 'seluar')] = ['NN', 'VB', 'NN']
parse_table[('S', 'ngoge')] = ['error']
parse_table[('S', 'man')] = ['error']
parse_table[('S', 'pake')] = ['error']
parse_table[('S', 'EOS')] = ['error']

#inisialisasi parse tabel NN
parse_table[('NN', 'agi')] = ['agi']
parse_table[('NN', 'kaka')] = ['kaka']
parse_table[('NN', 'kitab')] = ['kitab']
parse_table[('NN', 'kasut')] = ['kasut']
parse_table[('NN', 'miso')] = ['miso']
parse_table[('NN', 'bengkau')] = ['bengkau']
parse_table[('NN', 'seluar')] = ['seluar']
parse_table[('NN', 'ngoge')] = ['error']
parse_table[('NN', 'man')] = ['error']
parse_table[('NN', 'pake')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

#inisialisasi parse tabel VB
parse_table[('VB', 'agi')] = ['error']
parse_table[('VB', 'kaka')] = ['error']
parse_table[('VB', 'kitab')] = ['error']
parse_table[('VB', 'kasut')] = ['error']
parse_table[('VB', 'miso')] = ['error']
parse_table[('VB', 'bengkau')] = ['error']
parse_table[('VB', 'seluar')] = ['error']
parse_table[('VB', 'ngoge')] = ['ngoge']
parse_table[('VB', 'man')] = ['man']
parse_table[('VB', 'pake')] = ['pake']
parse_table[('VB', 'EOS')] = ['error']


#program analisa lexical/kata
if validation:
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'error':
            st.title('Hasil Lexical Analyzer:')
            st.error('input '+current_token+' tidak sesuai dengan daftar kata-kata')
            break
        idx_char = idx_char+1
    
    #kesimpulan analisa lexical
    if state == 'accept':
        st.title('Hasil Lexical Analyzer:')
        st.success('input : '+sentence+ ', sesuai dengan daftar kata-kata')
        
        
        
 # parser main program

    # Stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    # Input reading initialization
    idx_token = 0
    symbol = token[idx_token]

    # parsing
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        if top in terminal:
            if top == symbol:
                stack.pop()
                idx_token = idx_token+1
                symbol = token[idx_token]
                if symbol == 'EOS':
                    stack.pop()
            else:
                st.error('input '+sentence+' tidak sesuai grammar')
                break
        elif top in non_terminal:
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbols_to_be_paused = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_paused)-1, -1, -1):
                    stack.append(symbols_to_be_paused[i])
            else:
                break
        else:
            break

    # conclusion
    st.write()
    st.title('Hasil Parser:')
    if symbol == 'EOS' and len(stack) == 0:
        st.success('Input '+sentence+' diterima, sesuai grammar')
    else:
        st.error('input '+sentence+' tidak sesuai grammar')
    
