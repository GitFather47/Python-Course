import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

#Tensorflow Model Prediction
def model_prediction(test_image):
    image = Image.open(test_image)
    image = image.resize((128, 128))
    image = np.array(image) / 255.0  # Normalize pixel values to the range [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    model = tf.keras.models.load_model("plant_model.keras")
    predictions = model.predict(image)
    return np.argmax(predictions)  # Return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Diagnosis"])

#Main Page
if(app_mode=="Home"):
    st.markdown("<div style='text-align:center'><h1 style='font-family:Ink Free;'>SNAPLEAF🌿</h1></div>", unsafe_allow_html=True)
  # Centered header with Pricedown font
    image_path = "home_page.png"
    st.image(image_path,use_column_width=True)

    st.markdown("""
        Welcome to SnapLeaf: Plant Disease Diagnosis System! 🔍
        
        Our objective is to efficiently diagnose plant diseases. Upload an image of a plant, and our system will analyze it to identify any signs of diseases. Let's protect our crops and ensure a healthier harvest together!

        ### How It Works
        1. **Upload Image:** Navigate to the **Disease Diagnosis** section and upload an image of a plant suspected of having diseases.
        2. **Analysis:** Our system will employ advanced algorithms and cnn machine learning model to process the image and diagnose potential diseases.
        3. **Results:** Check out the diagnosis and recommendations for further steps, including medication prescriptions based on the identified disease.

        ### Why Choose Us?
        - **Accuracy:** We utilize cutting-edge machine learning techniques for precise disease diagnosis.
        - **User-Friendly:** Our interface is straightforward and intuitive, ensuring a seamless user experience.
        - **Speed and Efficiency:** Get results within seconds, enabling quick decision-making.

        ### Getting Started
        Click on the **Disease Diagnosis** section in the sidebar to upload an image and experience the effectiveness of our Plant Disease Diagnosis System!

        ### About Us
        Learn more about the project, our team, and our goals on the **About** page.
        """)


#About Project
elif(app_mode=="About"):
    st.markdown("<div style='text-align:center'><h1 style='font-family:Ink Free;'>About</h1></div>", unsafe_allow_html=True)
    st.markdown("""
               ### Dataset Overview
               This dataset has been generated through offline augmentation techniques
               based on an original dataset available in Kaggle(https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
               .It comprises approximately 87,000 RGB images depicting both healthy and diseased crop leaves,
               organized into 38 distinct categories. The dataset is partitioned into training and validation sets
               in an 80/20 ratio while maintaining the directory structure. Additionally, a separate directory containing
               33 test images has been created for prediction purposes.

                #### Composition
                1. Training set: 70,295 images
                2. Test set: 33 images
                3. Validation set: 17,572 images
                
                #### List of Diseases
                - Apple___Apple_scab
                - Apple___Black_rot
                - Apple___Cedar_apple_rust
                - Apple___healthy
                - Blueberry___healthy
                - Cherry_(including_sour)___Powdery_mildew
                - Cherry_(including_sour)___healthy
                - Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot
                - Corn_(maize)___Common_rust_
                - Corn_(maize)___Northern_Leaf_Blight
                - Corn_(maize)___healthy
                - Grape___Black_rot
                - Grape___Esca_(Black_Measles)
                - Grape___Leaf_blight_(Isariopsis_Leaf_Spot)
                - Grape___healthy
                - Orange___Haunglongbing_(Citrus_greening)
                - Peach___Bacterial_spot
                - Peach___healthy
                - Pepper,_bell___Bacterial_spot
                - Pepper,_bell___healthy
                - Potato___Early_blight
                - Potato___Late_blight
                - Potato___healthy
                - Raspberry___healthy
                - Soybean___healthy
                - Squash___Powdery_mildew
                - Strawberry___Leaf_scorch
                - Strawberry___healthy
                - Tomato___Bacterial_spot
                - Tomato___Early_blight
                - Tomato___Late_blight
                - Tomato___Leaf_Mold
                - Tomato___Septoria_leaf_spot
                - Tomato___Spider_mites Two-spotted_spider_mite
                - Tomato___Target_Spot
                - Tomato___Tomato_Yellow_Leaf_Curl_Virus
                - Tomato___Tomato_mosaic_virus
                - Tomato___healthy

                
                #### Credits:
                Arnob Aich Anurag
                
                Research Intern at AMIR Lab (Advanced Machine Intelligence Research Lab)
                
                Student at American International University Bangladesh
                
                Dhaka,Bangladesh
                
                Email:  openworld41@gmail.com


                """)

