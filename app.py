from openai import OpenAI
import openai
from PIL import Image
import streamlit as st
from streamlit_carousel import carousel
from apikey import apikey

#Initialize your image generation client
client=OpenAI(api_key=apikey)

single_img=dict(
    title="",
    text="",
    interval=None,
    img=""
)

def generate_images(image_description, num_images):
    # images=[]
    image_gallery=[]
    for i in range(num_images):
        img_response=client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1
            
        )
        
        image_url=img_response.data[0].url
        # images.append(image_url)
        new_image=single_img.copy()
        new_image["title"]=f"Image {i+1}"
        new_image["text"]=image_description
        new_image["img"]=image_url
        image_gallery.append(new_image)
    return image_gallery

st.set_page_config(page_title="AI_Image_Generator",page_icon=":camera:", layout="wide")

st.title("AI Image Generation Tool")

st.subheader("POWERED BY The World's Most Powerful Image Generator API-DALL-E")
img_description=st.text_input("Enter the description for the image you want to generte")
num_of_images= st.number_input("Select the number of images you want to generate", min_value=1, max_value=10, value=1)

#Create a button

if st.button("Generate Images"):
    generate_image=generate_images(img_description, num_of_images)
    # st.write(generate_image)
    carousel(items=generate_image, width=1)
    # for i in range(len(generate_image)):
    #     st.image(generate_image[i])