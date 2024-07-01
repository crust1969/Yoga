import streamlit as st

# Title of the Web App
st.title('Yoga Training App')

# List of Yoga Exercises with corresponding image URLs
exercises = {
    'Downward Dog': 'user/documents/Downward-Facing-Dog.jpg',
    'Warrior II': 'user/documents/warrior2.jpg',
    'Tree Pose': 'user/documents/treepose.jpg',
    'Child\'s Pose': 'user/documents/childpose.jpg'
}

# Display Yoga Exercises with Images
st.subheader('Yoga Exercises:')
for exercise_name, image_url in exercises.items():
    st.image(image_url, caption=exercise_name, use_column_width=True)
    
# Booking Section
st.subheader('Book Your Yoga Training:')

# Allow user to select three trainings
trainings = st.multiselect('Select Three Trainings:', list(exercises.keys()), default=list(exercises.keys())[:3])

# Display selected trainings
st.write('Your Selected Trainings:')
for training in trainings:
    st.write(f'- {training}')

# Book Button
if st.button('Book Trainings'):
    st.success('Trainings booked successfully!')
