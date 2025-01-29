import streamlit as st

# Define some basic responses related to Planview EPPM
planview_faq = {
    "What is Planview EPPM?": "Planview EPPM (Enterprise Project Portfolio Management) is a solution that helps organizations manage their projects, resources, and portfolios effectively.",
    "How does Planview help in project management?": "Planview EPPM provides tools for planning, tracking, and optimizing resources, budgets, and project schedules in a unified platform.",
    "Can I integrate Planview EPPM with other tools?": "Yes, Planview EPPM supports integrations with various tools such as Microsoft Project, Jira, and others through APIs.",
    "What are the key features of Planview EPPM?": "Some key features include resource management, portfolio management, project tracking, time tracking, and financial management.",
    "How do I access Planview EPPM?": "Planview EPPM is a cloud-based solution. You can access it via your web browser or through the Planview mobile app.",
    "Is Planview EPPM suitable for small businesses?": "Planview EPPM is ideal for medium to large organizations with complex project management needs. For smaller teams, Planview offers other tools like Planview LeanKit or Planview Spigit."
}

# Function to get a response from the FAQ based on user input
def get_response(user_input):
    return planview_faq.get(user_input, "Sorry, I don't have an answer for that. Can you please rephrase your question?")

# Streamlit UI Setup
st.title("Planview EPPM Chatbot")
st.write("Ask me anything related to Planview EPPM!")

# User input
user_input = st.text_input("You: ", "")

# If the user enters a question
if user_input:
    response = get_response(user_input)
    st.write("Chatbot: " + response)
