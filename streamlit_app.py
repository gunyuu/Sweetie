import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Dessert Match", page_icon="🍰")
st.title("🍩 What Dessert Matches Your Personality?")

st.write("Tell us about your personality and we’ll match you with a dessert that fits your vibe.")

# Personality input
personality = st.text_area("Describe your personality (e.g., adventurous, calm, romantic, creative):", "")

# Preference input
flavor = st.selectbox("Pick your favorite flavor:", ["Chocolate", "Vanilla", "Fruity", "Nutty", "Spicy", "Citrusy", "Creamy"])

# Mood input
mood = st.selectbox("What’s your current mood?", ["Happy", "Focused", "Lazy", "Romantic", "Stressed", "Excited"])

if st.button("Find My Dessert Match 🍨") and personality:
    with st.spinner("Thinking..."):
        prompt = f"""
        Based on the following personality and preferences, suggest one dessert or cake that matches this person.
        Include the name, a short description, and why it fits their personality.

        Personality: {personality}
        Flavor preference: {flavor}
        Current mood: {mood}

        Be fun and a little poetic.
        """
        response = model.generate_content(prompt)
        st.subheader("🎂 Your Dessert Match:")
        st.write(response.text)
else:
    st.info("Fill in your personality details and click the button to get started!")
