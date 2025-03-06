import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Student Portfolio", page_icon="🎓")

# Custom CSS for animations
st.markdown("""
<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fade-in {
    animation: fadeIn 1s ease-in;
}

.project-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    padding: 20px;
    border-radius: 10px;
    background-color: #f9f9f9;
    margin: 10px 0;
}

.project-card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
""", unsafe_allow_html=True)

# Add AOS library for scroll animations
st.markdown("""
<link href="https://cdn.rawgit.com/michalsnik/aos/2.1.1/dist/aos.css" rel="stylesheet">
<script src="https://cdn.rawgit.com/michalsnik/aos/2.1.1/dist/aos.js"></script>
<script>
    AOS.init();
</script>
<style>
    [data-aos] {
        opacity: 0;
        transition-property: opacity;
    }

    [data-aos].aos-animate {
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Testimonials", "Timeline", "Settings", "Contact"])

# Home section
if page == "Home":
    st.title("🎓 Student Portfolio")

    # Profile image
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="Uploaded image")
    else:
        st.image("profile.jpg", width=150, caption="Default image")

    # Student details (Editable!)
    name = st.text_input("Name: ", "Henry Allison.")
    location = st.text_input("Location: ", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study: ", "Computer Science, SWE")
    university = st.text_input("University: ", "INES - Ruhengeri")

    st.write(f"📍 {location}")
    st.write(f"📚 {field_of_study}")
    st.write(f"🎓 {university}")

    # Resume download button
    with open("resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")

    st.markdown("---")
    st.subheader("About Me")
    about_me = st.text_area("Short introduction about myself:", "I'm currently a student at INES Ruhengeri. I am someone who is very hardworking and focus in life. I have "
                "have a very good knowledge when it comes to software engineering. I also have a good programing knowledge"
                                                                " in many programing language."
            " I'm also a problem solver by default. I also follow good Software engineering practices at all time ")
    st.write(about_me)

# Projects section
elif page == "Projects":
    st.title("💻 My Projects")

    # Project filtering system
    st.subheader("Filter Projects")
    project_filter = st.selectbox("Filter by:", ["All", "Year 1", "Year 2", "Year 3", "Dissertation"])

    if project_filter == "All" or project_filter == "Year 1":
        with st.expander("📊 Simple Calculator"):
            st.write("This project focuses on the creation of a simple calculator which can be use to perform addition, substation, multiplication, and division")
            st.write("**Technologies Used: C programing")
            st.write("[🔗 GitHub Repo](https://github.com/henryallison/crop-disease-prediction)")

        with st.expander("📊 Mobile Money System"):
            st.write("This system focuses on devloping of a system which simulates those activities that are conduct in a real world mobile money system")
            st.write("**Technologies Used: C programing")
            st.write("[🔗 GitHub Repo](https://github.com/henryallison/crop-disease-prediction)")
            st.write("📧 Email: hyallison5050@gmail.com")
            st.write("[🔗 LinkedIn](https://www.linkedin.com/in/henry-allison-027545337/)")

    if project_filter == "All" or project_filter == "Year 2":
        with st.expander("🏥 Employee Management System"):
            st.write("This system focuses on devloping of a system which helps to manage employees data efficiently")
            st.write("**Technologies Used:** Java")
            st.write("[🔗 GitHub Repo](https://github.com/henryallison/hospital-management)")
            st.write("📧 Email: hyallison5050@gmail.com")
            st.write("[🔗 LinkedIn](https://www.linkedin.com/in/henry-allison-027545337/)")


        with st.expander("🏥 Web based hospital management System"):
            st.write("This system focuses on devloping of a system which helps to manage patients, an doctors day to day data efficiently")
            st.write("**Technologies Used:** html, css, java, javascript, SQL")
            st.write("[🔗 GitHub Repo](https://github.com/henryallison/hospital-management)")
            st.write("📧 Email: hyallison5050@gmail.com")
            st.write("[🔗 LinkedIn](https://www.linkedin.com/in/henry-allison-027545337/)")

    if project_filter == "All" or project_filter == "Year 3":
            with st.expander("📊 Crop (Coffee and Maize) Disease Prediction"):
                    st.write(
                        "This is an AI prediction project developed using Python Flask for prediction and HTML/CSS for the front end. The project predicts crop diseases and recommends appropriate treatments.")
                    st.write("**Technologies Used:** Python, Flask, HTML, CSS")
            with st.expander("🏥 Hospital Management System"):
                    st.write(
                            "Developed a hospital management system to reduce workload pressure and stress for healthcare providers and patients.")
                    st.write("**Technologies Used:** Python, SQL")
                    st.write("[🔗 GitHub Repo](https://github.com/henryallison/crop-disease-prediction)")
                    st.write("📧 Email: hyallison5050@gmail.com")
                    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/henry-allison-027545337/)")

    if project_filter == "All" or project_filter == "Dissertation":
            with st.expander("Designing a Basic Encryption System for Secure Health Data Sharing"):
                st.write("My final year project focuses on developing a light weight encryption system that will be use to keep patient medical records, encrypted at times. Both at rest and in transit ")
                st.write("**Technologies Used:** Python, SQL")
                st.write("[🔗 GitHub Repo](https://github.com/henryallison/ai-chatbot)")
                st.write("📧 Email: hyallison5050@gmail.com")
                st.write("[🔗 LinkedIn](https://www.linkedin.com/in/henry-allison-027545337/)")

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")

    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)

    skill_sql_quires = st.slider("MySQL quires", 0, 100, 95)
    st.progress(skill_sql_quires)

    skill_C_programing = st.slider("C programing", 0, 92, 90)
    st.progress(skill_C_programing)

    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)

    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)

    st.subheader("Certifications & Achievements")
    st.write("✔ Completed AI & ML in Crop disease detection Certification")
    st.write("✔ Certified in programing Python ")

# Testimonials section
elif page == "Testimonials":
    st.title("🗣️ Student Testimonials")

    st.write("Here’s what my classmates and mentors have to say about me:")
    st.markdown("---")

    st.write("Elvis T Harmony")
    st.write("> Henry is a really hardworking person who knows what he wants in life.")

    st.write("Blessing Allison")
    st.write("> Henry is always willing to work with other team player and always delivers high-quality work.")

    st.write("Octave")
    st.write("> Henry’s dedication to learning and improving his skills is inspiring and very motivating.")

# Timeline section
elif page == "Timeline":
    st.title("⏳ Academic & Project Milestones")

    st.write("Here’s a timeline of my key achievements:")
    st.markdown("---")

    st.write("**Year 1**")
    st.write("✅ Completed my first project: Simple Calculator, followed by a simple mobile money system")

    st.write("**Year 2**")
    st.write("🏆 I manage to achieve the creation of one of the best hospital management system with a very beautiful and seamless GUI.")

    st.write("**Year 3**")
    st.write("💼 Here I manage to complete an internship of 2 months at IKIGUGU LTD Company, working on AI-powered chatbots, QR code Scanner attendance system and more AI based system.")

    st.write("Final year dissertation")
    st.write("📖 Here I manage to create a basic encryption system for protecting medical health records at rest and in transit.")

# Settings section
elif page == "Settings":
    st.title("🎨 Customize Your Profile")

    st.subheader("Upload a Profile Picture")
    uploaded_image = st.file_uploader("Choose a file", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150)

    st.subheader("✍ Edit Personal Info")
    new_name = st.text_input("Update Name: ", "Henry Allison")
    new_location = st.text_input("Update Location: ", "Musanze, Rwanda")
    new_field = st.text_input("Update Field of Study: ", "Computer Science, SWE")
    new_university = st.text_input("Update University: ", "INES - Ruhengeri")

# Contact section
elif page == "Contact":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Enter your Name")
        email = st.text_input("Enter your Email")
        message = st.text_area("Enter your Message")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully")

    st.write("📧 Email: hyallison5050@gmail.com")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/henry-allison-027545337/)")
    st.write("[📂 GitHub](https://github.com/henryallison)")


# Footer
st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ using Streamlit")
