company_name = 'TechGenix'

sql_password = 'sql_password'

sql_db = company_name

admuser='ADMIN'

admkey=f'{company_name.lower()}'

assets=r"C:\Users\user\OneDrive\Desktop\CS Project\Assets"

download_path = r"C:\Users\user\Downloads"

company_logo = rf"{assets}\TechGenix.jpg"

aesthetic_banner= rf"{assets}\aesthetic_bg.jpeg"

user_logo = rf"{assets}\user_logo.png"

personal_logo= rf"{assets}\personal_logo.png"

inbox_logo= rf"{assets}\inbox_logo.png"

supervisor_logo= rf"{assets}\supervisor_logo.png"

department_logo= rf"{assets}\department_logo.png"

send_logo= rf"{assets}\send_logo.png"

#Generation Vars

Samples=[]

PassKeys=[]

Characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Contacts=[]

Digits=['0','1','2','3','4','5','6','7','8','9']

eid = None

first_names_male = ['Aaron', 'Adam', 'Adrian', 'Aidan', 'Alexander', 'Andrew', 'Angel', 'Anthony', 'Antonio', 'Arthur', 'Asher', 'Ashton', 'Austin', 'Benjamin', 'Blake', 'Brandon', 'Brian', 'Caleb', 'Cameron', 'Carlos', 'Carson', 'Carter', 'Charles', 'Chase', 'Christopher', 'Cody', 'Cole', 'Collin', 'Connor', 'Daniel', 'David', 'Devin', 'Diego', 'Dominic', 'Dylan', 'Edward', 'Edwin', 'Elias', 'Elijah', 'Elliot', 'Emmett', 'Eric', 'Ethan', 'Evan', 'Ezra', 'Felix', 'Finn', 'Gabriel', 'Gavin', 'George', 'Hayden', 'Henry', 'Hunter', 'Ian', 'Isaac', 'Isaiah', 'Jack', 'Jackson', 'Jacob', 'James', 'Jason', 'Jasper', 'Jayden', 'Jeffrey', 'Jeremiah', 'John', 'Jonah', 'Jonathan', 'Jordan', 'Jose', 'Joseph', 'Joshua', 'Juan', 'Jude', 'Julian', 'Justin', 'Kevin', 'Kyle', 'Landon', 'Leo', 'Levi', 'Liam', 'Link', 'Logan', 'Lucas', 'Luis', 'Luke', 'Martin', 'Mason', 'Matthew', 'Michael', 'Miguel', 'Miles', 'Nathan', 'Nicolas', 'Noah', 'Oscar', 'Owen', 'Patrick', 'Peter', 'Peyton', 'Quinn', 'Richard', 'Robert', 'Ryan', 'Samuel', 'Sawyer', 'Sean', 'Sebastian', 'Seth', 'Simon', 'Spencer', 'Steven', 'Theodore', 'Thomas', 'Timothy', 'Tony', 'Travis', 'Tristan', 'Tyler', 'Wesley', 'William', 'Wyatt', 'Xavier', 'Zachary']

