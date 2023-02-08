import streamlit as st
from PIL import Image
import streamlit.components.v1 as stc
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">App </h1>
    <p style="color:white;text-align:center;">Built by Knowledge team</p>
    </div>
    """
stc.html(HTML_BANNER)

#st.header("Creec Application", )
st.image("https://www.creec.or.ug/wp-content/uploads/2020/04/cropped-IMG-20181004-WA0000-6.jpg")
st.sidebar.header("CREEC Knowleadgemet Platform")
st.sidebar.image("https://strategy-alliance.com/so-media/original/SKill.png")
stc.html(HTML_BANNER)


st.sidebar.button("About")
st.sidebar.button("Projects")
st.sidebar.button("Publications")
st.sidebar.button("Team ")

with st.expander("Publications"):
    stc.html(HTML_BANNER)
    ("1. MECS \n"
     "2. Research")

with st.expander("Projects"):
    st.write("List of projects")

with st.expander("Projects"):
    col1, col2 = st.columns(2)
    with col1:
        st.write("solar")
        st.image(
            "https://cdn.vox-cdn.com/thumbor/jfNeex8Gr4d6Vk6awLYnnLrWrZU=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/13457847/510728016.jpg.jpg")
    with col2:
        st.write("Biomass")
        st.image("https://5.imimg.com/data5/SELLER/Default/2021/4/YA/JU/XE/113210729/high-grade-bio-coal-1000x1000.jpg")

