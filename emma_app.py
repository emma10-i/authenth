import streamlit as st

with st.container():
    st.set_page_config(page_title="E-chat",
                       page_icon=":tada🌴:",
                       layout="wide")

st.title("E-CHAT NIGERIA ")
st.subheader("ALL ABOUT TRENDS AND LATEST INFO")

with st.container():
    st.write("___")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("President Bola Ahmed Tinubu plans to reduce fuel price ")
        st.write("""due to the upcoming 2027 election
                 president bola ahmed tinubu has planed
                 to reduce the price of fuel by 5%
                 from 1500 naira to 1450 naira""")
        st.write("[read more>](https//punch.com)")

    with right_column:
        st.header("EL-NINO 'heats' Nigeria")
        st.write("""heat wave strikes west Africa
                 experts advice to take enough water
                 every day to prevent dehydration
                 which can lead to death""")
        st.write("[read more>](https//punch.com)")

with st.container():
    st.write("___")
    st.header("other virals")
    st.write("##")
    image_column,text_column=st.columns((1,2))

    with image_column:
       video_url = "https://www.youtube.com/watch?v=XVRWjCNoH5A"
st.video(
    video_url, 
    format="video/mp4", 
    start_time=0
)







    with text_column:
        st.subheader("latest tiktok trend")
        st.write("this trend makes no sense 🌴")

        st.markdown("[watch video>](https//tiktok.com)")
