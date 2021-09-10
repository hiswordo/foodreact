######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Page Title
######################

# image = Image.open('dna-logo.jpg')

st.image('dna-logo.jpg') # , use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()[1:] # Skips the sequence name (first line)
# sequence = sequence[1:] 
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_countlist(seq):
  d = [
        ('A',seq.count('A'),'adenine (A)'),
        ('T',seq.count('T'),'thymine (T)'),
        ('G',seq.count('G'),'guanine (G)'),
        ('C',seq.count('C'),'cytosine (C)')
        ]
  return d

Y = DNA_nucleotide_countlist(sequence)

Y

# def DNA_nucleotide_count(seq):
#   d = dict([
#             ('A',seq.count('A')),
#             ('T',seq.count('T')),
#             ('G',seq.count('G')),
#             ('C',seq.count('C'))
#             ])
#   return d

# X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

# X

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame(Y, columns=['nucleotide','count','fullname'])
df

# df = pd.DataFrame.from_dict(X, orient='index')
# df = df.rename({0: 'count'}, axis='columns')
# df.reset_index(inplace=True)
# df = df.rename(columns = {'index':'nucleotide'})
# st.write(df)

### 2. Print text
st.subheader('2. Print text')
for index, row in df.iterrows():
    st.write('There are  ' , row['count'] , row['fullname'])
# st.write('There are  ' + str(Y[0][1]) + ' adenine (A)')
# st.write('There are  ' + str(Y[1][1]) + ' thymine (T)')
# st.write('There are  ' + str(Y[2][1]) + ' guanine (G)')
# st.write('There are  ' + str(Y[3][1]) + ' cytosine (C)')

# st.write('There are  ' + str(X['A']) + ' adenine (A)')
# st.write('There are  ' + str(X['T']) + ' thymine (T)')
# st.write('There are  ' + str(X['G']) + ' guanine (G)')
# st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 4. 長條圖 Display Bar Chart using Altair 
# X軸會自動按`數字`或`英文`升幂排列
st.subheader('4. Display Bar chart')
df.index = ['A','T','G','C']
bardf = df.iloc[:,1]
bardf
st.bar_chart(bardf)

# p = alt.Chart(df).mark_bar().encode(
#     x='nucleotide',
#     y='count'
# )
# p = p.properties(
#     width=alt.Step(80)  # controls width of bar.
# )
# st.write(p)