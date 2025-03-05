import streamlit as st

#Set page title and icon

st.set_page_config(page_title="Student Portfolio",page_icon="🎓")

#Sidebar navigation

st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:",
	   ["Home","Projects","Skills","Settings","Contact"])
#Home section

if page =="Home":
	st.title("🎓 Student Portfolio")

	#Profile image
	uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg","png"])
	if uploaded_image is not None:
		st.image(uploaded_image, width=150, caption="Uploaded image")
	else:
		st.image("person.png", width=150, caption="Default image")
	#Student details (Editable!)
	name = st.text_input("Name: ", "Henry Allison")
	location = st.text_input("Location: ", "Musanze,Rwanda")
	field_of_study = st.text_input("Field of Study: ",
	                               "Computer Science, SWE")
	university = st.text_input("University: ", "INES - Ruhengeri")

	st.write(f"📍{location}")
	st.write(f"📚{field_of_study}")
	st.write(f"🎓{university}")

	# Resume download button
	with open("resume.pdf", "rb") as file:
		resume_bytes = file.read()
	st.download_button(label="📄Download Resume",
		data=resume_bytes,file_name="resume.pdf",
		mime="application/pdf")

	st.markdown("---")
	st.subheader("About Me")
	about_me = st.text_area("Short introduction about myself:",
		"I am a passionate AI look forward engineer!")
	st.write(about_me)

#Projects section
elif page =="Projects":
	st.title("💻 My Projects")

	with st.expander("📊 Crop(coffee and Maize) disease prediction"):
		st.write("This is an AI prediction project developed using python flask for prediction and html and css for front end. This AI project followed some predefined rules in order to make crop "
				 "predictions and recommend appropriate treatment. The end user firstly select a type of crop."
				 "Next they select a type of common symptom that they think they are seeing in the crop."
				 "Based on their previous choices made by the user, the system will made a prediction of the disease and then"
				 " also recommend a treatment or a solution")

	with st.expander("🏥 Hospital Management System"):
		st.write("Developed a hospital management systemt that releases the workload pressure and stress  that healthcare providers and patients"
				 " usually undergoes regular")



elif page =="Skills":
	st.title("⚡ Skills and Achievements")

	st.subheader("Programming Skills")
	skill_python = st.slider("Python",0,100,90)
	st.progress(skill_python)

	skill_js = st.slider("JavaScript",0,100,75)
	st.progress(skill_js)
	skill_AI = st.slider("Artificial Intelligence",0,100,65)
	st.progress(skill_AI)

	st.subheader("Certifications & Achievements")
	st.write("✔ Completed AI&ML in Business Certification")
	st.write("✔ Certified AI in Research and Course Preparation for Education")

elif page == "Settings":
	st.title("🎨 Customize your profile")

	st.subheader("Upload a Profile Picture")
	uploaded_image = st.file_uploader("Choose a file", type=["jpg","png"])
	if uploaded_image:
		st.image(uploaded_image, width=150)

	st.subheader("✍ Edit Personal Info")

elif page =="Contact":
	st.title("📬 Contact Me")

	with st.form("contact_form"):
		name = st.text_input("Your Name")
		email = st.text_input("Your Email")
		message=st.text_area("Your message")

		submitted = st.form_submit_button("Send Message")
		if submitted:
			st.success("✅ Message sent successfully")

		st.write("📧 Email: hyallison5050@gmail.com")
		st.write("[🔗LinkedIn](https://www.linkedin.com/in/henry-allison-027545337/)")
		st.write("[📂GitHub](https://github.com/henryallison)")

	st.sidebar.write("---")
	st.sidebar.write("🔹 Made with ❤ using My Watermelon")