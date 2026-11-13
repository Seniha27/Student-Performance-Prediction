
import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #101426;
    color: #F5F3FF;
}

/* Main Layout */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main Heading */
h1 {
    color: #C4A7FF !important;
    text-align: center;
    font-size: 40px !important;
    font-weight: 800;
}

/* Section Headings */
h2, h3 {
    color: #C4A7FF !important;
    font-weight: 700;
}

/* Normal Text */
p, label {
    color: #E5E1F5 !important;
}

/* KPI Cards */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #252044, #38265F);
    border: 1px solid #7954C8;
    padding: 22px 15px;
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

div[data-testid="stMetricLabel"] {
    color: #C9B8FF !important;
}

div[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-size: 30px;
    font-weight: bold;
}

/* Section Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #202943;
    border: 1px solid #7954C8;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.25);
}

/* Input Fields */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #252044;
    color: white;
    border-radius: 10px;
}

.stNumberInput input {
    background-color: #252044;
    color: white;
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #7045C5, #A16BEB);
    color: white;
    border: none;
    border-radius: 12px;
    height: 52px;
    font-size: 17px;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    background: #8B5CDA;
    color: white;
    border: 1px solid #C4A7FF;
}

/* Prediction Message */
.stAlert {
    background-color: #252044;
    border-radius: 12px;
}

/* Divider */
hr {
    border-color: #40345F;
}

