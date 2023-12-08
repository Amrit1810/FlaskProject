import numpy as np
import random
import pycountry
import calendar
import hashlib

def create_sample_dataset():
    
    # Male Names
    rand_male_names = [
        "Alexander Smith", "Benjamin Johnson", "Caleb Davis", "Daniel Williams", "Elijah Brown", "Felix Moore",
        "Gabriel Anderson", "Henry Taylor", "Isaac Martinez", "Jack Thomas", "Kevin Jackson", "Liam White",
        "Mason Harris", "Noah Clark", "Oliver Lewis", "Peter Hall", "Quinn Lee", "Ryan Turner", "Samuel Martin",
        "Theodore Garcia", "Ulysses Rodriguez", "Victor Martinez", "William Davis", "Xavier Anderson",
        "Yannick Taylor", "Zachary Thompson", "Adrian Wilson", "Brandon Hall", "Christopher Garcia",
        "Dominic Thomas", "Ethan Miller", "Franklin Davis", "Gavin Smith", "Harrison Johnson", "Ivan Anderson",
        "Jackson Taylor", "Kenneth Wilson", "Lucas Brown", "Maxwell Martinez", "Nathaniel Davis", "Oscar Miller",
        "Patrick Smith", "Quentin Anderson", "Raymond Taylor", "Sebastian Wilson", "Tristan Harris",
        "Upton Smith", "Vincent Davis", "Wesley Thomas", "Xavier Martinez", "Yosef Johnson", "Zachariah Anderson",
        "Anderson Johnson", "Brody Taylor", "Carter Martinez", "Dorian Smith", "Emerson Davis", "Finnegan Wilson",
        "Gideon Harris", "Harrison Smith", "Ian Anderson", "Jaxon Taylor", "Kellan Wilson", "Landon Davis",
        "Miles Martinez", "Nolan Harris", "Owen Smith", "Preston Johnson", "Quinlan Anderson", "Rhys Taylor",
        "Sawyer Wilson", "Tucker Harris", "Ulysses Smith", "Vaughn Davis", "Wyatt Thomas", "Xander Martinez",
        "Yannick Johnson", "Zane Anderson", "Atticus Taylor", "Beckett Wilson", "Callum Harris", "Declan Smith",
        "Ezekiel Davis", "Fabian Martinez", "Garrett Johnson", "Holden Anderson", "Ignatius Taylor", "Jasper Wilson",
        "Kieran Harris", "Leon Smith", "Magnus Johnson", "Nico Anderson", "Orion Taylor", "Paxton Wilson",
        "Quentin Davis", "Rylan Smith", "Silas Johnson", "Thaddeus Anderson", "Uriah Taylor", "Vance Wilson"
    ]

    # Female Names
    rand_female_names = [
        "Abigail Smith", "Bella Johnson", "Chloe Davis", "Daisy Williams", "Emma Brown", "Fiona Moore",
        "Grace Anderson", "Harper Taylor", "Isabella Martinez", "Jade Thomas", "Kylie Jackson", "Lily White",
        "Mia Harris", "Nora Clark", "Olivia Lewis", "Penelope Hall", "Quinn Lee", "Riley Turner", "Sophia Martin",
        "Taylor Garcia", "Victoria Rodriguez", "Willow Martinez", "Ximena Davis", "Yara Miller", "Zoey Smith",
        "Addison Johnson", "Brianna Taylor", "Charlotte Wilson", "Delilah Anderson", "Emily Wilson", "Faith Harris",
        "Gabriella Smith", "Hailey Johnson", "Isla Anderson", "Juliet Taylor", "Kayla Wilson", "Lily Davis",
        "Mackenzie Martinez", "Natalie Harris", "Olivia Smith", "Piper Johnson", "Quinn Anderson", "Rose Taylor",
        "Scarlett Wilson", "Trinity Harris", "Ulyssa Smith", "Violet Davis", "Willow Thomas", "Xandra Martinez",
        "Yasmine Johnson", "Zara Anderson", "Aurora Taylor", "Bella Wilson", "Cassidy Harris", "Daphne Smith",
        "Eloise Johnson", "Freya Taylor", "Genevieve Harris", "Hazel Smith", "Ivy Johnson", "Juliette Taylor",
        "Kendall Wilson", "Lila Harris", "Madeline Smith", "Naomi Johnson", "Ophelia Anderson", "Paisley Taylor",
        "Quinn Wilson", "Rosalind Harris", "Seraphina Smith", "Tessa Johnson", "Ulla Anderson", "Veda Taylor",
        "Wren Harris", "Xyla Smith", "Yara Johnson", "Zara Anderson", "Amara Taylor", "Bianca Wilson",
        "Cadence Harris", "Dahlia Smith", "Esme Johnson", "Felicity Wilson", "Genevieve Harris", "Harper Smith",
        "Isla Johnson", "Jocelyn Harris", "Kira Smith", "Luna Johnson", "Mabel Taylor", "Nova Davis", "Orla Smith",
        "Phoebe Johnson", "Quinn Harris", "Rhiannon Smith", "Savannah Johnson", "Talia Harris", "Ulyana Smith",
        "Vanessa Johnson", "Willow Taylor"
    ]

    # Industrial Designations
    industrial_designations = [
        "Mechanical Engineer", "Electrical Engineer", "Chemical Engineer", "Civil Engineer", "Industrial Engineer",
        "Process Engineer", "Quality Assurance Engineer", "Manufacturing Engineer", "Production Manager", "Operations Manager",
        "Project Manager", "Maintenance Supervisor", "Automation Engineer", "Safety Officer", "Environmental Engineer",
        "Materials Engineer", "Reliability Engineer", "Research and Development Engineer", "Supply Chain Manager",
        "Logistics Coordinator", "Lean Manufacturing Specialist", "Six Sigma Black Belt", "Product Development Manager",
        "CAD Designer (Computer-Aided Design)", "CNC Machinist (Computer Numerical Control)", "Tooling Engineer",
        "Systems Engineer", "Robotics Engineer", "Packaging Engineer", "Ergonomics Specialist", "Facilities Manager",
        "Technical Writer", "Industrial Designer", "Process Control Engineer", "Maintenance Engineer", "Energy Efficiency Engineer",
        "Quality Control Inspector", "Reliability Manager", "Production Planner", "Continuous Improvement Manager",
        "Operations Analyst", "Automation Technician", "Technical Support Engineer", "Industrial Hygienist",
        "Field Service Engineer", "Product Designer", "Regulatory Affairs Manager", "Instrumentation Engineer",
        "Validation Engineer", "Aerospace Engineer", "Safety Manager", "Plant Manager", "HVAC Engineer (Heating, Ventilation, and Air Conditioning)",
        "Research Scientist", "Manufacturing Technician", "Instrumentation Technician", "Industrial Electrician",
        "Welding Engineer", "Calibration Technician", "Industrial Maintenance Mechanic", "Technical Sales Engineer",
        "Biomedical Engineer", "Reliability Analyst", "Operations Supervisor", "Quality Assurance Analyst", "Sustainability Manager",
        "Supplier Quality Engineer", "Production Control Coordinator", "Process Improvement Engineer", "CAD/CAM Programmer",
        "Operations Engineer", "Maintenance Planner", "Automation Specialist", "Safety Coordinator", "Industrial Psychologist",
        "Regulatory Compliance Specialist", "Materials Scientist", "Plant Engineer", "Robotics Technician",
        "Environmental Health and Safety Engineer", "Production Coordinator", "Maintenance Electrician", "Manufacturing Supervisor",
        "Design Engineer", "Assembly Line Supervisor", "Human Factors Engineer", "Industrial Sales Representative",
        "Manufacturing Analyst", "Plant Operations Manager", "CNC Operator", "Cost Estimator", "Product Manager",
        "Technical Illustrator", "Research Analyst", "Reliability Coordinator", "Production Scheduler", "Quality Control Manager",
        "CNC Programmer", "Systems Analyst", "Industrial Technology Specialist"
    ]

    # List of all the counties
    countries = [country.name for country in list(pycountry.countries)]

    # Function to create a Profile Description Randomly
    def generate_profile_description(age, country, designation):

        # Generate random data to pick a Hobby
        hobby = random.choice([ "Coding", "Cooking", "Reading", "Photography", "Hiking", "Drawing", 
                               "Playing an Instrument", "Swimming", "Board Games", "Video Games", 
                               "Woodworking", "Astronomy", "Collecting Stamps", "Playing Sports", 
                               "DIY Projects", "Yoga", "Meditation", "Traveling", "Gardening", "Painting", 
                               "Chess", "Blogging", "Knitting", "Watching Movies"])

        # Create profile description
        profile_description = f"I am {age}-year-old {designation} from {country}. In my free time, I enjoy {hobby}."

        #return profile_description
        return profile_description



    all_data = []
    for i in range(200):
        name = rand_male_names[i] if i < 100 else rand_female_names[i - 100]
        user_data = {
            'name': name,
            'age': np.random.randint(18, 60),
            'gender': 'Male' if i < 100 else 'Female',
            'linkedinProfURL': f"https://www.linkedin.com/in/{name.split(' ')[0].lower()}-{name.split(' ')[1].lower()}-{''.join(str(random.randint(0, 9)) for _ in range(9))}/",
            'designation': random.choice(industrial_designations),
            'country': random.choice(countries),
            'disabled': np.random.choice(['Yes', 'No'], p = [0.05, 0.95]),
            'FreshExp': np.random.choice(['Fresher', 'Experienced'], p = [0.5, 0.5]),
            'joinedDate': f"{random.choice(list(calendar.month_name[1:]))} {random.randint(0, 28)}, {random.choice(['2020', '2021', '2022', '2023'])}"
        }

        user_data['profileDescription'] = generate_profile_description(user_data['age'], user_data['country'], user_data['designation'])
        user_data['username'] = '_'.join((name+str(user_data['age'])).lower().split(' '))
        user_data['email'] = user_data['username'] + random.choice(['@gmail.com', '@outlook.com'])
        user_data['password'] = str(hashlib.sha1(user_data['username'].encode()).hexdigest())
        user_data['primaryKey'] = hashlib.sha1((user_data['email']+user_data['password']).encode()).hexdigest()
        all_data.append(user_data)



    return all_data