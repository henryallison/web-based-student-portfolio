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
    if "profile_image" in st.session_state and st.session_state.profile_image is not None:
        st.image(st.session_state.profile_image, width=150, caption="Profile Picture")
    else:
        st.image("profile.jpg", width=150, caption="Default Image")

    # Student details (Editable!)
    name = st.session_state.get("name", "Henry Allison")
    location = st.session_state.get("location", "Musanze, Rwanda")
    field_of_study = st.session_state.get("field_of_study", "Computer Science, SWE")
    university = st.session_state.get("university", "INES - Ruhengeri")

    # Display user details
    st.write(f"**👤 Name:** {name}")
    st.write(f"**📍 Location:** {location}")
    st.write(f"**📚 Field of Study:** {field_of_study}")
    st.write(f"**🎓 University:** {university}")

    # Resume download button
    cv_file = st.session_state.get("cv", "resume.pdf")
    with open(cv_file, "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="📄 Download Resume", data=resume_bytes, file_name=cv_file, mime="application/pdf")

    st.markdown("---")
    st.subheader("About Me")

    # About me section
    about_me = st.session_state.get("bio", (
        "I'm currently a student at INES Ruhengeri. I am someone who is very hardworking and focused in life. "
        "I have a very good knowledge when it comes to software engineering. I also have strong programming skills "
        "in multiple programming languages. I'm a problem solver by default and always follow good software engineering practices."
    ))

    # Display the about me section
    st.write(about_me)


# Projects section
elif page == "Projects":
    st.title("💻 My Projects")

    # Project filtering system
    st.subheader("Filter Projects")
    project_filter = st.selectbox("Filter by:", ["All", "Year 1", "Year 2", "Year 3", "Dissertation"])

    if project_filter == "All" or project_filter == "Year 1":
        with st.expander("📊 Simple Calculator(individual Project)"):
            st.write("This project focuses on the creation of a simple calculator which can be use to perform addition, substation, multiplication, and division")
            st.write("**Technologies Used: C programing")
            st.write("[🔗 GitHub Repo](https://github.com/henryallison/simple-calculator.git)")

        with st.expander("📊 Mobile Money System (individual Project)"):
            st.write("This project focuses on devloping of a system which simulates those activities that are conduct in a real world mobile money system")
            st.write("**Technologies Used: C programing")
            st.write("[🔗 GitHub Repo](https://github.com/henryallison/mobile-money-System.git)")


    if project_filter == "All" or project_filter == "Year 2":
        with st.expander("🏥 Employee Management System (Group Project)"):
            st.write("This project focuses on devloping of a system which helps to manage employees data efficiently")
            st.write("**Technologies Used:** Python")
            st.write("[🔗 GitHub Repo](https://github.com/henryallison/employee-management-sys.git)")



        with st.expander("🏥 hospital management System (Group Project)"):
            st.write("This project focuses on devloping of a system which helps to manage patients, an doctors day to day data efficiently")
            st.write("**Technologies Used:** python and, SQL")
            st.write("[🔗 GitHub Repo](https://github.com/henryallison/hospital-sys.git)")


    if project_filter == "All" or project_filter == "Year 3":
            with st.expander("📊 Crop (Coffee and Maize) Disease Prediction(Group Project)"):
                    st.write(
                        "This is an AI prediction project developed using Python Flask for prediction and HTML/CSS for the front end. The project predicts crop diseases and recommends appropriate treatments.")
                    st.write("**Technologies Used:** Python, Flask, HTML, CSS")
                    st.write("[🔗 GitHub Repo](https://github.com/henryallison/-AI_Group1_ExpertSystem_Assignment2.git)")

            with st.expander("🏥 subscription boxes for pet"):
                    st.write(
                            "Developed a web base project on with customer can purchase surprise boxes for their pet")
                    st.write("[🔗 GitHub Repo](https://github.com/henryallison/Subscription-boxes-for-pet.git)")


    if project_filter == "All" or project_filter == "Dissertation":
            with st.expander("Designing a Basic Encryption System for Secure Health Data Sharing"):
                st.write("My final year project focuses on developing a light weight encryption system that will be use to keep patient medical records, encrypted at times. Both at rest and in transit ")
                st.write("**Technologies Used:** Python, SQL")
                st.write("Pending")


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

if "testimonials" not in st.session_state:
    st.session_state.testimonials = []

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

    for testimonial in st.session_state.testimonials:
        st.write(f"**{testimonial['name']}**")
        st.write(f"> {testimonial['message']}")
        st.markdown("---")

        # Form to submit new testimonials
    with st.form("testimonial_form"):
        name = st.text_input("Your Name")
        message = st.text_area("Your Testimonial")
        submitted = st.form_submit_button("Submit Testimonial")

        if submitted:
            if name and message:  # Ensure both fields are filled
                # Add the new testimonial to the session state
                st.session_state.testimonials.append({"name": name, "message": message})
                st.success("✅ Thank you for your testimonial!")
            else:
                st.warning("⚠️ Please fill out both fields.")

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
# Settings section
elif page == "Settings":
    st.title("🎨 Customize Your Profile")

    st.subheader("Upload a Profile Picture")
    uploaded_image = st.file_uploader("Choose a file", type=["jpg", "png"])
    if uploaded_image is not None:
        st.session_state.profile_image = uploaded_image
        st.image(uploaded_image, width=150)

    st.subheader("✍ Edit Personal Info")
    new_name = st.text_input("Update Name: ", st.session_state.get("name", "Henry Allison"))
    new_location = st.text_input("Update Location: ", st.session_state.get("location", "Musanze, Rwanda"))
    new_field = st.text_input("Update Field of Study: ", st.session_state.get("field_of_study", "Computer Science, SWE"))
    new_university = st.text_input("Update University: ", st.session_state.get("university", "INES - Ruhengeri"))

    st.subheader("✍ Update Bio")
    new_bio = st.text_area("Update Bio: ", st.session_state.get("bio", (
        "I'm currently a student at INES Ruhengeri. I am someone who is very hardworking and focused in life. "
        "I have a very good knowledge when it comes to software engineering. I also have strong programming skills "
        "in multiple programming languages. I'm a problem solver by default and always follow good software engineering practices."
    )))

    st.subheader("📄 Upload New CV")
    new_cv = st.file_uploader("Upload CV (PDF)", type=["pdf"])

    # Save changes
    if st.button("Save Changes"):
        st.session_state.name = new_name
        st.session_state.location = new_location
        st.session_state.field_of_study = new_field
        st.session_state.university = new_university
        st.session_state.bio = new_bio
        if new_cv is not None:
            st.session_state.cv = new_cv
        st.success("✅ Changes saved successfully!")

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