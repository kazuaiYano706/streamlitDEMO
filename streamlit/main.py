import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('成長株判定')
st.write('interactive Widgets')
'Start!!'

latst_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latst_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!'
#
# text=st.text_input('yourhubby')
# 'yourhobby:',text
#
# option = st.selectbox('chois your number', list(range(1, 11))
#              )
# 'your love',option


condision=st.slider('anatanochousi',0,100,50)

'your',condision

left_column,right_column = st.columns(2)
button = left_column.button('右に文時g表示')
if button:
    right_column.write('migikaramu')

eee = st.expander('toiawase')
eee.write('toiawase')




# st.title('Streamlit 超入門')
#
# st.write('DataFrame')
#
# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns= ['a','b','c'],
#     )
    # 'row1':[1,2,3,4,],
    # 'row2':[0,20,30,40]
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)
#
# st.dataframe(df.style.highlight_max(axis=0))#, width = 100, height = 100)
# st.write(df, width=100, height=100)
# st.table(df.style.highlight_max(axis=0))
#
# """
#
# # 章
# ## 節
# ### 項
#
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
#
# """