first_names_female = ['Abigail','Adelaide' ,'Adeline', 'Alexa', 'Alexandra', 'Alice', 'Allison', 'Alyssa', 'Amanda', 'Amber', 'Amelia', 'Andrea', 'Angelina', 'Anna', 'Arabella', 'Ariana', 'Ashley', 'Audrey', 'Aurora', 'Autumn', 'Ava', 'Avery', 'Bailey', 'Bella', 'Brianna', 'Brittany', 'Brooke', 'Brooklyn', 'Camila', 'Caroline', 'Charlotte', 'Chloe', 'Claire', 'Cora', 'Danielle', 'Destiny', 'Elena', 'Eliza', 'Ella', 'Eloise', 'Emily', 'Emma', 'Erica', 'Erin', 'Evelyn', 'Faith', 'Gabriella', 'Georgie', 'Grace', 'Haley', 'Hannah', 'Harper', 'Hazel', 'Isabella', 'Isla', 'Ivy', 'Jada', 'Jane', 'Jasmine', 'Jenna', 'Jennifer', 'Jessica', 'Josephine', 'Julia', 'Karen', 'Katelyn', 'Katherine', 'Kayla', 'Kelly', 'Kelsie', 'Kiara', 'Kimberly', 'Kira', 'Kylie', 'Lauren', 'Layla', 'Leah', 'Lily', 'Lola', 'Lucy', 'Mackenzie', 'Madeline', 'Madison', 'Makayla', 'Maria', 'Mariah', 'Mary', 'Maya', 'Megan', 'Melanie', 'Mia', 'Michelle', 'Molly', 'Morgan', 'Natalie', 'Navaeh', 'Nicole', 'Nina', 'Nora', 'Olivia', 'Paige', 'Rachel', 'Raegan', 'Rebecca', 'Riley', 'Rose', 'Ruby', 'Sabrina', 'Samantha', 'Sarah', 'Savannah', 'Scarlett', 'Sierra', 'Skylar', 'Sophia', 'Stella', 'Stephanie', 'Summer', 'Sydney', 'Taylor', 'Vanessa', 'Victoria', 'Violet', 'Vivian', 'Zoe']

middle_names_male = ['Cash', 'Chester', 'Clay', 'Cole', 'Colt', 'Earl', 'Floyd', 'Grey', 'Jay', 'Kai', 'Leon', 'Lloyd', 'Louis', 'Mac', 'Max', 'Nash', 'Nico', 'Norman', 'Oscar', 'Paul', 'Ralph', 'Seth', 'Stan', 'Tate', 'Warren']

middle_names_female = ['Anna', 'Celine', 'Elise', 'Ella', 'Eve', 'Gem', 'Grace', 'Hazel', 'Helen', 'Hope', 'Jes', 'Joy', 'Kat', 'Luna', 'Mia', 'Quinn', 'Rae', 'Ray', 'Rose', 'Star', 'Sue', 'Talia', 'Veda', 'Zara', 'Zoe']

last_names = ['Adams', 'Aguilar', 'Alexander', 'Allen', 'Anderson', 'Andrews', 'Armstrong', 'Arnold', 'Austin', 'Bailey', 'Baker', 'Barnes', 'Bennett', 'Berry', 'Bishop', 'Black', 'Boyd', 'Bradley', 'Brooks', 'Brown', 'Burke', 'Burns', 'Butler', 'Campbell', 'Carpenter', 'Carroll', 'Carter', 'Castillo', 'Castro', 'Chapman', 'Chavez', 'Clark', 'Cole', 'Coleman', 'Collins', 'Cook', 'Cooper', 'Cox', 'Crawford', 'Cruz', 'Cunningham', 'Davis', 'Dean', 'Diaz', 'Dixon', 'Duncan', 'Dunn', 'Edwards', 'Elliot', 'Elliott', 'Evans', 'Ferguson', 'Fernandez', 'Fisher', 'Flores', 'Ford', 'Foster', 'Fox', 'Franklin', 'Freeman', 'Garcia', 'Gardner', 'George', 'Gibson', 'Gilbert', 'Gomez', 'Gonzalez', 'Gonzales', 'Gordon', 'Gray', 'Greene', 'Griffin', 'Gutierrez', 'Hall', 'Hamilton', 'Hansen', 'Harper', 'Harrison', 'Harvey', 'Hayes', 'Henderson', 'Henry', 'Hernandez', 'Hicks', 'Hill', 'Hoffman', 'Holmes', 'Hudson', 'Hunt', 'Hunter', 'Hawkins', 'Herrera', 'Hicks', 'Hill', 'Hoffman', 'Holmes', 'Hudson', 'Hunt', 'Hunter', 'Jacobs', 'James', 'Jensen', 'Jimenez', 'Johnson', 'Johnston', 'Jones', 'Jordan', 'Kelly', 'Kennedy', 'King', 'Knight', 'Lane', 'Larson', 'Lawrence', 'Lee', 'Lewis', 'Lopez', 'Lynch', 'Mason', 'Martinez', 'Martin', 'Matthews', 'Mcdonald', 'Mendez', 'Meyer', 'Mills', 'Mitchell', 'Montgomery', 'Moore', 'Morales', 'Moreno', 'Morris', 'Morrison', 'Munoz', 'Murphy', 'Murray', 'Myers', 'Nelson', 'Nichols', 'Obrien', 'Oliver', 'Olson', 'Owens', 'Palmer', 'Parker', 'Patel', 'Patterson', 'Payne', 'Perez', 'Perry', 'Peters', 'Phillips', 'Pierce', 'Porter', 'Powell', 'Price', 'Ramirez', 'Rice', 'Richards', 'Richardson', 'Riley', 'Rivera', 'Roberts', 'Robertson', 'Robinson', 'Rogers', 'Romero', 'Rose', 'Ross', 'Ruiz', 'Ryan', 'Sanchez', 'Sanders', 'Schmidt', 'Scott', 'Silva', 'Simmons', 'Simpson', 'Snyder', 'Spencer', 'Stewart', 'Stone', 'Sullivan', 'Taylor', 'Thomas', 'Thompson', 'Torres', 'Tran', 'Turner', 'Vargas', 'Vasquez', 'Vargas', 'Vasquez', 'Vargas', 'Vasquez', 'Wagner', 'Walker', 'Wallace', 'Watkins', 'Watson', 'Watts', 'Weaver', 'Wells', 'White', 'Williams', 'Willis', 'Wilson', 'Wood', 'Woods', 'Washington', 'Wheeler', 'Williamson', 'Willis', 'Wilson', 'Wood', 'Woods', 'Washington', 'Wheeler', 'Williamson', 'Willis', 'Wilson', 'Wood', 'Woods', 'Wright', 'Young']

