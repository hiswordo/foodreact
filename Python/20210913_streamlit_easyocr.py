# @link [針對複雜場景的 OCR 文字識別，推薦一個Python 庫！_zeroing1 - MdEditor](https://www.gushiciku.cn/pl/g8Zy/zh-tw) at 2021/9/13
import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image, ImageDraw  # Image Processing
import numpy as np  # Image Processing

# title
st.title("Easy OCR - Extract Text from Images")

# subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

st.markdown("")

# image uploader
image = st.file_uploader(label="Upload your image here", type=["png", "jpg", "jpeg"])


@st.cache
def load_model():
    reader = ocr.Reader(["ch_sim", "en"], gpu = False, model_storage_directory=".")
    return reader


reader = load_model()  # load model

if image is not None:

    input_image = Image.open(image)  # read image
    st.image(input_image)  # display image

    with st.spinner("🤖 AI is at Work! "):

        result = reader.readtext(np.array(input_image))
        # result = reader.readtext(input_image)

        # result_text = []  # empty list for results

        # for text in result:
        #     result_text.append(text[1])

        # st.write(result_text)
        img = Image.open(input_image)
        draw = ImageDraw.Draw(img)

        for i in result:
            draw.rectangle((tuple(i[0][0]),tuple(i[0][2])),fill=None,outline='red',width=2)
        img.save(input_image)

        st.write(result)

    # st.success("Here you go!")
    st.balloons()

else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by @1littlecoder")


# @link [Python Tutorial to build Image to Text App using EasyOCR & Streamlit - YouTube](https://www.youtube.com/watch?v=j7TH0MRlnGs) at 2021/9/13
