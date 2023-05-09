from Functions_module import *



# Set data path
data_path = "./Data/"

# Read in Masters data
masters = pd.read_csv(data_path+"201709301651_masters_portal.csv",
                 low_memory=False,
                 na_values=['NaN', 'nan'],
                 na_filter=True)

# Read in currency exchange data
currencies = pd.read_csv(data_path+"eurofxref.csv")
currencies.columns = [c.replace(" ","") for c in currencies.columns]
currencies = currencies.drop(columns=["Date"]).to_dict('list')

# Transform currency values to EUR
masters['tuition_1_EUR'] = masters.apply(lambda x: transform_currencies(x['tution_1_money'], x['tution_1_currency']), axis=1)

# Convert program duration to months
masters['duration_months'] = masters['duration'].apply(convert_duration)

# Fix city names
masters["city"] = masters["city"].apply(fix_city)

# Split language values into a list
masters.language = masters.language.apply(lambda x: x.split(", ") if not pd.isna(x) else np.nan)

# Create a new DataFrame with selected columns
masters_short = pd.DataFrame(masters, columns = ["program_name","program_type","university_name","program_url",
                      "tuition_1_EUR","duration_months","structure"]).drop_duplicates()

# Read in university and city data
univ_city = pd.DataFrame(pd.read_csv(data_path + "University_ranking.csv"),columns=["Name","City","Country"])\
    .drop_duplicates()
# We change the name of the column to do the join
univ_city.columns = ['university_name', 'City', 'Country']
# Get rid of duplicates
univ_city = univ_city[univ_city.City !="-"]
univ_city = univ_city[univ_city["university_name"].duplicated()==False]

# Read in additional university information
univ_info = pd.read_csv(data_path+"universities_data.csv")

# Keep only the last year
univ_info = univ_info[univ_info.year == 2015].drop(columns =["year"])

# We change the name of the column to do the join
univ_info["university_name"] = univ_info.institution
univ_info = univ_info.drop(columns =["institution"])


"/home/javier/Universidad/Master/2º Semestre/Biological databases/Project/universities.csv"

LOAD DATA INFILE '/path/to/universities.csv'
INTO TABLE universities
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
  program_name,
  program_type,
  program_url,
  tuition_1_EUR FLOAT,
  duration_months INT,
  structure VARCHAR(255),
);









masters.to_csv(data_path+"processed_data.csv")








