import streamlit as st


def app():

    st.header('Minor Project Credits ')
    video_file = open('project_Credits.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time=1)

    st.header('Contact Details')
    col1, col2, col3, col4 = st.beta_columns([1, 1, 1, 1])

    with col1:
        st.write('Pratheek J Bhat')
        st.write("phno:9483982869")
    with col2:
        st.write("Pavan Kalyan D S")
        st.write("phno:6363509493")
    with col3:
        st.write("Rakesh Reddy P ")
        st.write("phno:6303665574")
    with col4:
        st.write("Prajwal B Raj")
        st.write("phno:8548867840")

    def draw_all(
        key,
        plot=False,
    ):
        col1, col2, col3 = st.beta_columns([1, 4.5, 1])

        with col1:
            st.write("")

        with col2:
            st.image('rvce.png')

        with col3:
            st.write("")

        st.write(
            """
                        # Minor Project On ML
                        
                        """
        )
        st.write("#")
        st.header("Contributed by")
        st.write(
            """
                        **Pavankalyan D S  - 1RV18EC108**\n
                        **Rakesh Reddy P -  1RV18EC109**\n
                        **Prajwal  B  Raj -  1RV18EC111** \n
                        **Pratheek J Bhat -  1RV18EC105**\n
                        
                        """
        )
        st.write("#")
        st.header("Guided by")
        st.write(
            """
                        **Rajani Katiyar, Assistant Professor, Electronics and Communication Engineering.** 
                        """
        )
    with st.sidebar:
        draw_all("sidebar")
