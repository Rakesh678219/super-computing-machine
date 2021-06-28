import streamlit as st


def app():
    st.header('Eyes the Windows to Your Health ')
    video_file = open('intro.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time=1)

    st.write(""" **Your eyes are tiny spheres of wonder. 
    A doctor can find warning signs of high blood pressure, diabetes, and a whole range of other
    systemic health issues, just by examining your eyes. Ophthalmologist Neal Adams explains
    why the eye's tissues and blood vessels make such a good barometer for wellness** """)

    st.header('Animation: Dilated Eye Exam')
    video_file = open('Animation_ Dilated Eye Exam.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time=1)
    st.write('** This video describes what the doctor sees when examining the retina (the light-sensitive tissue at the back of the eye), macula (the part of the retina needed for sharp, central vision) and optic nerve (which connects the retina to the brain).**')

    st.header('How Your Eyes Make Sense of the World ?')
    video_file = open('eye_decoder.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time=1)
    st.write('** How does the eye work exactly?  learn some of the extraordinary science behind how your eyes and brain work together to perceive the world around you **')

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
            # RV COLLEGE OF ENGINEERING
            """
        )
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
