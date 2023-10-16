# streamlit 설치       !pip install streamlit
# 이 파일이 있는 폴더에서 아래 명령 실행
# (명령창에서)   streamlit run e_80_Streamlit.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


st.title('사이트 타이틀-23614')
st.header("큰제목")
st.subheader("소제목")
st.write("화면에 출력할 임의의 내용")

if st.button("Button"):
    st.write("버튼을 눌렀습니다.")
    # 임의의 작업 수행 코드
    
if st.checkbox('Checktbox'):
    st.write('선택!')
    
st.header("데이터프레임 보기")

# st.dataframe을 사용하면 인터랙티브한 테이블을 볼 수 있고
# st.table을 사용하면 정적인 테이블을 볼 수 있음

# 데이터프레임 샘플
df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.subheader("소팅이 가능한 데이터프레임(컬럼 클릭)")
st.dataframe(df)

st.subheader("정적인 테이블로 보기")
st.table(df)

# 그래프 그리기
st.header("데이터프레임 그래프")

st.subheader("line_chart")
st.line_chart(df)

st.subheader("area_chart")
st.area_chart(df)

st.subheader("bar_chart")
st.bar_chart(df)

# 고정된 이미지를 출력하려면 pyplot() 사용
st.subheader("정적인 그래프보기 pyplot")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

# plotly를 사용하여 인터랙티브한 그래프 만들기
st.subheader("plotly_chart")

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]
group_labels = ["Group 1", "Group 2", "Group 3"]

fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])
st.plotly_chart(fig)

st.subheader("vega_lite_chart")

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

st.vega_lite_chart(df,
    {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
        },
    },
    use_container_width=True,
)

# 컬럼을 나누어 보기 (아래로는 연속 스크롤링이 된다)
# columns 사용

st.header("세개의 컬럼으로 레이아웃 지정)")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

with col2:
   st.header("Button")
   if st.button("Button!!"):
           st.write("버튼......")

with col3:
	st.header("Chart Data")
	chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
	st.bar_chart(chart_data)
    
# 사용자로부터 임의의 변수 또는 파일을 입력 받기
# 키보드에서 입력 받기

value = st.text_input("변수를 입력하세요 i: ")

if value:
    st.write("이 변수를 사용합니다, i = ", value)
    # 이 변수를 사용한 프로그램 실행

# 파일을 업로드하기

f = st.file_uploader('파일을 올리세요........')
    # 이 파일을 사용한 프로그램 실행