</style>
""", unsafe_allow_html=True)


# Load Model and Preprocessor
model = joblib.load("best_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# Load Dataset
df = pd.read_csv("student-mat.csv", sep=";")


# Main Heading
st.title("🎓 Student Performance Prediction")

st.markdown(
    "<p style='text-align:center;color:#B9B5CE;'>"
    "Machine Learning Based Student Grade Prediction System"
    "</p>",
    unsafe_allow_html=True
)

st.divider()


# KPI Dashboard
st.markdown("## 📊 Student Performance Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Students", len(df))

with col2:
    st.metric("Average Grade", round(df["G3"].mean(), 2))

with col3:
    st.metric("Highest Grade", df["G3"].max())

with col4:
    st.metric("Model R² Score", "0.14")


st.divider()



# Personal Details
with st.container(border=True):

    st.subheader("👤 Personal Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Student's Age",
            min_value=15, max_value=22, value=17,
            key="student_age"
        )

        school_options = {
            "Gabriel Pereira School": "GP",
            "Mousinho da Silveira School": "MS"
        }

        school = school_options[
            st.selectbox(
                "School",
                list(school_options.keys()),
                key="student_school"
            )
        ]

        gender_options = {
            "Female": "F",
            "Male": "M"
        }

        sex = gender_options[
            st.selectbox(
                "Gender",
                list(gender_options.keys()),
                key="student_gender"
            )
        ]

    with col2:
        address_options = {
            "Urban Area": "U",
            "Rural Area": "R"
        }

        address = address_options[
            st.selectbox(
                "Home Location",
                list(address_options.keys()),
                key="home_location"
            )
        ]

        family_options = {
            "3 or Fewer Members": "LE3",
            "More Than 3 Members": "GT3"
        }

        famsize = family_options[
            st.selectbox(
                "Family Size",
                list(family_options.keys()),
                key="family_size"
            )
        ]

        parent_options = {
            "Living Together": "T",
            "Living Apart": "A"
        }

        Pstatus = parent_options[
            st.selectbox(
                "Parents' Living Arrangement",
                list(parent_options.keys()),
                key="parent_status"
            )
        ]


# Family and Education
with st.container(border=True):

    st.subheader("📚 Family & Education Details")

    col1, col2 = st.columns(2)

    education_options = {
        "No Education": 0,
        "Primary Education (Up to 4th Grade)": 1,
        "5th to 9th Grade": 2,
        "Secondary Education": 3,
        "Higher Education": 4
    }

    job_options = {
        "Teacher": "teacher",
        "Healthcare": "health",
        "Services": "services",
        "Staying at Home": "at_home",
        "Other": "other"
    }

    reason_options = {
        "Near Home": "home",
        "Good School Reputation": "reputation",
        "Preferred Course": "course",
        "Other": "other"
    }

    guardian_options = {
        "Mother": "mother",
        "Father": "father",
        "Other": "other"
    }

    travel_options = {
        "Less than 15 minutes": 1,
        "15 to 30 minutes": 2,
        "30 minutes to 1 hour": 3,
        "More than 1 hour": 4
    }

    with col1:

        Medu = education_options[
            st.selectbox(
                "Mother's Education",
                list(education_options.keys()),
                key="mother_education"
            )
        ]

        Mjob = job_options[
            st.selectbox(
                "Mother's Job",
                list(job_options.keys()),
                key="mother_job"
            )
        ]

        reason = reason_options[
            st.selectbox(
                "Reason for Choosing School",
                list(reason_options.keys()),
                key="school_reason"
            )
        ]

        guardian = guardian_options[
            st.selectbox(
                "Student's Guardian",
                list(guardian_options.keys()),
                key="student_guardian"
            )
        ]

    with col2:

        Fedu = education_options[
            st.selectbox(
                "Father's Education",
                list(education_options.keys()),
                key="father_education"
            )
        ]

        Fjob = job_options[
            st.selectbox(
                "Father's Job",
                list(job_options.keys()),
                key="father_job"
            )
        ]

        traveltime = travel_options[
            st.selectbox(
                "Travel Time to School",
                list(travel_options.keys()),
                key="school_travel_time"
            )
        ]


# Academic Details
with st.container(border=True):

    st.subheader("📖 Academic Details")

    col1, col2, col3 = st.columns(3)

    studytime_options = {
        "Less than 2 hours": 1,
        "2 to 5 hours": 2,
        "5 to 10 hours": 3,
        "More than 10 hours": 4
    }

    failure_options = {
        "No Previous Failures": 0,
        "1 Previous Failure": 1,
        "2 Previous Failures": 2,
        "3 or More Previous Failures": 3
    }

    with col1:
        studytime = studytime_options[
            st.selectbox(
                "Weekly Study Time",
                list(studytime_options.keys()),
                key="weekly_study_time"
            )
        ]

    with col2:
        failures = failure_options[
            st.selectbox(
                "Number of Past Class Failures",
                list(failure_options.keys()),
                key="past_failures"
            )
        ]

    with col3:
        absences = st.number_input(
            "Number of School Absences",
            min_value=0,
            max_value=100,
            value=0,
            key="school_absences"
        )



# Activities and Support
with st.container(border=True):

    st.subheader("✨ Student Activities & Support")

    col1, col2 = st.columns(2)

    yes_no_options = {
        "Yes": "yes",
        "No": "no"
    }

    with col1:

        schoolsup = yes_no_options[
            st.selectbox(
                "Does the Student Receive Extra Educational Support?",
                list(yes_no_options.keys()),
                key="school_support"
            )
        ]

        famsup = yes_no_options[
            st.selectbox(
                "Does the Family Provide Educational Support?",
                list(yes_no_options.keys()),
                key="family_support"
            )
        ]

        paid = yes_no_options[
            st.selectbox(
                "Attends Extra Paid Classes?",
                list(yes_no_options.keys()),
                key="paid_classes"
            )
        ]

        activities = yes_no_options[
            st.selectbox(
                "Participates in Extracurricular Activities?",
                list(yes_no_options.keys()),
                key="extra_activities"
            )
        ]

    with col2:

        nursery = yes_no_options[
            st.selectbox(
                "Attended Nursery School?",
                list(yes_no_options.keys()),
                key="nursery_school"
            )
        ]

        higher = yes_no_options[
            st.selectbox(
                "Wants to Pursue Higher Education?",
                list(yes_no_options.keys()),
                key="higher_education"
            )
        ]

        internet = yes_no_options[
            st.selectbox(
                "Has Internet Access at Home?",
                list(yes_no_options.keys()),
                key="home_internet"
            )
        ]

        romantic = yes_no_options[
            st.selectbox(
                "Is Currently in a Romantic Relationship?",
                list(yes_no_options.keys()),
                key="romantic_relationship"
            )
        ]


# Lifestyle and Health
with st.container(border=True):

    st.subheader("💜 Lifestyle & Health Details")

    col1, col2 = st.columns(2)

    rating_options = {
        "Very Low (1)": 1,
        "Low (2)": 2,
        "Moderate (3)": 3,
        "High (4)": 4,
        "Very High (5)": 5
    }

    quality_options = {
        "Very Poor (1)": 1,
        "Poor (2)": 2,
        "Average (3)": 3,
        "Good (4)": 4,
        "Excellent (5)": 5
    }

    with col1:

        famrel = quality_options[
            st.selectbox(
                "How is the Relationship with Family?",
                list(quality_options.keys()),
                key="family_relationship"
            )
        ]

        freetime = rating_options[
            st.selectbox(
                "How Much Free Time Does the Student Have?",
                list(rating_options.keys()),
                key="free_time"
            )
        ]

        goout = rating_options[
            st.selectbox(
                "How Often Does the Student Go Out with Friends?",
                list(rating_options.keys()),
                key="going_out"
            )
        ]

    with col2:

        Dalc = rating_options[
            st.selectbox(
                "Workday Alcohol Consumption Level",
                list(rating_options.keys()),
                key="workday_alcohol"
            )
        ]

        Walc = rating_options[
            st.selectbox(
                "Weekend Alcohol Consumption Level",
                list(rating_options.keys()),
                key="weekend_alcohol"
            )
        ]

        health = rating_options[
            st.selectbox(
                "How Would the Student Rate Their Health?",
                list(rating_options.keys()),
                key="health_status"
            )
        ]

# Prediction Section
st.divider()

with st.container(border=True):

    st.subheader("🚀 Predict Student Performance")

    st.write(
        "Enter the student details above and click below "
        "to predict the final grade."
    )

    if st.button("Predict Final Grade"):

        input_data = {
            'school': school,
            'sex': sex,
            'age': age,
            'address': address,
            'famsize': famsize,
            'Pstatus': Pstatus,
            'Medu': Medu,
            'Fedu': Fedu,
            'Mjob': Mjob,
            'Fjob': Fjob,
            'reason': reason,
            'guardian': guardian,
            'traveltime': traveltime,
            'studytime': studytime,
            'failures': failures,
            'schoolsup': schoolsup,
            'famsup': famsup,
            'paid': paid,
            'activities': activities,
            'nursery': nursery,
            'higher': higher,
            'internet': internet,
            'romantic': romantic,
            'famrel': famrel,
            'freetime': freetime,
            'goout': goout,
            'Dalc': Dalc,
            'Walc': Walc,
            'health': health,
            'absences': absences
        }

        input_df = pd.DataFrame([input_data])

        processed_data = preprocessor.transform(input_df)

        prediction = model.predict(processed_data)

        st.success(
            f"🎓 Predicted Final Grade: {prediction[0]:.2f} / 20"
        )


# Footer
st.divider()

st.markdown(
    "<p style='text-align:center;color:#AFA4CC;'>"
    "Student Performance Prediction | Machine Learning Project"
    "</p>",
    unsafe_allow_html=True
)
