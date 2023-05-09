import csv
import os
from django.http import HttpResponse
from django.shortcuts import render
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET


def csv_to_xml(request):
    if request.method == 'POST':
        if request.FILES and 'csvFile' in request.FILES:
            csv_file = request.FILES['csvFile']
            csv_file_name = csv_file.name
            upload_path = os.path.join('upload', csv_file_name)

            # Create the upload directory if it does not exist
            upload_directory = os.path.join('..', 'upload')
            if not os.path.exists(upload_directory):
                os.makedirs(upload_directory)

            # Write the uploaded file to the upload directory
            with open(upload_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            # Process the CSV file
            output = []
            with open(upload_path, 'r', encoding='ISO-8859-1') as csv_file:
            # with open(upload_path, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                header = next(csv_reader)  # Get the header row
                                
                # Find the indices of columns containing 'Qual1' and 'Buy_Q6' using string matching
                #) number to letter
                qual1_indices = [i for i, col_name in enumerate(header) if 'Qual1_' in col_name]

                #I put these here for following the order of the csv file
                qual_2_indices = [i for i, col_name in enumerate(header) if 'Qual_2' in col_name]
                online_q1_indices = [i for i, col_name in enumerate(header) if 'Online_Q1' in col_name]
                
                #) number to letter also
                buy_q6_indices = [i for i, col_name in enumerate(header) if 'Buy_Q6_' in col_name]
                discovery_q1_indices = [i for i, col_name in enumerate(header) if 'Discovery_Q1_' in col_name]
                


                #2) minus adjustments
                # minus_adjustments_indices = [i for i, col_name in enumerate(header) if 'Discovery_Q2' in col_name or 'Buy_Q8' in col_name or 'Discovery_Q3a' in col_name or 'Discovery_Q3b' in col_name or 'Discovery_Q3c' in col_name or 'Discovery_Q3d' in col_name or 'Discovery_Q3e' in col_name or 'Discovery_Q4' in col_name or 'Discovery_Q5' in col_name or 'Discovery_Q6' in col_name or 'Discovery_Q7' in col_name or 'Discovery_Q8' in col_name or 'Discovery_Q10' in col_name or 'Discovery_Q11' in col_name or 'Discovery_Q14a' in col_name or 'Discovery_Q14b' in col_name or 'Discovery_Q14c' in col_name or 'Discovery_Q14d' in col_name or 'Discovery_Q14e' in col_name or 'Offer_Q2a' in col_name or 'Offer_Q2b' in col_name or 'Offer_Q3' in col_name or 'Follow_Q1' in col_name]
                
                discovery_q2_indices = [i for i, col_name in enumerate(header) if 'Discovery_Q2' in col_name]
                online_q3_indices = [i for i, col_name in enumerate(header) if 'Online_Q3' in col_name]

                improve_q1_indices = [i for i, col_name in enumerate(header) if 'Improve_Q1' in col_name]

                buy_q1_indices = [i for i, col_name in enumerate(header) if  col_name == 'Buy_Q1']
                buy_q2_li_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q2_LI']
                buy_q2_li_m_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q2_LI_M']
                buy_q3_indices = [i for i, col_name in enumerate(header) if 'Buy_Q3' in col_name]
                buy_q4a_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q4a']
                buy_q4b_indices = [i for i, col_name in enumerate(header) if 'Buy_Q4b' in col_name]
                buy_q4a_li_indices = [i for i, col_name in enumerate(header) if  col_name == 'Buy_Q4a_LI']
                buy_q5a_1b_indices = [i for i, col_name in enumerate(header) if 'Buy_Q5a_1b' in col_name]
                buy_q5a_2b_indices = [i for i, col_name in enumerate(header) if 'Buy_Q5a_2b' in col_name]
                buy_q5a_3b_indices = [i for i, col_name in enumerate(header) if 'Buy_Q5a_3b' in col_name]
                buy_q5b_1b_indices = [i for i, col_name in enumerate(header) if 'Buy_Q5b_1b' in col_name]
                buy_q5b_2b_indices = [i for i, col_name in enumerate(header) if 'Buy_Q5b_2b' in col_name]
                buy_q5b_3b_indices = [i for i, col_name in enumerate(header) if 'Buy_Q5b_3b' in col_name]
                buy_q5_li_indices = [i for i, col_name in enumerate(header) if 'Buy_Q5_LI' in col_name]


                buy_q7a_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q7a']
                buy_q7b_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q7b']
                buy_q7c_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q7c']
                buy_q7d_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q7d']
                buy_q7e_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q7e']
                
                discovery_q3a_indices = [i for i, col_name in enumerate(header) if 'Discovery_Q3a' in col_name]
                discovery_q3b_indices = [i for i, col_name in enumerate(header) if 'Discovery_Q3b' in col_name]

                discovery_q3c_indices = [i for i, col_name in enumerate(header) if 'Discovery_Q3c' in col_name]
                discovery_q3d_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q3d']
                discovery_q3d1_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q3d1']
                discovery_q3e_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q3e']
                discovery_q3e1_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q3e1']

                discovery_q3f_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q3f']
                discovery_q3f1_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q3f1']

                discovery_q4_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q4']
                discovery_q5_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q5']
                discovery_q6_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q6']
                discovery_q7_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q7']
                discovery_q8_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q8']


                discovery_q9_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q9']
                discovery_q10_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q10']
                discovery_q11_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q11']
                discovery_q12_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q12']
                discovery_q13_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q13']
                discovery_q14_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q14']

                discovery_q14a_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q14a']
                discovery_q14b_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q14b']
                discovery_q14c_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q14c']
                discovery_q14d_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q14d']

                discovery_q14d1_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q14d1']

                discovery_q14e_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q14e']

                discovery_q14e1_indices = [i for i, col_name in enumerate(header) if col_name == 'Discovery_Q14e1']

                offer_q1_indices = [i for i, col_name in enumerate(header) if col_name == 'Offer_Q1']
                offer_q1a_indices = [i for i, col_name in enumerate(header) if col_name == 'Offer_Q1a']
                offer_q1b_indices = [i for i, col_name in enumerate(header) if col_name == 'Offer_Q1b']
                offer_q1c_indices = [i for i, col_name in enumerate(header) if col_name == 'Offer_Q1c']

                offer_q2a_indices = [i for i, col_name in enumerate(header) if col_name == 'Offer_Q2a']
                offer_q2b_indices = [i for i, col_name in enumerate(header) if col_name == 'Offer_Q2b']


                offer_q2_1_indices = [i for i, col_name in enumerate(header) if 'Offer_Q2_1_1' in col_name or 'Offer_Q2_1_2' in col_name]

                offer_q3_indices = [i for i, col_name in enumerate(header) if col_name == 'Offer_Q3']
                follow_q1_indices = [i for i, col_name in enumerate(header) if col_name == 'Follow_Q1']
                follow_q1_1_indices = [i for i, col_name in enumerate(header) if col_name == 'Follow_Q1_1']
                anonym_q1_indices = [i for i, col_name in enumerate(header) if col_name == 'Anonym_Q1']
                                                
                buy_Q8_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q8']
                buy_q9_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q9']
                buy_q10_indices = [i for i, col_name in enumerate(header) if col_name == 'Buy_Q10']
                
                online_q2_indices = [i for i, col_name in enumerate(header) if 'Online_Q2' in col_name]


                #I put these here also for following the order of the csv file

                crs_q1_indices = [i for i, col_name in enumerate(header) if 'CRS_Q1' in col_name]
                crs_q2_indices = [i for i, col_name in enumerate(header) if 'CRS_Q2' in col_name]


                # Include the header row in the output
                output.append(header)


                for row in csv_reader:
                    
                    # Update the corresponding letters based on column indices
                    combined_qual1 = ''
                    combined_buy_q6 = ''
                    combined_discovery_q1 = ''

                    adjusted_online_q2 = ''
                    adjusted_qual_2 = ''

                    adjusted_buy_q7a = ''
                    adjusted_buy_q7b = ''
                    adjusted_buy_q7c = ''
                    adjusted_buy_q7d = ''
                    adjusted_buy_q7e = ''

                    adjusted_buy_q1 = ''
                    adjusted_buy_q2_li = ''
                    adjusted_buy_q2_li_m = ''
                    adjusted_buy_q3 = ''
                    adjusted_buy_q4a = ''
                    adjusted_buy_q4b = ''
                    adjusted_buy_q4a_li = ''
                    adjusted_buy_q5a_1b = ''
                    adjusted_buy_q5a_2b = ''
                    adjusted_buy_q5a_3b = ''
                    adjusted_buy_q5b_1b = ''
                    adjusted_buy_q5b_2b = ''
                    adjusted_buy_q5b_3b = ''
                    adjusted_buy_q5_li = ''

                    adjusted_online_q1 = int()
                    adjusted_crs_q1 = int()
                    adjusted_crs_q2 = ''

                    #minus adjustments
                    adjusted_discovery_q2 = int()
                    adjusted_online_q3 = int()
                    adjusted_improve_q1 = ''
                    adjusted_discovery_q3a = int()
                    adjusted_discovery_q3b = int()

                    adjusted_discovery_q3c = int()
                    adjusted_discovery_q3d = int()
                    adjusted_discovery_q3d1 = ''
                    adjusted_discovery_q3e = int()
                    adjusted_discovery_q3e1 = ''

                    adjusted_buy_q8 = int()
                    adjusted_buy_q9 = ''
                    adjusted_buy_q10 = ''

                    adjusted_discovery_q3f = int()
                    adjusted_discovery_q3f1 = ''

                    adjusted_discovery_q4 = int()
                    adjusted_discovery_q5 = int()
                    adjusted_discovery_q6 = int()
                    adjusted_discovery_q7 = int()
                    adjusted_discovery_q8 = int()
                    adjusted_discovery_q9 = int()
                    adjusted_discovery_q10 = int()
                    adjusted_discovery_q11 = int()
                    adjusted_discovery_q12 = int()
                    adjusted_discovery_q13 = int()
                    adjusted_discovery_q14 = int()

                    adjusted_discovery_q14a = int()
                    adjusted_discovery_q14b = int()
                    adjusted_discovery_q14c = int()
                    adjusted_discovery_q14d = int()
                    adjusted_discovery_q14d1 = ''
                    adjusted_discovery_q14e = int()
                    adjusted_discovery_q14e1 = ''

                    adjusted_offer_q1 = ''
                    adjusted_offer_q1a = int()
                    adjusted_offer_q1b = int()
                    adjusted_offer_q1c = int()

                    adjusted_offer_q2a = int()
                    adjusted_offer_q2b = int()

                    combined_offer_q2_1 = ''

                    adjusted_offer_q3 = int()
                    adjusted_follow_q1 = int()
                    adjusted_follow_q1_1 = ''
                    adjusted_anonym_q1 = int()

                

                    for i, value in enumerate(row):
                        if i == 0:
                            continue  # Skip updating the ID column

                        # Check if the column index is in the qual1_indices or buy_q6_indices
                        if i in qual1_indices:
                            if int(value) == 2:
                                combined_qual1 += chr(97 + qual1_indices.index(i)) + ','  # Map column indices to letters a, b, c, d, e

                        elif i in qual_2_indices:
                            qual_2_value = row[i] 
                            adjusted_qual_2 = qual_2_value
                            row[i] = adjusted_qual_2                               
                                        

                        elif i in online_q1_indices: 
                            online_q1_value = row[i] 
                            adjusted_online_q1 = str(int(online_q1_value) - 1)
                            row[i] = adjusted_online_q1 


                        elif i in online_q2_indices:
                            online_q2_value = row[i] 
                            adjusted_online_q2 = online_q2_value
                            row[i] = adjusted_online_q2


                        elif i in buy_q1_indices:
                            buy_q1_value = row[i]
                            adjusted_buy_q1 = buy_q1_value
                            row[i] = adjusted_buy_q1

                        elif i in buy_q2_li_indices:
                            buy_q2_li_value = row[i]
                            adjusted_buy_q2_li = buy_q2_li_value
                            row[i] = adjusted_buy_q2_li

                        elif i in buy_q2_li_m_indices:
                            buy_q2_li_m_value = row[i]
                            adjusted_buy_q2_li_m = buy_q2_li_m_value
                            row[i] = adjusted_buy_q2_li_m

                        elif i in buy_q3_indices:
                            buy_q3_value = row[i]
                            adjusted_buy_q3 = buy_q3_value
                            row[i] = adjusted_buy_q3

                        elif i in buy_q4a_indices:
                            buy_q4a_value = row[i]
                            adjusted_buy_q4a = buy_q4a_value
                            row[i] = adjusted_buy_q4a

                        elif i in buy_q4b_indices:
                            buy_q4b_value = row[i]
                            adjusted_buy_q4b = buy_q4b_value
                            row[i] = adjusted_buy_q4b

                        elif i in buy_q4a_li_indices:
                            buy_q4a_li_value = row[i]
                            adjusted_buy_q4a_li = buy_q4a_li_value
                            row[i] = adjusted_buy_q4a_li

                        elif i in buy_q5a_1b_indices:
                            buy_q5a_1b_value = row[i]
                            adjusted_buy_q5a_1b = buy_q5a_1b_value
                            row[i] = adjusted_buy_q5a_1b

                        elif i in buy_q5a_2b_indices:
                            buy_q5a_2b_value = row[i]
                            adjusted_buy_q5a_2b = buy_q5a_2b_value
                            row[i] = adjusted_buy_q5a_2b

                        elif i in buy_q5a_3b_indices:
                            buy_q5a_3b_value = row[i]
                            adjusted_buy_q5a_3b = buy_q5a_3b_value
                            row[i] = adjusted_buy_q5a_3b

                        elif i in buy_q5b_1b_indices:
                            buy_q5b_1b_value = row[i]
                            adjusted_buy_q5b_1b = buy_q5b_1b_value
                            row[i] = adjusted_buy_q5b_1b

                        elif i in buy_q5b_2b_indices:
                            buy_q5b_2b_value = row[i]
                            adjusted_buy_q5b_2b = buy_q5b_2b_value
                            row[i] = adjusted_buy_q5b_2b

                        elif i in buy_q5b_3b_indices:
                            buy_q5b_3b_value = row[i]
                            adjusted_buy_q5b_3b = buy_q5b_3b_value
                            row[i] = adjusted_buy_q5b_3b

                        elif i in buy_q5_li_indices:
                            buy_q5_li_value = row[i]
                            adjusted_buy_q5_li = buy_q5_li_value
                            row[i] = adjusted_buy_q5_li
    

                        elif i in crs_q1_indices:
                            crs_q1_value = row[i] 

                            try:
                                crs_q1_value_int = int(crs_q1_value)
                                adjusted_crs_q1 = str(crs_q1_value_int - 1)
                            except ValueError:
                                # Handle case where crs_q1_value is not an integer
                                adjusted_crs_q1 = ''

                            # adjusted_crs_q1 = str(int(crs_q1_value) - 1)
                            row[i] = adjusted_crs_q1

                        elif i in crs_q2_indices:
                            crs_q2_value = row[i] 
                            adjusted_crs_q2 = crs_q2_value
                            row[i] = adjusted_crs_q2   

                        elif i in online_q3_indices: 
                            online_q3_value = row[i]
                            try:
                                if online_q3_value == '-9':
                                    adjusted_online_q3 = '99'
                                elif online_q3_value == '-1':
                                    adjusted_online_q3 = 'a'
                                elif online_q3_value == '-2':
                                    adjusted_online_q3 = 'b'
                                else:
                                    adjusted_online_q3 = str(int(online_q3_value) - 1)
                            except ValueError:
                                # Handle case where crs_q1_value is not an integer
                                adjusted_online_q3 = ''        

                            row[i] = adjusted_online_q3      
                           
                        elif i in improve_q1_indices:
                            improve_q1_value = row[i] 
                            adjusted_improve_q1 = improve_q1_value
                            row[i] = adjusted_improve_q1

                        elif i in buy_q6_indices:
                            if int(value) == 2:
                                combined_buy_q6 += chr(97 + buy_q6_indices.index(i)) + ','  # Map column indices to letters a, b, c, d, e
                       
                        elif i in discovery_q1_indices:
                            if int(value) == 2:
                                combined_discovery_q1 += chr(97 + discovery_q1_indices.index(i)) + ','

                        elif i in buy_q7a_indices:
                            buy_q7a_value = row[i]
                            if buy_q7a_value == '1':
                                adjusted_buy_q7a = 'Y'
                            elif buy_q7a_value == '2':
                                adjusted_buy_q7a = 'N'
                            row[i]= adjusted_buy_q7a  

                        elif i in buy_q7b_indices:
                            buy_q7b_value = row[i]
                            if buy_q7b_value == '1':
                                adjusted_buy_q7b = 'Y'
                            elif buy_q7b_value == '2':
                                adjusted_buy_q7b = 'N'
                            row[i]= adjusted_buy_q7b 

                        elif i in buy_q7c_indices:
                            buy_q7c_value = row[i]
                            if buy_q7c_value == '1':
                                adjusted_buy_q7c = 'Y'
                            elif buy_q7c_value == '2':
                                adjusted_buy_q7c = 'N'
                            row[i]= adjusted_buy_q7c  

                        elif i in buy_q7d_indices:
                            buy_q7d_value = row[i]
                            if buy_q7d_value == '1':
                                adjusted_buy_q7d = 'Y'
                            elif buy_q7d_value == '2':
                                adjusted_buy_q7d = 'N'
                            row[i]= adjusted_buy_q7d

                        elif i in buy_q7e_indices:
                            buy_q7e_value = row[i]
                            if buy_q7e_value == '1':
                                adjusted_buy_q7e = 'Y'
                            elif buy_q7e_value == '2':
                                adjusted_buy_q7e = 'N'
                            row[i]= adjusted_buy_q7e                 

                        elif i in buy_Q8_indices: 
                            buy_q8_value = row[i]
                            if buy_q8_value == '-9':
                                adjusted_buy_q8 = '99'
                            elif buy_q8_value == '-1':
                                adjusted_buy_q8 = 'a'
                            elif buy_q8_value == '-2':
                                adjusted_buy_q8 = 'b'
                            else:
                                adjusted_buy_q8 = str(int(buy_q8_value) - 1)
                            row[i] = adjusted_buy_q8


                        elif i in buy_q9_indices:
                            buy_q9_value = row[i] 
                            adjusted_buy_q9 = buy_q9_value
                            row[i] = adjusted_buy_q9   

                        elif i in buy_q10_indices:
                            buy_q10_value = row[i] 
                            adjusted_buy_q10 = buy_q10_value
                            row[i] = adjusted_buy_q10    

                        elif i in discovery_q2_indices: 
                            discovery_q2_value = row[i]
                            if discovery_q2_value == '-9':
                                adjusted_discovery_q2 = '99'
                            elif discovery_q2_value == '-1':
                                adjusted_discovery_q2 = 'a'
                            elif discovery_q2_value == '-2':
                                adjusted_discovery_q2 = 'b'
                            else:
                                adjusted_discovery_q2 = str(int(discovery_q2_value) - 1)
                            row[i] = adjusted_discovery_q2 

                        elif i in discovery_q3a_indices: 
                            discovery_q3a_value = row[i]
                            if discovery_q3a_value == '-9':
                                adjusted_discovery_q3a = '99'
                            elif discovery_q3a_value == '-1':
                                adjusted_discovery_q3a = 'a'
                            elif discovery_q3a_value == '-2':
                                adjusted_discovery_q3a = 'b'
                            else:
                                adjusted_discovery_q3a = str(int(discovery_q3a_value) - 1)
                            row[i] = adjusted_discovery_q3a

                        elif i in discovery_q3b_indices: 
                            discovery_q3b_value = row[i]
                            if discovery_q3b_value == '-9':
                                adjusted_discovery_q3b = '99'
                            elif discovery_q3b_value == '-1':
                                adjusted_discovery_q3b = 'a'
                            elif discovery_q3b_value == '-2':
                                adjusted_discovery_q3b = 'b'
                            else:
                                adjusted_discovery_q3b = str(int(discovery_q3b_value) - 1)
                            row[i] = adjusted_discovery_q3b

                        elif i in discovery_q3c_indices: 
                            discovery_q3c_value = row[i]
                            if discovery_q3c_value == '-9':
                                adjusted_discovery_q3c = '99'
                            elif discovery_q3c_value == '-1':
                                adjusted_discovery_q3c = 'a'
                            elif discovery_q3c_value == '-2':
                                adjusted_discovery_q3c = 'b'
                            else:
                                adjusted_discovery_q3c = str(int(discovery_q3c_value) - 1)
                            row[i] = adjusted_discovery_q3c  

                        elif i in discovery_q3d_indices: 
                            discovery_q3d_value = row[i]
                            if discovery_q3d_value == '-9':
                                adjusted_discovery_q3d = '99'
                            elif discovery_q3d_value == '-1':
                                adjusted_discovery_q3d = 'a'
                            elif discovery_q3d_value == '-2':
                                adjusted_discovery_q3d = 'b'
                            else:
                                adjusted_discovery_q3d = str(int(discovery_q3d_value) - 1)
                            row[i] = adjusted_discovery_q3d  

                        elif i in discovery_q3d1_indices:

                            discovery_q3d1_value = row[i]
                            adjusted_discovery_q3d1 = discovery_q3d1_value
                            row[i] = adjusted_discovery_q3d1  



                        elif i in discovery_q3e_indices: 
                            discovery_q3e_value = row[i]
                            if discovery_q3e_value == '-9':
                                adjusted_discovery_q3e = '99'
                            elif discovery_q3e_value == '-1':
                                adjusted_discovery_q3e = 'a'
                            elif discovery_q3e_value == '-2':
                                adjusted_discovery_q3e = 'b'
                            else:
                                adjusted_discovery_q3e = str(int(discovery_q3e_value) - 1)
                            row[i] = adjusted_discovery_q3e 


                        elif i in discovery_q3f_indices: 
                            discovery_q3f_value = row[i]
                            if discovery_q3f_value == '-9':
                                adjusted_discovery_q3f = '99'
                            elif discovery_q3f_value == '-1':
                                adjusted_discovery_q3f = 'a'
                            elif discovery_q3f_value == '-2':
                                adjusted_discovery_q3f = 'b'
                            else:
                                adjusted_discovery_q3f = str(int(discovery_q3f_value) - 1)
                            row[i] = adjusted_discovery_q3f  

                        elif i in discovery_q3f1_indices:
                            discovery_q3f1_value = row[i] 
                            adjusted_discovery_q3f1 = discovery_q3f1_value
                            row[i] = adjusted_discovery_q3f1      

                        elif i in discovery_q3e1_indices:
                            discovery_q3e1_value = row[i]
                            adjusted_discovery_q3e1 = discovery_q3e1_value
                            row[i] = adjusted_discovery_q3e1  

                        elif i in discovery_q4_indices: 
                            discovery_q4_value = row[i]
                            try:
                                if discovery_q4_value == '-9':
                                    adjusted_discovery_q4 = '99'
                                elif discovery_q4_value == '-1':
                                    adjusted_discovery_q4 = 'a'
                                elif discovery_q4_value == '-2':
                                    adjusted_discovery_q4 = 'b'
                                else:
                                    adjusted_discovery_q4 = str(int(discovery_q4_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q4 = ''  
                            row[i] = adjusted_discovery_q4

                        elif i in discovery_q5_indices: 
                            discovery_q5_value = row[i]
                            try:
                                if discovery_q5_value == '-9':
                                    adjusted_discovery_q5 = '99'
                                elif discovery_q5_value == '-1':
                                    adjusted_discovery_q5 = 'a'
                                elif discovery_q5_value == '-2':
                                    adjusted_discovery_q5 = 'b'
                                else:
                                    adjusted_discovery_q5 = str(int(discovery_q5_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q5 = ''  
                            row[i] = adjusted_discovery_q5

                        elif i in discovery_q6_indices: 
                            discovery_q6_value = row[i]
                            try:
                                if discovery_q6_value == '-9':
                                    adjusted_discovery_q6 = '99'
                                elif discovery_q6_value == '-1':
                                    adjusted_discovery_q6 = 'a'
                                elif discovery_q6_value == '-2':
                                    adjusted_discovery_q6 = 'b'
                                else:
                                    adjusted_discovery_q6 = str(int(discovery_q6_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q6 = ''  
                            row[i] = adjusted_discovery_q6 

                        elif i in discovery_q7_indices: 
                            discovery_q7_value = row[i]
                            try:
                                if discovery_q7_value == '-9':
                                    adjusted_discovery_q7 = '99'
                                elif discovery_q7_value == '-1':
                                    adjusted_discovery_q7 = 'a'
                                elif discovery_q7_value == '-2':
                                    adjusted_discovery_q7 = 'b'
                                else:
                                    adjusted_discovery_q7 = str(int(discovery_q7_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q7 = ''  
                            row[i] = adjusted_discovery_q7 

                        elif i in discovery_q8_indices: 
                            discovery_q8_value = row[i]
                            try:
                                if discovery_q8_value == '-9':
                                    adjusted_discovery_q8 = '99'
                                elif discovery_q8_value == '-1':
                                    adjusted_discovery_q8 = 'a'
                                elif discovery_q8_value == '-2':
                                    adjusted_discovery_q8 = 'b'
                                else:
                                    adjusted_discovery_q8 = str(int(discovery_q8_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q8 = ''  
                            row[i] = adjusted_discovery_q8  

                        elif i in discovery_q9_indices: 
                            discovery_q9_value = row[i]
                            try:
                                if discovery_q9_value == '1':
                                    adjusted_discovery_q9 = 'a'
                                elif discovery_q9_value == '2':
                                    adjusted_discovery_q9 = 'b'
                                elif discovery_q9_value == '-9':
                                    adjusted_discovery_q9 = '99'
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q9 = ''  
                            row[i] = adjusted_discovery_q9   

                        elif i in discovery_q10_indices: 
                            discovery_q10_value = row[i]
                            try:
                                if discovery_q10_value == '-9':
                                    adjusted_discovery_q10 = '99'
                                elif discovery_q10_value == '-1':
                                    adjusted_discovery_q10 = 'a'
                                elif discovery_q10_value == '-2':
                                    adjusted_discovery_q10 = 'b'
                                else:
                                    adjusted_discovery_q10 = str(int(discovery_q10_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q10 = ''  
                            row[i] = adjusted_discovery_q10

                        elif i in discovery_q11_indices: 
                            discovery_q11_value = row[i]
                            try:
                                if discovery_q11_value == '-9':
                                    adjusted_discovery_q11 = '99'
                                elif discovery_q11_value == '-1':
                                    adjusted_discovery_q11 = 'a'
                                elif discovery_q11_value == '-2':
                                    adjusted_discovery_q11 = 'b'
                                else:
                                    adjusted_discovery_q11 = str(int(discovery_q11_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q11 = ''  
                            row[i] = adjusted_discovery_q11

                        elif i in discovery_q12_indices: 
                            discovery_q12_value = row[i]
                            try:
                                if discovery_q12_value == '-9':
                                    adjusted_discovery_q12 = '99'
                                elif discovery_q12_value == '-1':
                                    adjusted_discovery_q12 = 'a'
                                elif discovery_q12_value == '-2':
                                    adjusted_discovery_q12 = 'b'
                                else:
                                    adjusted_discovery_q12 = str(int(discovery_q12_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q12 = ''  
                            row[i] = adjusted_discovery_q12

                        elif i in discovery_q13_indices: 
                            discovery_q13_value = row[i]
                            try:
                                if discovery_q13_value == '-9':
                                    adjusted_discovery_q13 = '99'
                                elif discovery_q13_value == '-1':
                                    adjusted_discovery_q13 = 'a'
                                elif discovery_q13_value == '-2':
                                    adjusted_discovery_q13 = 'b'
                                else:
                                    adjusted_discovery_q13 = str(int(discovery_q13_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q13 = ''  
                            row[i] = adjusted_discovery_q13

                        elif i in discovery_q14_indices: 
                            discovery_q14_value = row[i]
                            try:
                                if discovery_q14_value == '-9':
                                    adjusted_discovery_q14 = '99'
                                elif discovery_q14_value == '-1':
                                    adjusted_discovery_q14 = 'a'
                                elif discovery_q14_value == '-2':
                                    adjusted_discovery_q14 = 'b'
                                else:
                                    adjusted_discovery_q14 = str(int(discovery_q14_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q14 = ''  
                            row[i] = adjusted_discovery_q14  


                        elif i in discovery_q14a_indices: 
                            discovery_q14a_value = row[i]
                            try:
                                if discovery_q14a_value == '-9':
                                    adjusted_discovery_q14a = '99'
                                elif discovery_q14a_value == '-1':
                                    adjusted_discovery_q14a = 'a'
                                elif discovery_q14a_value == '-2':
                                    adjusted_discovery_q14a = 'b'
                                else:
                                    adjusted_discovery_q14a = str(int(discovery_q14a_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q14a = ''  
                            row[i] = adjusted_discovery_q14a

                        elif i in discovery_q14b_indices: 
                            discovery_q14b_value = row[i]
                            try:
                                if discovery_q14b_value == '-9':
                                    adjusted_discovery_q14b = '99'
                                elif discovery_q14b_value == '-1':
                                    adjusted_discovery_q14b = 'a'
                                elif discovery_q14b_value == '-2':
                                    adjusted_discovery_q14b = 'b'
                                else:
                                    adjusted_discovery_q14b = str(int(discovery_q14b_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q14b = ''  
                            row[i] = adjusted_discovery_q14b   


                        elif i in discovery_q14c_indices: 
                            discovery_q14c_value = row[i]
                            try:
                                if discovery_q14c_value == '-9':
                                    adjusted_discovery_q14c = '99'
                                elif discovery_q14c_value == '-1':
                                    adjusted_discovery_q14c = 'a'
                                elif discovery_q14c_value == '-2':
                                    adjusted_discovery_q14c = 'b'
                                else:
                                    adjusted_discovery_q14c = str(int(discovery_q14c_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q14c = ''  
                            row[i] = adjusted_discovery_q14c    


                        elif i in discovery_q14d_indices: 
                            discovery_q14d_value = row[i]
                            try:
                                if discovery_q14d_value == '-9':
                                    adjusted_discovery_q14d = '99'
                                elif discovery_q14d_value == '-1':
                                    adjusted_discovery_q14d = 'a'
                                elif discovery_q14d_value == '-2':
                                    adjusted_discovery_q14d = 'b'
                                else:
                                    adjusted_discovery_q14d = str(int(discovery_q14c_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q14d = ''  
                            row[i] = adjusted_discovery_q14d   


                        elif i in discovery_q14d1_indices: 
                            discovery_q14d1_value = row[i]   
                            adjusted_discovery_q14d1 = discovery_q14d1_value
                            row[i] = adjusted_discovery_q14d1   

                        elif i in discovery_q14e_indices: 
                            discovery_q14e_value = row[i]
                            try:
                                if discovery_q14e_value == '-9':
                                    adjusted_discovery_q14e = '99'
                                elif discovery_q14e_value == '-1':
                                    adjusted_discovery_q14e = 'a'
                                elif discovery_q14e_value == '-2':
                                    adjusted_discovery_q14e = 'b'
                                else:
                                    adjusted_discovery_q14e = str(int(discovery_q14e_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_discovery_q14e = ''  
                            row[i] = adjusted_discovery_q14e

                        elif i in discovery_q14e1_indices: 
                            discovery_q14e1_value = row[i]   
                            adjusted_discovery_q14e1 = discovery_q14e1_value
                            row[i] = adjusted_discovery_q14e1  



                        elif i in offer_q1_indices: 
                            offer_q1_value = row[i]
                            adjusted_offer_q1 = offer_q1_value
                            row[i] = adjusted_offer_q1     
                  
                        elif i in offer_q1a_indices: 
                            offer_q1a_value = row[i]
                            try:
                                if offer_q1a_value == '1':
                                    adjusted_offer_q1a = 'a'
                                elif offer_q1a_value == '2':
                                    adjusted_offer_q1a = 'b'
                                elif offer_q1a_value == '3':
                                    adjusted_offer_q1a = 'c'
                                elif offer_q1a_value == '-9':
                                    adjusted_offer_q1a = '99'                                   
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_offer_q1a = ''  
                            row[i] = adjusted_offer_q1a

                        elif i in offer_q1b_indices: 
                            offer_q1b_value = row[i]
                            try:
                                if offer_q1b_value == '1':
                                    adjusted_offer_q1b = 'a'
                                elif offer_q1b_value == '2':
                                    adjusted_offer_q1b = 'b'
                                elif offer_q1b_value == '3':
                                    adjusted_offer_q1b = 'c'
                                elif offer_q1b_value == '-9':
                                    adjusted_offer_q1b = '99' 
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_offer_q1b = ''  
                            row[i] = adjusted_offer_q1b 


                        elif i in offer_q1c_indices: 
                            offer_q1c_value = row[i]
                            try:
                                if offer_q1c_value == '1':
                                    adjusted_offer_q1c = 'a'
                                elif offer_q1c_value == '2':
                                    adjusted_offer_q1c = 'b'
                                elif offer_q1c_value == '3':
                                    adjusted_offer_q1c = 'c'
                                elif offer_q1c_value == '-9':
                                    adjusted_offer_q1c = '99' 
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_offer_q1c = ''  
                            row[i] = adjusted_offer_q1c  


                        elif i in offer_q2a_indices: 
                            offer_q2a_value = row[i]
                            try:
                                if offer_q2a_value == '-9':
                                    adjusted_offer_q2a = '99'
                                elif offer_q2a_value == '-1':
                                    adjusted_offer_q2a = 'a'
                                elif offer_q2a_value == '-2':
                                    adjusted_offer_q2a = 'b'
                                else:
                                    adjusted_offer_q2a = str(int(offer_q2a_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_offer_q2a = ''  
                            row[i] = adjusted_offer_q2a   


                        elif i in offer_q2b_indices: 
                            offer_q2b_value = row[i]
                            try:
                                if offer_q2b_value == '-9':
                                    adjusted_offer_q2b = '99'
                                elif offer_q2b_value == '-1':
                                    adjusted_offer_q2b = 'a'
                                elif offer_q2b_value == '-2':
                                    adjusted_offer_q2b = 'b'
                                else:
                                    adjusted_offer_q2b = str(int(offer_q2b_value) - 1)
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_offer_q2b = ''  
                            row[i] = adjusted_offer_q2b         

                        if i in offer_q2_1_indices:
                            offer_q2_1_value = row[i] 
                            if 'Offer_Q2_1_1' in header[i]:
                                combined_offer_q2_1 = offer_q2_1_value
                            elif 'Offer_Q2_1_2' in header[i]:
                                combined_offer_q2_1 += " " + offer_q2_1_value
                            row[i] = combined_offer_q2_1 

                        elif i in offer_q3_indices: 
                            offer_q3_value = row[i]
                            if offer_q3_value == '-9':
                                adjusted_offer_q3 = '99'
                            elif offer_q3_value == '-1':
                                adjusted_offer_q3 = 'a'
                            elif offer_q3_value == '-2':
                                adjusted_offer_q3 = 'b'
                            else:
                                adjusted_offer_q3 = str(int(offer_q3_value) - 1)
                            row[i] = adjusted_offer_q3  

                        elif i in follow_q1_indices: 
                            follow_q1_value = row[i]
                            if follow_q1_value == '-9':
                                adjusted_follow_q1 = '99'
                            elif follow_q1_value == '-1':
                                adjusted_follow_q1 = 'a'
                            elif follow_q1_value == '-2':
                                adjusted_follow_q1 = 'b'
                            else:
                                adjusted_follow_q1 = str(int(follow_q1_value) - 1)
                            row[i] = adjusted_follow_q1       


                        elif i in follow_q1_1_indices: 
                            follow_q1_1_value = row[i]
                            adjusted_follow_q1_1 = follow_q1_1_value
                            row[i] = adjusted_follow_q1_1   

                        
                        elif i in anonym_q1_indices: 
                            anonym_q1_value = row[i]
                            try:
                                if anonym_q1_value == '1':
                                    adjusted_anonym_q1 = 'a'
                                elif anonym_q1_value == '2':
                                    adjusted_anonym_q1 = 'b'
                                elif anonym_q1_value == '3':
                                    adjusted_anonym_q1 = 'c'
                                elif anonym_q1_value == '-9':
                                    adjusted_anonym_q1 = '99' 
                            except ValueError:
                                # Handle case value is not an integer
                                adjusted_anonym_q1 = ''  
                            row[i] = adjusted_anonym_q1         

                                                                          
                                                                  

                    for index in qual1_indices:
                        if index < len(row):
                            row[index] = combined_qual1.rstrip(',')  # Update Qual1 columns   

                    for index in qual_2_indices:
                        if index < len(row):
                            row[index] = adjusted_qual_2        
                   
                    for index in online_q1_indices:
                        if index < len(row):
                            row[index] = adjusted_online_q1 
                    
                    for index in online_q2_indices:
                        if index < len(row):
                            row[index] = adjusted_online_q2  

                    for index in crs_q1_indices:
                        if index < len(row):
                            row[index] = adjusted_crs_q1 

                    for index in crs_q2_indices:
                        if index < len(row):
                            row[index] = adjusted_crs_q2

                    for index in online_q3_indices:
                        if index < len(row):
                            row[index] = adjusted_online_q3

                    for index in improve_q1_indices:
                        if index < len(row):
                            row[index] = adjusted_improve_q1


                    for index in buy_q1_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q1

                    for index in buy_q2_li_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q2_li

                    for index in buy_q2_li_m_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q2_li_m

                    for index in buy_q3_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q3

                    for index in buy_q4a_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q4a

                    for index in buy_q4b_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q4b

                    for index in buy_q4a_li_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q4a_li

                    for index in buy_q5a_1b_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q5a_1b

                    for index in buy_q5a_2b_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q5a_2b

                    for index in buy_q5a_3b_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q5a_3b

                    for index in buy_q5b_1b_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q5b_1b

                    for index in buy_q5b_2b_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q5b_2b

                    for index in buy_q5b_3b_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q5b_3b

                    for index in buy_q5_li_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q5_li
               

                    for index in buy_q6_indices:
                        if index < len(row):
                            row[index] = combined_buy_q6.rstrip(',')  # Update Buy_Q6 columns
   
                    for index in discovery_q1_indices:
                        if index < len(row):
                            row[index] = combined_discovery_q1.rstrip(',')  # Update Buy_Q6 columns


                    for index in buy_q7a_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q7a      

                    for index in buy_q7b_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q7b

                    for index in buy_q7c_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q7c

                    for index in buy_q7d_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q7d

                    for index in buy_q7e_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q7e                                      

                    for index in buy_Q8_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q8 

                    for index in buy_q9_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q9 

                    for index in buy_q10_indices:
                        if index < len(row):
                            row[index] = adjusted_buy_q10         

                    for index in discovery_q2_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q2
                    for index in discovery_q3a_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3a
                    for index in discovery_q3b_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3b

                    for index in discovery_q3c_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3c  

                    for index in discovery_q3d_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3d  

                    for index in discovery_q3d1_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3d1          

                    for index in discovery_q3e_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3e 

                    for index in discovery_q3e1_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3e1  

                    for index in discovery_q3f_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3f      

                    for index in discovery_q3f1_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q3f1    

                    for index in discovery_q4_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q4   

                    for index in discovery_q5_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q5      

                    for index in discovery_q6_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q6

                    for index in discovery_q7_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q7

                    for index in discovery_q8_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q8

                    for index in discovery_q9_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q9

                    for index in discovery_q10_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q10

                    for index in discovery_q11_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q11

                    for index in discovery_q12_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q12   

                    for index in discovery_q13_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q13

                    for index in discovery_q14_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q14

                    for index in discovery_q14a_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q14a
                    
                    for index in discovery_q14b_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q14b 

                    for index in discovery_q14c_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q14c

                    for index in discovery_q14d_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q14d


                    for index in discovery_q14d1_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q14d1

                    for index in discovery_q14e_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q14e


                    for index in discovery_q14e1_indices:
                        if index < len(row):
                            row[index] = adjusted_discovery_q14e1  


                    for index in offer_q1_indices:
                        if index < len(row):
                            row[index] = adjusted_offer_q1     

                    for index in offer_q1a_indices:
                        if index < len(row):
                            row[index] = adjusted_offer_q1a 

                    for index in offer_q1b_indices:
                        if index < len(row):
                            row[index] = adjusted_offer_q1b                                           
                    
                    for index in offer_q1c_indices:
                        if index < len(row):
                            row[index] = adjusted_offer_q1c

                    for index in offer_q2a_indices:
                        if index < len(row):
                            row[index] = adjusted_offer_q2a 

                    for index in offer_q2b_indices:
                        if index < len(row):
                            row[index] = adjusted_offer_q2b 

                    for index in offer_q2_1_indices:
                        if index < len(row):
                            row[index] = combined_offer_q2_1 

                    for index in offer_q3_indices:
                        if index < len(row):
                            row[index] = adjusted_offer_q3

                    for index in follow_q1_indices:
                        if index < len(row):
                            row[index] = adjusted_follow_q1 

                    for index in follow_q1_1_indices:
                        if index < len(row):
                            row[index] = adjusted_follow_q1_1    

                    for index in anonym_q1_indices:
                        if index < len(row):
                            row[index] = adjusted_anonym_q1                               

                                                                

                    # Update the new Qual1 and Buy_Q6 columns .. etc
                    row.append(combined_qual1.rstrip(','))
                    row.append(adjusted_qual_2)
                    row.append(adjusted_online_q1)
                    row.append(adjusted_online_q2)
                    row.append(adjusted_crs_q1)
                    row.append(adjusted_crs_q2)
                    row.append(adjusted_online_q3)
                    row.append(adjusted_improve_q1)
                    row.append(adjusted_buy_q1)
                    row.append(adjusted_buy_q2_li)
                    row.append(adjusted_buy_q2_li_m)
                    row.append(adjusted_buy_q3)
                    row.append(adjusted_buy_q4a)
                    row.append(adjusted_buy_q4b)
                    row.append(adjusted_buy_q4a_li)
                    row.append(adjusted_buy_q5a_1b)
                    row.append(adjusted_buy_q5a_2b)
                    row.append(adjusted_buy_q5a_3b)
                    row.append(adjusted_buy_q5b_1b)
                    row.append(adjusted_buy_q5b_2b)
                    row.append(adjusted_buy_q5b_3b)
                    row.append(adjusted_buy_q5_li)
                    row.append(combined_buy_q6.rstrip(','))
                    row.append(adjusted_buy_q7a)
                    row.append(adjusted_buy_q7b)
                    row.append(adjusted_buy_q7c)
                    row.append(adjusted_buy_q7d)
                    row.append(adjusted_buy_q7e)
                    row.append(adjusted_buy_q8)
                    row.append(adjusted_buy_q9)
                    row.append(adjusted_buy_q10)
                    row.append(combined_discovery_q1.rstrip(','))
                    row.append(adjusted_discovery_q2)
                    row.append(adjusted_discovery_q3a)
                    row.append(adjusted_discovery_q3b)
                    row.append(adjusted_discovery_q3c)
                    row.append(adjusted_discovery_q3d)
                    row.append(adjusted_discovery_q3d1)
                    row.append(adjusted_discovery_q3e)
                    row.append(adjusted_discovery_q3e1)
                    row.append(adjusted_discovery_q3f)
                    row.append(adjusted_discovery_q3f1)
                    row.append(adjusted_discovery_q4)
                    row.append(adjusted_discovery_q5)
                    row.append(adjusted_discovery_q6)
                    row.append(adjusted_discovery_q7)
                    row.append(adjusted_discovery_q8)
                    row.append(adjusted_discovery_q9)
                    row.append(adjusted_discovery_q10)
                    row.append(adjusted_discovery_q11)
                    row.append(adjusted_discovery_q12)
                    row.append(adjusted_discovery_q13)
                    row.append(adjusted_discovery_q14)
                    row.append(adjusted_discovery_q14a)
                    row.append(adjusted_discovery_q14b)
                    row.append(adjusted_discovery_q14c)
                    row.append(adjusted_discovery_q14d)
                    row.append(adjusted_discovery_q14d1)
                    row.append(adjusted_discovery_q14e)
                    row.append(adjusted_discovery_q14e1)
                    row.append(adjusted_offer_q1)
                    row.append(adjusted_offer_q1a)
                    row.append(adjusted_offer_q1b)
                    row.append(adjusted_offer_q1c)
                    row.append(adjusted_offer_q2a)
                    row.append(adjusted_offer_q2b)
                    row.append(combined_offer_q2_1)
                    row.append(adjusted_offer_q3)
                    row.append(adjusted_follow_q1)
                    row.append(adjusted_follow_q1_1)
                    row.append(adjusted_anonym_q1)

                    print(row)

                    # Write the updated row to the output file with only the ID, Qual1, and Buy_Q6 columns
                    updated_row = [row[0], row[-71], row[-70], row[-69], row[-68], row[-67], row[-66], row[-65], row[-64], row[-63], row[-62], row[-61], row[-60], row[-59], row[-58], row[-57], row[-56], row[-55], row[-54], row[-53], row[-52], row[-51], row[-50], row[-49], row[-48], row[-47], row[-46], row[-45], row[-44], row[-43], row[-42], row[-41], row[-40], row[-39], row[-38], row[-37], row[-36], row[-35], row[-34], row[-33], row[-32], row[-31], row[-30], row[-29], row[-28], row[-27], row[-26], row[-25], row[-24], row[-23], row[-22], row[-21], row[-20], row[-19], row[-18], row [-17], row[-16], row[-15], row[-14], row[-13], row[-12], row[-11], row[-10], row[-9], row[-8], row[-7], row[-6], row[-5], row[-4], row[-3], row[-2], row[-1]]
                   
                    print(updated_row)

                    output.append(updated_row)

    
            # Convert the processed CSV to XML
            qual_column_name = 'Qual1'
            qual2_column_name = 'Qual2'
            online_q1_name = 'Online_Q1'
            online_q2_name = 'Online_Q2'
            crs_q1_name = 'CRS_Q1'
            crs_q2_name = 'CRS_Q2'
            online_q3_name = "Online_Q3"
            improve_q1_name = "Improve_Q1"
            buy_q1_name = "Buy_Q1"
            buy_q2_li_name = "Buy_Q2_LI"
            buy_q2_li_m_name = "Buy_Q2_LI_M"
            buy_q3_name = "Buy_Q3"
            buy_q4a_name = "Buy_Q4a"
            buy_q4b_name = "Buy_Q4b"
            buy_q4a_li_name = "Buy_Q4a_LI"
            buy_q5a_1b_name = "Buy_Q5a_1b"
            buy_q5a_2b_name = "Buy_Q5a_2b"
            buy_q5a_3b_name = "Buy_Q5a_3b"
            buy_q5b_1b_name = "Buy_Q5b_1b"
            buy_q5b_2b_name = "Buy_Q5b_2b"
            buy_q5b_3b_name = "Buy_Q5b_3b"
            buy_q5_li_name = "Buy_Q5_LI"
            buy_q6_column_name = 'Buy_Q6'

            buy_q7a_name = 'Buy_Q7a'
            buy_q7b_name = 'Buy_Q7b'
            buy_q7c_name = 'Buy_Q7c'
            buy_q7d_name = 'Buy_Q7d'
            buy_q7e_name = 'Buy_Q7e'

            discovery_q1_name = 'Discovery_Q1'
            discovery_q2_name = 'Discovery_Q2'
            discovery_q3a_name = 'Discovery_Q3a'
            discovery_q3b_name = 'Discovery_Q3b'

            discovery_q3c_name = 'Discovery_Q3c'
            discovery_q3d_name = 'Discovery_Q3d'
            discovery_q3d1_name = 'Discovery_Q3d1'
            discovery_q3e_name = 'Discovery_Q3e'
            discovery_q3e1_name = 'Discovery_Q3e1'

            discovery_q3f_name = 'Discovery_Q3f'
            discovery_q3f1_name = 'Discovery_Q3f1'

            discovery_q4_name = 'Discovery_Q4'
            discovery_q5_name = 'Discovery_Q5'
            discovery_q6_name = 'Discovery_Q6'
            discovery_q7_name = 'Discovery_Q7'
            discovery_q8_name = 'Discovery_Q8'
            discovery_q9_name = 'Discovery_Q9'
            discovery_q10_name = 'Discovery_Q10'
            discovery_q11_name = 'Discovery_Q11'
            discovery_q12_name = 'Discovery_Q12'
            discovery_q13_name = 'Discovery_Q13'
            discovery_q14_name = 'Discovery_Q14'
            discovery_q14a_name = 'Discovery_Q14a'
            discovery_q14b_name = 'Discovery_Q14b'
            discovery_q14c_name = 'Discovery_Q14c'
            discovery_q14d_name = 'Discovery_Q14d'
            discovery_q14d1_name = 'Discovery_Q14d1'
            discovery_q14e_name = 'Discovery_Q14e'
            discovery_q14e1_name = 'Discovery_Q14e1'

            offer_q1_name = 'Offer_Q1'
            offer_q1a_name = 'Offer_Q1a'
            offer_q1b_name = 'Offer_Q1b'
            offer_q1c_name = 'Offer_Q1c'
            offer_q2a_name = 'Offer_Q2a'
            offer_q2b_name = 'Offer_Q2b'

            offer_q2_1_name = 'Offer_q2_1'


            buy_Q8_name = 'Buy_Q8'
            buy_q9_name = 'Buy_Q9'
            buy_q10_name = 'Buy_Q10'

            offer_q3_name = 'Offer_Q3'
            follow_q1_name = 'Follow_Q1'
            follow_q1_1_name = 'Follow_Q1_1'
            anonym_q1_name = 'Anonym_Q1'

            xml_file_name = 'output.xml'

            root = ET.Element('data')
            for row in output[1:]:
                row_element = ET.SubElement(root, 'row')
                id_element = ET.SubElement(row_element, 'id')
                id_element.text = escape(row[0])

                qual1_element = ET.SubElement(row_element, qual_column_name)
                qual1_element.text = escape(row[1])

                qual2_element = ET.SubElement(row_element, qual2_column_name)
                qual2_element.text = row[2]
                
                online_q1_element = ET.SubElement(row_element, online_q1_name)
                online_q1_element.text = row[3]

                online_q2_element = ET.SubElement(row_element, online_q2_name)
                online_q2_element.text = row[4]

                crs_q1_element = ET.SubElement(row_element, crs_q1_name)
                crs_q1_element.text = row[5]

                crs_q2_element = ET.SubElement(row_element, crs_q2_name)
                crs_q2_element.text = row[6]

                online_q3_element = ET.SubElement(row_element, online_q3_name)
                online_q3_element.text = row[7]

                improve_q1_element = ET.SubElement(row_element, improve_q1_name)
                improve_q1_element.text = row[8]

                buy_q1_element = ET.SubElement(row_element, buy_q1_name)
                buy_q1_element.text = row[9]

                buy_q2_li_element = ET.SubElement(row_element, buy_q2_li_name)
                buy_q2_li_element.text = row[10]

                buy_q2_li_m_element = ET.SubElement(row_element, buy_q2_li_m_name)
                buy_q2_li_m_element.text = row[11]

                buy_q3_element = ET.SubElement(row_element, buy_q3_name)
                buy_q3_element.text = row[12]

                buy_q4a_element = ET.SubElement(row_element, buy_q4a_name)
                buy_q4a_element.text = row[13]

                buy_q4b_element = ET.SubElement(row_element, buy_q4b_name)
                buy_q4b_element.text = row[14]

                buy_q4a_li_element = ET.SubElement(row_element, buy_q4a_li_name)
                buy_q4a_li_element.text = row[15]

                buy_q5a_1b_element = ET.SubElement(row_element, buy_q5a_1b_name)
                buy_q5a_1b_element.text = row[16]

                buy_q5a_2b_element = ET.SubElement(row_element, buy_q5a_2b_name)
                buy_q5a_2b_element.text = row[17]

                buy_q5a_3b_element = ET.SubElement(row_element, buy_q5a_3b_name)
                buy_q5a_3b_element.text = row[18]

                buy_q5b_1b_element = ET.SubElement(row_element, buy_q5b_1b_name)
                buy_q5b_1b_element.text = row[19]

                buy_q5b_2b_element = ET.SubElement(row_element, buy_q5b_2b_name)
                buy_q5b_2b_element.text = row[20]

                buy_q5b_3b_element = ET.SubElement(row_element, buy_q5b_3b_name)
                buy_q5b_3b_element.text = row[21]

                buy_q5_li_element = ET.SubElement(row_element, buy_q5_li_name)
                buy_q5_li_element.text = row[22]

                buy_q6_element = ET.SubElement(row_element, buy_q6_column_name)
                buy_q6_element.text = escape(row[23])


                buy_q7a_element = ET.SubElement(row_element, buy_q7a_name)
                buy_q7a_element.text = escape(row[24])

                buy_q7b_element = ET.SubElement(row_element, buy_q7b_name)
                buy_q7b_element.text = escape(row[25])

                buy_q7c_element = ET.SubElement(row_element, buy_q7c_name)
                buy_q7c_element.text = escape(row[26])

                buy_q7d_element = ET.SubElement(row_element, buy_q7d_name)
                buy_q7d_element.text = escape(row[27])

                buy_q7e_element = ET.SubElement(row_element, buy_q7e_name)
                buy_q7e_element.text = escape(row[28])

                buy_Q8_element = ET.SubElement(row_element, buy_Q8_name)
                buy_Q8_element.text = row[29]

                buy_q9_element = ET.SubElement(row_element, buy_q9_name)
                buy_q9_element.text = row[30]

                buy_q10_element = ET.SubElement(row_element, buy_q10_name)
                buy_q10_element.text = row[31]

                discovery_q1_element = ET.SubElement(row_element, discovery_q1_name)
                discovery_q1_element.text = escape(row[32])

                discovery_q2_element = ET.SubElement(row_element, discovery_q2_name)
                discovery_q2_element.text = row[33]
            
                discovery_q3a_element = ET.SubElement(row_element, discovery_q3a_name)
                discovery_q3a_element.text = row[34]

                discovery_q3b_element = ET.SubElement(row_element, discovery_q3b_name)
                discovery_q3b_element.text = row[35]

                discovery_q3c_element = ET.SubElement(row_element, discovery_q3c_name)
                discovery_q3c_element.text = row[36]

                discovery_q3d_element = ET.SubElement(row_element, discovery_q3d_name)
                discovery_q3d_element.text = row[37]
                
                discovery_q3d1_element = ET.SubElement(row_element, discovery_q3d1_name)
                discovery_q3d1_element.text = row[38]

                discovery_q3e_element = ET.SubElement(row_element, discovery_q3e_name)
                discovery_q3e_element.text = row[39]

                discovery_q3e1_element = ET.SubElement(row_element, discovery_q3e1_name)
                discovery_q3e1_element.text = row[40]

                discovery_q3f_element = ET.SubElement(row_element, discovery_q3f_name)
                discovery_q3f_element.text = row[41]

                discovery_q3f1_element = ET.SubElement(row_element, discovery_q3f1_name)
                discovery_q3f1_element.text = row[42]

                discovery_q4_element = ET.SubElement(row_element, discovery_q4_name)
                discovery_q4_element.text = row[43]

                discovery_q5_element = ET.SubElement(row_element, discovery_q5_name)
                discovery_q5_element.text = row[44]

                discovery_q6_element = ET.SubElement(row_element, discovery_q6_name)
                discovery_q6_element.text = row[45]

                discovery_q7_element = ET.SubElement(row_element, discovery_q7_name)
                discovery_q7_element.text = row[46]

                discovery_q8_element = ET.SubElement(row_element, discovery_q8_name)
                discovery_q8_element.text = row[47]

                discovery_q9_element = ET.SubElement(row_element, discovery_q9_name)
                discovery_q9_element.text = row[48]

                discovery_q10_element = ET.SubElement(row_element, discovery_q10_name)
                discovery_q10_element.text = row[49]

                discovery_q11_element = ET.SubElement(row_element, discovery_q11_name)
                discovery_q11_element.text = row[50]

                discovery_q12_element = ET.SubElement(row_element, discovery_q12_name)
                discovery_q12_element.text = row[51]

                discovery_q13_element = ET.SubElement(row_element, discovery_q13_name)
                discovery_q13_element.text = row[52]

                discovery_q14_element = ET.SubElement(row_element, discovery_q14_name)
                discovery_q14_element.text = row[53]

                discovery_q14a_element = ET.SubElement(row_element, discovery_q14a_name)
                discovery_q14a_element.text = row[54]

                discovery_q14b_element = ET.SubElement(row_element, discovery_q14b_name)
                discovery_q14b_element.text = row[55]

                discovery_q14c_element = ET.SubElement(row_element, discovery_q14c_name)
                discovery_q14c_element.text = row[56]

                discovery_q14d_element = ET.SubElement(row_element, discovery_q14d_name)
                discovery_q14d_element.text = row[57]

                discovery_q14d1_element = ET.SubElement(row_element, discovery_q14d1_name)
                discovery_q14d1_element.text = row[58]

                discovery_q14e_element = ET.SubElement(row_element, discovery_q14e_name)
                discovery_q14e_element.text = row[59]

                discovery_q14e1_element = ET.SubElement(row_element, discovery_q14e1_name)
                discovery_q14e1_element.text = row[60]


                offer_q1_element = ET.SubElement(row_element, offer_q1_name)
                offer_q1_element.text = row[61]

                offer_q1a_element = ET.SubElement(row_element, offer_q1a_name)
                offer_q1a_element.text = row[62]

                offer_q1b_element = ET.SubElement(row_element, offer_q1b_name)
                offer_q1b_element.text = row[63]

                offer_q1c_element = ET.SubElement(row_element, offer_q1c_name)
                offer_q1c_element.text = row[64]

                offer_q2a_element = ET.SubElement(row_element, offer_q2a_name)
                offer_q2a_element.text = row[65]

                offer_q2b_element = ET.SubElement(row_element, offer_q2b_name)
                offer_q2b_element.text = row[66]

                offer_q2_1_element = ET.SubElement(row_element,  offer_q2_1_name)
                offer_q2_1_element.text = row[67]

                offer_q3_element = ET.SubElement(row_element,  offer_q3_name)
                offer_q3_element.text = row[68]

                follow_q1_element = ET.SubElement(row_element,  follow_q1_name)
                follow_q1_element.text = row[69]

                follow_q1_1_element = ET.SubElement(row_element,  follow_q1_1_name)
                follow_q1_1_element.text = row[70]

                anonym_q1_element = ET.SubElement(row_element,  anonym_q1_name)
                anonym_q1_element.text = row[71]
   

               
            # xml_content = ET.tostring(root, encoding='utf-8', method='xml').decode()

            xml_content = ET.tostring(root, encoding='ISO-8859-1', method='xml').decode()
                

            with open(xml_file_name, 'w') as xml_file:
                xml_file.write(xml_content)

            # Set the headers to force download
            with open(xml_file_name, 'rb') as file:
                response = HttpResponse(file, content_type='application/xml')
                response['Content-Disposition'] = f'attachment; filename="{xml_file_name}"'
                return response


        else:
            return HttpResponse("No file selected.")
    else:
        return render(request, 'csv_to_xml.html')