DOBs=[]

Gender=['F','M','Other']

Userlist = []

Departments = []

Supervisors = ['Sales Supervisor', 'Marketing Supervisor', 'HR Supervisor', 'Finance Supervisor', 'IT Supervisor', 'Operations Supervisor', 'Customer Service Supervisor', 'R&D Supervisor', 'Legal Supervisor', 'Administrative Supervisor', 'Supply Chain Supervisor', 'QA Supervisor', 'PR Supervisor', 'Product Supervisor', 'Engineering Supervisor', 'Design Supervisor', 'H&S Supervisor', 'Training Supervisor', 'Compliance Supervisor']

street_names = ['Oak', 'Maple', 'Pine', 'Cedar', 'Elm', 'Willow', 'Birch', 'Aspen', 'Hickory', 'Chestnut']

street_types = ['St', 'Ave', 'Blvd', 'Dr', 'Ln', 'Ct', 'Rd', 'Way', 'Pl']

us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

us_states_cities = {
    'Alabama': [['Birmingham', '35203'], ['Montgomery', '36104'], ['Mobile', '36602'], ['Huntsville', '35801'], ['Tuscaloosa', '35401']],
    'Alaska': [['Anchorage', '99501'], ['Fairbanks', '99701'], ['Juneau', '99801'], ['Sitka', '99835'], ['Ketchikan', '99901']],
    'Arizona': [['Phoenix', '85001'], ['Tucson', '85701'], ['Mesa', '85201'], ['Chandler', '85225'], ['Glendale', '85301']],
    'Arkansas': [['Little Rock', '72201'], ['Fort Smith', '72901'], ['Fayetteville', '72701'], ['Springdale', '72764'], ['Jonesboro', '72401']],
    'California': [['Los Angeles', '90001'], ['San Diego', '92101'], ['San Jose', '95101'], ['San Francisco', '94102'], ['Fresno', '93701']],
    'Colorado': [['Denver', '80202'], ['Colorado Springs', '80903'], ['Aurora', '80010'], ['Fort Collins', '80521'], ['Lakewood', '80226']],
    'Connecticut': [['Bridgeport', '06601'], ['New Haven', '06501'], ['Stamford', '06901'], ['Hartford', '06101'], ['Waterbury', '06702']],
    'Delaware': [['Wilmington', '19801'], ['Dover', '19901'], ['Newark', '19702'], ['Middletown', '19709'], ['Smyrna', '19977']],
    'Florida': [['Jacksonville', '32202'], ['Miami', '33101'], ['Tampa', '33601'], ['Orlando', '32801'], ['St. Petersburg', '33701']],
    'Georgia': [['Atlanta', '30301'], ['Augusta', '30901'], ['Columbus', '31901'], ['Macon', '31201'], ['Savannah', '31401']],
    'Hawaii': [['Honolulu', '96801'], ['Hilo', '96720'], ['Kailua', '96734'], ['Kapolei', '96707'], ['Pearl City', '96782']],
    'Idaho': [['Boise', '83702'], ['Meridian', '83642'], ['Nampa', '83651'], ['Idaho Falls', '83402'], ['Pocatello', '83201']],
    'Illinois': [['Chicago', '60601'], ['Aurora', '60505'], ['Rockford', '61101'], ['Joliet', '60432'], ['Naperville', '60540']],
    'Indiana': [['Indianapolis', '46201'], ['Fort Wayne', '46802'], ['Evansville', '47708'], ['South Bend', '46601'], ['Carmel', '46032']],
    'Iowa': [['Des Moines', '50309'], ['Cedar Rapids', '52401'], ['Davenport', '52801'], ['Sioux City', '51101'], ['Iowa City', '52240']],
    'Kansas': [['Wichita', '67202'], ['Overland Park', '66202'], ['Kansas City', '66101'], ['Olathe', '66051'], ['Topeka', '66603']],
    'Kentucky': [['Louisville', '40202'], ['Lexington', '40502'], ['Bowling Green', '42101'], ['Owensboro', '42301'], ['Covington', '41011']],
    'Louisiana': [['New Orleans', '70112'], ['Baton Rouge', '70802'], ['Shreveport', '71101'], ['Lafayette', '70501'], ['Lake Charles', '70601']],
    'Maine': [['Portland', '04101'], ['Lewiston', '04240'], ['Bangor', '04401'], ['South Portland', '04106'], ['Auburn', '04210']],
    'Maryland': [['Baltimore', '21201'], ['Frederick', '21701'], ['Rockville', '20850'], ['Gaithersburg', '20877'], ['Bowie', '20715']],
    'Massachusetts': [['Boston', '02101'], ['Worcester', '01601'], ['Springfield', '01101'], ['Lowell', '01852'], ['Cambridge', '02138']],
    'Michigan': [['Detroit', '48201'], ['Grand Rapids', '49503'], ['Warren', '48093'], ['Sterling Heights', '48310'], ['Ann Arbor', '48104']],
    'Minnesota': [['Minneapolis', '55401'], ['Saint Paul', '55101'], ['Rochester', '55901'], ['Bloomington', '55420'], ['Duluth', '55802']],
    'Mississippi': [['Jackson', '39201'], ['Gulfport', '39501'], ['Southaven', '38671'], ['Hattiesburg', '39401'], ['Biloxi', '39530']],
    'Missouri': [['Kansas City', '64101'], ['St. Louis', '63101'], ['Springfield', '65802'], ['Independence', '64050'], ['Columbia', '65201']],
    'Montana': [['Billings', '59101'], ['Missoula', '59801'], ['Great Falls', '59401'], ['Bozeman', '59715'], ['Butte', '59701']],
    'Nebraska': [['Omaha', '68102'], ['Lincoln', '68502'], ['Bellevue', '68005'], ['Grand Island', '68801'], ['Kearney', '68845']],
    'Nevada': [['Las Vegas', '89101'], ['Henderson', '89002'], ['Reno', '89501'], ['North Las Vegas', '89030'], ['Sparks', '89431']],
    'New Hampshire': [['Manchester', '03101'], ['Nashua', '03060'], ['Concord', '03301'], ['Derry', '03038'], ['Dover', '03820']],
    'New Jersey': [['Newark', '07102'], ['Jersey City', '07302'], ['Paterson', '07501'], ['Elizabeth', '07201'], ['Edison', '08817']],
    'New Mexico': [['Albuquerque', '87102'], ['Las Cruces', '88001'], ['Rio Rancho', '87124'], ['Santa Fe', '87501'], ['Roswell', '88201']],
    'New York': [['New York City', '10001'], ['Buffalo', '14201'], ['Rochester', '14602'], ['Yonkers', '10701'], ['Syracuse', '13202']],
    'North Carolina': [['Charlotte', '28202'], ['Raleigh', '27601'], ['Greensboro', '27401'], ['Durham', '27701'], ['Winston-Salem', '27101']],
    'North Dakota': [['Fargo', '58102'], ['Bismarck', '58501'], ['Grand Forks', '58201'], ['Minot', '58701'], ['West Fargo', '58078']],
    'Ohio': [['Columbus', '43201'], ['Cleveland', '44101'], ['Cincinnati', '45201'], ['Toledo', '43601'], ['Akron', '44301']],
    'Oklahoma': [['Oklahoma City', '73102'], ['Tulsa', '74103'], ['Norman', '73069'], ['Broken Arrow', '74012'], ['Lawton', '73501']],
    'Oregon': [['Portland', '97201'], ['Salem', '97301'], ['Eugene', '97401'], ['Gresham', '97030'], ['Hillsboro', '97123']],
    'Pennsylvania': [['Philadelphia', '19102'], ['Pittsburgh', '15201'], ['Allentown', '18101'], ['Erie', '16501'], ['Reading', '19601']],
    'Rhode Island': [['Providence', '02903'], ['Warwick', '02886'], ['Cranston', '02910'], ['Pawtucket', '02860'], ['East Providence', '02914']],
    'South Carolina': [['Columbia', '29201'], ['Charleston', '29401'], ['North Charleston', '29405'], ['Mount Pleasant', '29464'], ['Rock Hill', '29730']],
    'South Dakota': [['Sioux Falls', '57103'], ['Rapid City', '57701'], ['Aberdeen', '57401'], ['Brookings', '57006'], ['Watertown', '57201']],
    'Tennessee': [['Nashville', '37201'], ['Memphis', '38103'], ['Knoxville', '37902'], ['Chattanooga', '37402'], ['Clarksville', '37040']],
    'Texas': [['Houston', '77001'], ['San Antonio', '78201'], ['Dallas', '75201'], ['Austin', '78701'], ['Fort Worth', '76102']],
    'Utah': [['Salt Lake City', '84101'], ['West Valley City', '84119'], ['Provo', '84601'], ['West Jordan', '84084'], ['Orem', '84057']],
    'Vermont': [['Burlington', '05401'], ['South Burlington', '05403'], ['Rutland', '05701'], ['Essex Junction', '05452'], ['Montpelier', '05602']],
    'Virginia': [['Virginia Beach', '23450'], ['Norfolk', '23501'], ['Chesapeake', '23320'], ['Richmond', '23219'], ['Newport News', '23607']],
    'Washington': [['Seattle', '98101'], ['Spokane', '99201'], ['Tacoma', '98402'], ['Vancouver', '98660'], ['Bellevue', '98004']],
    'West Virginia': [['Charleston', '25301'], ['Huntington', '25701'], ['Parkersburg', '26101'], ['Wheeling', '26003'], ['Morgantown', '26501']],
    'Wisconsin': [['Milwaukee', '53202'], ['Madison', '53703'], ['Green Bay', '54301'], ['Kenosha', '53140'], ['Racine', '53403']],
    'Wyoming': [['Cheyenne', '82001'], ['Casper', '82601'], ['Laramie', '82070'], ['Gillette', '82716'], ['Rock Springs', '82901']]
}
