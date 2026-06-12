# pip install pandas rapidfuzz (download this before running the script)
import pandas as pd
from rapidfuzz import process, utils

print("STEP 1: Loading your raw data...")
# Read the file sitting in your project folder
df = pd.read_csv("../data/monthly_new_vehicle_registration_march_2026.csv")

# ----------------------------------------------------
# CONFIGURATION: Define your rules
# ----------------------------------------------------
# Manual fixes for the specific words that confused the computer
forced_replacements = {
    'FLTOY'  : 'TOYOTA',
    'FL TOY' : 'TOYOTA',
    'FERRAR' : 'FERRARI',
    'FIAT'   : 'FIAT',
    'GEELY'  : 'GEELY',
    'BRAAAP' : 'BRAAAP',
    'KYMCO'  : 'KYMCO',
    'RIEJU'  : 'RIEJU',
    'SURRON' : 'SURRON',
    'SYM'    : 'SYM',
    'UBCO'   : 'UBCO',
    'STARK'  : 'STARK',
    'MV AGU' : 'MV AGUSTA',
    'MASS F' : 'MASS FURGOVAN',
    'JACOB'  : 'JACOBSEN',
    'LAMBR'  : 'LAMBORGHINI',
    'R ROV'  : 'RANGE ROVER',
    'U LOAD' : 'ULOAD',
    'KENWTH' : 'KENWORTH',
    'AJP'    : 'AJP',
}

# The clean dictionary of correct brand names
clean_dictionary = [
    'ABARTH', 'AION', 'ALFA ROMEO', 'ASTON MARTIN', 'AUDI', 'BMW', 'BYD', 'BENTLEY', 
    'CADILLAC', 'CAN-AM', 'CFMOTO', 'CHERY', 'CHEVROLET', 'CUPRA', 'DAF', 'DEEPAL', 
    'DENZA', 'DODGE', 'FORD', 'FOTON', 'FUSO', 'GMC', 'GREAT WALL', 'GAC', 'GENESIS', 
    'GMSV', 'HAVAL', 'HINO', 'HOLDEN', 'HONDA', 'HYUNDAI', 'INEOS', 'ISUZU', 'IVECO', 
    'JAC', 'JAECOO', 'JEEP', 'KGM', 'KIA', 'LAND ROVER', 'RANGE ROVER', 'LAMBORGHINI', 
    'LDV', 'LEAPMOTOR', 'LEXUS', 'MAN', 'MG', 'MACK', 'MAHINDRA', 'MASERATI', 'MAZDA', 
    'MERCEDES-BENZ', 'MINI', 'MITSUBISHI', 'NISSAN', 'OMODA', 'PEUGEOT', 'POLESTAR', 
    'PORSCHE', 'RAM', 'RENAULT', 'SCANIA', 'SKODA', 'SMART', 'SSANGYONG', 'SUBARU', 
    'SUZUKI', 'TESLA', 'TOYOTA', 'UD TRUCKS', 'VOLKSWAGEN', 'VOLVO', 'XPENG', 'ZEEKR',
    'APRILIA', 'BETA', 'DUCATI', 'FANTIC MOTOR', 'GASGAS', 'HARLEY-DAVIDSON', 'HUSQVARNA', 
    'INDIAN', 'KTM', 'KAWASAKI', 'ROYAL ENFIELD', 'SHERCO', 'TRIUMPH', 'VESPA', 'YAMAHA',
    'BOBCAT', 'CASE', 'CATERPILLAR', 'FENDT', 'HINO', 'JOHN DEERE', 'KOMATSU', 'KUBOTA', 
    'SCANIA', 'VALTRA', 'AUSA', 'BCI', 'EP EQUIPMENT', 'HYSTER', 'LIFTSMART', 'LINDE', 
    'MAGNI', 'MANITOU', 'MERLO', 'NICHIYU', 'ASV', 'AVANT', 'DEVELON', 'ENFORCER', 
    'GAIUS', 'GOLDACRE', 'HAMM', 'HANGCHA', 'HYDRO DRIVE', 'HERROD', 'JCB', 'JACOBSEN', 
    'KIOTI', 'KOBELCO', 'LANDINI', 'LIEBHERR', 'LOADMAC', 'LOVOL', 'MACDON', 'MCCORMICK', 
    'NEW HOLLAND', 'POLARIS', 'TAKEUCHI', 'WACKER NEUSON', 'VULCAN', 'ANTONIO CARRARO', 
    'FARIZON', 'MCDONNELL', 'SHANGHAI', 'SINOTRUK', 'FUTUR LINE', 'FERRARI', 'FIAT', 'GEELY', 'BRAAAP', 'KYMCO', 'RIEJU', 
    'SURRON', 'SYM', 'UBCO', 'STARK', 'MV AGUSTA', 'KENWORTH', 'AJP', 'RANGE ROVER',]

print("STEP 2: Cleaning the vehicle names...")
# This empty list will hold our newly cleaned names
cleaned_names_list = []

# Loop through every single row in your messy column
for raw_name in df["CD_MAKE_VEH"]:
    
    # 1. Clean up spaces and make it uppercase
    text_clean = str(raw_name).strip().upper()
    
    # 2. Check if the word matches our manual fixes list first
    if text_clean in forced_replacements:
        final_name = forced_replacements[text_clean]
        
    # 3. If not, let the fuzzy matching algorithm look for a typo fix
    else:
        match_result = process.extractOne(text_clean, clean_dictionary, processor=utils.default_process)
        
        # If the computer is 60% sure or higher, use the corrected word
        if match_result and match_result[1] >= 60:
            final_name = match_result[0]
        else:
            final_name = text_clean # If it can't find a match, leave it as is
            
    # Add our finished name to our list
    cleaned_names_list.append(final_name)

# ----------------------------------------------------
# SAVE THE RESULTS
# ----------------------------------------------------
# Put the clean list back into your DataFrame as a brand new column
df["CLEAN_MAKE_VEH"] = cleaned_names_list

print("STEP 3: Saving your brand new cleaned file...")
df.to_csv("cleaned_veh_data.csv", index=False)

print("All done! Open 'cleaned_veh_data.csv' in your folder to see it!")