elif app_mode == "Disease Diagnosis":
    st.markdown("<div style='text-align:center'><h1 style='font-family:Ink Free;'>Disease Diagnosis:Your Plant doctor is here</h1></div>", unsafe_allow_html=True)
    test_image = st.file_uploader("Choose an Image:")

    show_image_clicked = False  # Variable to track if "Show Image" button is clicked

    if st.button("Show Image"):
        show_image_clicked = True  # Set the variable to True when "Show Image" is clicked
        if test_image is not None:
            st.image(test_image, width=400, use_column_width=True)
        else:
            st.warning("No image found.")

    # Predict button
    if st.button("Predict"):
        st.snow()
        st.write("Our Prediction")
        if test_image is not None:
            result_index = model_prediction(test_image)
            class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                          'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
                          'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                          'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
                          'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                          'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                          'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
                          'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
                          'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
                          'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
                          'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
                          'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
                          'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                          'Tomato___healthy']
            medicine_dict = {
                    'Apple___Apple_scab': '**Treatment:** Apply fungicides containing copper or sulfur. **Preventative measures:** Prune diseased branches and fallen leaves, improve air circulation.',
                    'Apple___Black_rot': '**Treatment:** Apply fungicides containing chlorothalonil or copper. Prune and remove infected areas. **Preventative measures:** Avoid overhead watering, space plants for good air circulation.',
                    'Apple___Cedar_apple_rust': '**Treatment:** Apply fungicides containing tebuconazole or propiconazole. Remove cedar trees (alternate host) if feasible. **Preventative measures:** Plant resistant apple varieties.',
                    'Apple___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Blueberry___healthy': 'Maintain good irrigation and nutrition practices.',
                    'Cherry_(including_sour)___Powdery_mildew': '**Treatment:** Apply fungicides containing sulfur or neem oil. Improve air circulation by pruning and spacing plants. **Preventative measures:** Water at the base of the plant, avoid overhead watering.',
                    'Cherry_(including_sour)___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': '**Treatment:** Apply fungicides containing azoxystrobin or chlorothalonil. Practice crop rotation with non-susceptible crops.',
                    'Corn_(maize)___Common_rust_': '**Treatment:** Apply fungicides containing propiconazole or triticonazole. Plant resistant corn varieties if available.',
                    'Corn_(maize)___Northern_Leaf_Blight': '**Treatment:** Apply fungicides containing strobilurins or azoxystrobin. Remove infected debris like stalks and leaves.',
                    'Corn_(maize)___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Grape___Black_rot': '**Treatment:** Apply fungicides containing copper or strobilurins. Prune and remove infected vines.',
                    'Grape___Esca_(Black_Measles)': '**Treatment:** There is no cure, but fungicides containing copper may help suppress further spread. Practice proper vineyard hygiene by removing infected canes and debris.',
                    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': '**Treatment:** Apply fungicides containing copper or strobilurins. Improve air circulation by pruning and canopy management.',
                    'Grape___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Orange___Haunglongbing_(Citrus_greening)': '**Treatment:** There is no cure. Remove and destroy infected trees to prevent further spread.',
                    'Peach___Bacterial_spot': '**Treatment:** Apply copper-based bactericides. Prune and remove infected branches.',
                    'Peach___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Pepper,_bell___Bacterial_spot': '**Treatment:** Unfortunately, there is no effective control after infection. Remove infected plants to prevent further spread.',
                    'Pepper,_bell___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Potato___Early_blight': '**Treatment:** Apply fungicides containing chlorothalonil or copper. Practice crop rotation with non-susceptible crops.',
                    'Potato___Late_blight': '**Treatment:** Apply fungicides containing chlorothalonil or metalaxyl. Remove infected foliage to prevent further spread.',
                    'Potato___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Raspberry___healthy': 'Maintain good irrigation and nutrition practices.',
                    'Soybean___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Squash___Powdery_mildew': '**Treatment:** Apply fungicides containing sulfur or neem oil. Improve air circulation by pruning and spacing plants.',
                    'Strawberry___Leaf_scorch': '**Treatment:** Apply fungicides containing copper. Remove infected leaves.',
                    'Strawberry___healthy': 'No specific medicine needed. Ensure proper care like watering, sunlight, and fertilization.',
                    'Tomato___Bacterial_spot': '**Treatment:** Apply copper-based bactericides. Remove infected plants to prevent further spread.',
                    'Tomato___Early_blight': '**Treatment:** Apply fungicides containing chlorothalonil or copper. Prune affected areas to improve air circulation.',
                    'Tomato___Late_blight': '**Treatment:** Apply fungicides containing chlorothalonil or metalaxyl. Remove infected foliage to prevent further spread.',
                    'Tomato___Leaf_Mold': '**Treatment:** Improve air circulation by pruning and spacing plants. In severe cases, apply fungicides containing copper or neem oil.',
                    'Tomato___Septoria_leaf_spot': '**Treatment:** Apply fungicides containing chlorothalonil or copper. Remove infected leaves to prevent further spread. Practice crop rotation.',
                    'Tomato___Spider_mites Two-spotted_spider_mite': '**Treatment:** Apply miticides or insecticidal soap. Increase humidity around plants.',
                    'Tomato___Target_Spot': '**Treatment:** Apply fungicides containing copper or strobilurins. Practice crop rotation with non-susceptible crops.',
                    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': '**Treatment:** No cure available. Remove infected plants to prevent further spread. Practice preventative measures like insect control to avoid transmission by whiteflies.',
                    'Tomato___Tomato_mosaic_virus': '**Treatment:** No cure available. Remove infected plants to prevent further spread. Practice preventative measures like weed control to avoid transmission by aphids.'
                }
  

            predicted_disease = class_name[result_index]
            st.success("Model is Predicting it's a {}".format(predicted_disease))

            # Display medicine recommendation if available
            if predicted_disease in medicine_dict:
                st.info("Recommended Medicine: {}".format(medicine_dict[predicted_disease]))
            else:
                st.warning("No medicine recommendation available for this disease.")
        else:
            st.warning("No image found.")  # Display this message if "Show Image" was clicked but no image was selected