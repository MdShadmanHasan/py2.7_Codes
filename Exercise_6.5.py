str = 'X-DSPAM-Confidence: 0.8475'
colon_position = str.find(':')
extracted_string = str[colon_position+1:]
extracted_number = extracted_string.strip()
float_value = float(extracted_number)
print float_value
#print extracted_number
