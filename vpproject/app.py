import streamlit as st
import base64
from PIL import Image, ImageFile
import detection

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_img(img_file):
    bin_str = get_base64_of_bin_file(img_file)
    page_bg_img = '''
    <style>
    
    body {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        
        
    }
    header {
        color: white;
    }
    
    main {
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        font-size: 20px;
        color: white;
    }
    
    footer {
        color: white;
        background-color: #242424;
        padding: 1rem 1rem ;
        justify-content: center;
        align-items: center;
        font-size: 20px;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def main():
    
    chart = Image.open("chart.jpg")
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    
    set_bg_img("img-3.jpg")
    st.markdown("""<header>
                    <h1>Driver Drowsiness Detection</h1>
                    <p>System that ensures that everyone has a save journey</p>
                </header>
                """ , unsafe_allow_html=True)
    st.markdown("""<p>
                    System to ensure Safe Long Travels!
                </p>
                &nbsp;
                """, unsafe_allow_html=True)
    
    if st.button("Start System"):
        st.write("Starting the System!")
        detection.start_system()
         
    st.markdown(
        """
            &nbsp;
            <main>
                <p>
                    Driver Drowsiness Detection System is a system made to ensure that the Driver doesn't fall asleep during long distance
                    travels. The system is suited for those people who have to cover long trails and distances. The system alarms the Driver
                    if he falls asleep due to the heavy load of tiredness caused by spontaneous driving of buses/transport. The chart below
                    indicates the different causes for accidents. As it can been seen, drowziness conditions are only at the second to carelessness.
                </p>
            </main>
        """
    , unsafe_allow_html=True)
    
    st.image(chart, caption="A Survey conducted on Various Causes of Accidents" ,use_column_width=True)
    
    st.markdown(
        """
            &nbsp; &nbsp;
            <footer>
                &copy; Copyrights2021. Made by Darain Mukkaram, Hassan Farid and Daniyal Mehmood.
                &nbsp; Developed using StreamLit and Open-CV
            </footer>
        """
        , unsafe_allow_html=True
    )
    
if __name__ == "__main__":
    main()
