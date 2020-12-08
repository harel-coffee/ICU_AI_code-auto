# coding: utf-8

import os,glob
import pandas as pd
import datetime

BEFORE_SEC = -86400
AFTER_SEC = 86400

basic_info = {}
basic_list = ["pID","Age","Sex","Blood_ABO","Blood_Rh","department","height","weight","Ent_datetime",
			"Exit_datetime","days_of_stay","Ent_diagnosis","Current_diagnosis","body_restraint","ambulance",
			"introduction","MET","Ent_route","AIDS","AML_MM","Heart_failure","Lymphoma","Respiratory_failure",
			"Metastasis","Liver_failure","Immunosuppression","Cirrhosis","Maintenance_dialysis",
			"Cardiac_arrest_resuscitation","Accute_DIC","SOFA_score","apache2_score","apache2_est_mortality",
			"SIRS_score","FIM_score","outcome1","outcome2","Severity_of_sepsis"]
basic_change_no = ["AIDS","AML_MM","Heart_failure","Lymphoma","Respiratory_failure","Metastasis",
			"Liver_failure","Immunosuppression","Cirrhosis","Maintenance_dialysis",
			"Cardiac_arrest_resuscitation","Accute_DIC","SOFA_score","apache2_score",
			"apache2_est_mortality","SIRS_score","FIM_score"]
blood_info = {}
blood_list = {
			"150029": "GOT",
			"150030": "GPT",
			"150031": "LDH",
			"150032": "ALP",
			"150034": "G-GTP",
			"150035": "CHE",
			"150036": "AMY",
			"150037": "CPK",
			"150038": "TP ",
			"150039": "Alb",
			"150040": "UA",
			"150041": "UN",
			"150042": "CRE",
			"150043": "T-Bil",
			# "150044": "D-Bil",
			"150045": "Na",
			"150046": "K",
			"150047": "Cl",
			"150048": "Ca",
			"150049": "T-CHO",
			"150057": "CRP",
			"150064": "ammonia",
			"150022": "APTT",
			"150026": "PT-SEC",
			"150027": "PT-PER",
			"150028": "PT-INR",
			"150001": "WBC",
			"150002": "RBC",
			"150003": "HGB",
			"150004": "HCT",
			"150005": "MCV",
			"150006": "MCH",
			"150007": "MCHC",
			"150008": "RDW",
			"150009": "PLT",
			"150010": "PCT",
			"150011": "MPV",
			"150012": "PDW",
			"150024": "FDP",
			"150025": "AT3",
			"150014": "ST",
			"150015": "SEG",
			"150016": "EO",
			"150017": "BA",
			"150018": "MO",
			"150019": "LY",
			"150020": "ERYTHR.B",
			"150023": "FG",
			"150013": "MYEL",
			"150021": "ANISO",
			"151001": "pH",
			"151002": "pCO2",
			"151003": "pO2",
			"151004": "HCO3-",
			"151005": "TCO2",
			"151006": "BEecf",
			"151007": "BE_B",
			"151008": "SO2",
			"151009": "SO2C",
			"151010": "THb",
			"151011": "THbc",
			"151012": "Hct",
			"151013": "Na+",
			"151014": "K+",
			"151015": "Cl-",
			"151016": "Ca++",
			"151017": "AG",
			"151018": "Glu",
			"151019": "Lac",
			"151020": "O2Hb",
			"151021": "COHb",
			"151022": "Methb",
			"151023": "HHb",
			"150063": "IL-6",
			"150061": "FER",
			"150058": "B-D_glucan",
			"150059": "endotoxin",
			"150060": "BNP",
			"150065": "KL-6",
			"150067": "Mg",
			"150068": "I-P",
			"150085": "C-Bil",
			"100699021": "nan",
			"151024": "ACT",
			"150086": "request_to_clinical_laboratory",
			"150066": "HLADR",
			"150055": "cGlu",
			"150069": "TG",
			"150087": "confirmed_doctor",
			"151025": "measurement_category",
			"151026": "SerumPCT",
			"150088": "D-dimer",
			"150089": "APTT-Sec",
			"150090": "APTT-ratio",
}
blood_changed_list = []
vital_info = {}
vital_list = {
			"10001": "HR",
			"10003": "Pulse",
			"10022": "RR",
			"10024": "SpO2",
			"10006": "ARTs",
			"10007": "ARTm",
			"10008": "ARTd",
			"10017": "CVP",
			"10026": "T1",
			"10023": "etCO2",
			"10009": "NBPs",
			"10011": "NBPd",
			"10030": "axillary_temperature",
			"10028": "T2",
			"11022": "rResp_imp",
			"10410": "RESP_co2",
			"10020": "CCO",
			"10012": "PAPs",
			"10014": "PAPd",
			"10021": "CCI",
			"10018": "CO",
			"10019": "CI",
			"10090": "BIS",
			"10091": "SR (bis)",
			"10092": "SQI (bis)",
			"10093": "EMG (bis)",
			"10094": "SEF95 (bis)",
			"11242": "SvO2_CCO",
			"11081": "TB_CCO",
			"340030": "GEF (PICCO)",
			"340062": "PPV (PICCO)",
			"340011": "CI (PICCO)",
			"340012": "CO (PICCO)",
			"340020": "Dot_ID_low_PICCO",
			"340025": "EVLW (PICCO)",
			"340026": "ELWI (PICCO)",
			"340028": "GEDV (PICCO)",
			"340029": "GEDI (PICCO)",
			"340036": "ITBV (PICCO)",
			"340037": "ITBI (PICCO)",
			"340059": "PCCI (PICCO)",
			"340060": "PCCO (PICCO)",
			"340063": "PVPI (PICCO)",
			"340086": "SV (PICCO)",
			"340087": "SVI (PICCO)",
			"340091": "SVR (PICCO)",
			"340092": "SVRI (PICCO)",
			"340093": "SVV (PICCO)",
			"11223": "CCOSV",
			"10307": "ART_2s",
			"10309": "ART_2m",
			"10348": "ICPm",
			"10308": "ART_2d",
			"10013": "PAPm",
			"19013": "SVV(Vigileo)",
			"19009": "rSO2-1(INVOS)",
			"19010": "rSO2-2(INVOS)",
			"19011": "rSO2-3(INVOS)",
			"19012": "rSO2-4(INVOS)",
			"10027": "TBlood",
			"11570": "SVV",
			"11569": "ScvO2",
			# "10071": "CPP",
			# "11232": "SvO2",
}
bed_info = {}
bed_list = {
	"1": "A1",
	"2": "A2",
	"3": "A3",
	"4": "A4",
	"5": "A5",
	"6": "A6",
	"7": "A7",
	"8": "A8",
	"9": "C1",
	"10": "C2",
	"11": "C3",
	"12": "C4",
	"13": "C5",
	"14": "C6",
	"15": "B1",
	"16": "B2",
	"17": "B3",
	"18": "B4",
	"19": "B5",
	"20": "B6",
	"21": "B7",
	"22": "B8",
	"101": "Ward1",
	"102": "Ward2",
	"103": "Ward3",
	"104": "Ward4",
	"105": "Ward5",
	"106": "Ward6",
	"107": "Ward7",
	"108": "Ward8",
	"109": "Ward9",
	"110": "Ward10",
	"201": "EROPE",
	"202": "ER1",
	"203": "ER2",
	"205": "Emergency5",
	"208": "Emergency8",
	"210": "Emergency10",
	"991": "Temporary1",
	"992": "Temporary2",
	"9991": "Emergency_Temporary1",
	"9992": "Emergency_Temporary2",
	"9993": "Emergency_Temporary3"
}
error_info = {}
error_count = 0

cwd = os.getcwd()

if not os.path.isdir(cwd+"/patient"):
	os.mkdir(cwd+"/patient")
if not os.path.isdir(cwd+"/patient_error"):
	os.mkdir(cwd+"/patient_error")

data_path = "/Volumes/LaCie/work/ICU_data"
os.chdir(data_path)

dir1 = glob.glob("Date_*")
print(dir1)

for d1 in dir1:
	os.chdir(data_path+"/"+d1)
	dir2 = glob.glob("20*")
	for d2 in dir2:
		val_ent_date = None
		val_exit_date = None
		print(d2)
		case_dir = data_path+"/"+d1+"/"+d2
		os.chdir(case_dir)
		case_id = d2
		try:
			line_no = 0
			# patient attribute information
			file_name = "患者属性情報.csv"
			# df = pd.read_csv(file_name,sep=",",encoding="Shift_JISx0213")
			df = pd.read_csv(file_name,sep=",")
			basic_info[case_id] = {}
			for i in range(len(df)):
				line_no = i + 1
				line = list(df.iloc[i,:])
				val = str(line[5]).replace("\t", " ")
				if line[2] == "患者ID":
					basic_info[case_id]["pID"] = val
				elif line[2] == "生年月日":
					tmp_date = str(val)
					if tmp_date != "nan":
						birth = datetime.date(int(tmp_date[0:4]),int(tmp_date[4:6]),int(tmp_date[6:8]))
					else:
						birth = "NA"
				elif line[2] == "性別":
					if val == "女性":
						basic_info[case_id]["Sex"] = "F"
					elif val == "男性":
						basic_info[case_id]["Sex"] = "M"
					else:
						basic_info[case_id]["Sex"] = "Unknown"
				elif line[2] == "血液型ABO":
					basic_info[case_id]["Blood_ABO"] = val
				elif line[2] == "血液型Rh":
					if 'Rh' in val:
						basic_info[case_id]["Blood_Rh"] = val.replace('(','_').replace(')','')
					else:
						basic_info[case_id]["Blood_Rh"] = "Unknown"
				elif line[2] == "診療科":
					basic_info[case_id]["department"] = val
				elif line[2] == "身長":
					basic_info[case_id]["height"] = val
				elif line[2] == "体重":
					basic_info[case_id]["weight"] = val
				elif line[2] == "入室日時管理用（日）":
					val_ent_date = str(val).strip()
				elif line[2] == "入室日時管理用（時刻）":
					val_ent_time = str(val).strip()
				elif line[2] == "退室日時管理用（日）":
					val_exit_date = str(val).strip()
				elif line[2] == "退室日時管理用（時刻）":
					val_exit_time = str(val).strip()
				elif line[2] == "入室時診断":
					basic_info[case_id]["Ent_diagnosis"] = val
				elif line[2] == "現診断":
					basic_info[case_id]["Current_diagnosis"] = val
				elif line[2] == "身体拘束":
					basic_info[case_id]["body_restraint"] = val
				elif line[2] == "救急車利用":
					basic_info[case_id]["ambulance"] = val
				elif line[2] == "他院の紹介":
					basic_info[case_id]["introduction"] = val
				elif line[2] == "MET有無":
					basic_info[case_id]["MET"] = val
				elif line[2] == "入室経路":
					basic_info[case_id]["Ent_route"] = val
				elif line[2] == "AIDS":
					basic_info[case_id]["AIDS"] = val
				elif line[2] == "AML/MM":
					basic_info[case_id]["AML_MM"] = val
				elif line[2] == "心不全":
					basic_info[case_id]["Heart_failure"] = val
				elif line[2] == "肝不全":
					basic_info[case_id]["Liver_failure"] = val
				elif line[2] == "呼吸不全":
					basic_info[case_id]["Respiratory_failure"] = val
				elif line[2] == "癌転移":
					basic_info[case_id]["Metastasis"] = val
				elif line[2] == "ﾘﾝﾊﾟ種":
					basic_info[case_id]["Lymphoma"] = val
				elif line[2] == "肝硬変":
					basic_info[case_id]["Cirrhosis"] = val
				elif line[2] == "免疫抑制":
					basic_info[case_id]["Immunosuppression"] = val
				elif line[2] == "維持透析":
					basic_info[case_id]["Maintenance_dialysis"] = val
				elif line[2] == "心停止蘇生後":
					basic_info[case_id]["Cardiac_arrest_resuscitation"] = val
				elif line[2] == "急性期DIC":
					basic_info[case_id]["Accute_DIC"] = val
				elif line[2] == "SOFAスコア":
					basic_info[case_id]["SOFA_score"] = val
				elif line[2] == "SIRSスコア":
					basic_info[case_id]["SIRS_score"] = val
				elif line[2] == "apache2スコア":
					basic_info[case_id]["apache2_score"] = val
				elif line[2] == "apache2推定死亡率":
					basic_info[case_id]["apache2_est_mortality"] = val
				elif line[2] == "FIMスコア":
					basic_info[case_id]["FIM_score"] = val
				elif line[2] == "退室状況":
					basic_info[case_id]["outcome1"] = val
				elif line[2] == "転帰":
					basic_info[case_id]["outcome2"] = val
				elif line[2] == "経過中敗血症重症度コード":
					basic_info[case_id]["Severity_of_sepsis"] = val

			line_no = 0
			# basic information
			file_name = "基本情報.csv"
			# df2 = pd.read_csv(file_name,sep=",",encoding="Shift_JISx0213")
			df2 = pd.read_csv(file_name,sep=",")
			line = list(df2.iloc[0,:])
			val = str(line[5]).replace("\t", " ")
			basic_info[case_id]["Age"] = val
			
			ent_datetime = None
			if val_ent_date is not None and val_ent_time != '':
				int_ent_date = int(float(val_ent_date))
				int_ent_year = int_ent_date // 10000
				int_ent_month = int_ent_date // 100 % 100
				int_ent_day = int_ent_date % 100
				int_ent_time = int(float(val_ent_time[:4]))
				int_ent_hour = int_ent_time // 100
				int_ent_minute = int_ent_time % 100
				ent_datetime = datetime.datetime(int_ent_year, int_ent_month, int_ent_day,\
					int_ent_hour, int_ent_minute)
				basic_info[case_id]["Ent_datetime"] = ent_datetime.strftime('%Y-%m-%d %H:%M')
				
			exit_datetime = None
			if val_exit_date is not None and val_exit_time != '':
				int_exit_date = int(float(val_exit_date))
				int_exit_year = int_exit_date // 10000
				int_exit_month = int_exit_date // 100 % 100
				int_exit_day = int_exit_date % 100
				int_exit_time = int(float(val_exit_time[:4]))
				int_exit_hour = int_exit_time // 100
				int_exit_minute = int_exit_time % 100
				exit_datetime = datetime.datetime(int_exit_year, int_exit_month, int_exit_day,\
					int_exit_hour, int_exit_minute)
				basic_info[case_id]["Exit_datetime"] = exit_datetime.strftime('%Y-%m-%d %H:%M')

			if ent_datetime is not None and exit_datetime is not None:
				basic_info[case_id]["days_of_stay"] = int((exit_datetime - ent_datetime).total_seconds()) // 86400

			line_no = 0
			# result of blood test
			file_name = "検査結果値.csv"
			df3 = pd.read_csv(file_name,sep=",",encoding="Shift_JISx0213")
			a3 = df3.values
			blood_info[case_id] = {}
			for i in range(len(a3)):
				line_no = i + 1
				line = list(a3[i])
				val = str(line[5]).replace("\t", " ")
				if len(val) > 0 and val[-1] in ["H", "L", "?"]:
					val = val[:-1]
				if len(val) > 0 and val[0] in [">", "<"]:
					val = val[1:]
				str_started_at = str(line[4])
				str_code = str(line[1])
				if len(str_started_at) == 14 is not None and str_code in blood_list:
					started_at_datetime = datetime.datetime(int(str_started_at[:4]),int(str_started_at[4:6]),int(str_started_at[6:8]),\
						int(str_started_at[8:10]),int(str_started_at[10:12]),int(str_started_at[12:14]))
					elapsed_seconds = (started_at_datetime - ent_datetime).total_seconds()
					if BEFORE_SEC <= elapsed_seconds and elapsed_seconds <= AFTER_SEC:
						if str_code not in blood_info[case_id]:
							blood_info[case_id][str_code] = (elapsed_seconds, val)
						elif blood_info[case_id][str_code][0] < elapsed_seconds:
							blood_info[case_id][str_code] = (elapsed_seconds, val)
			line_no = 0
			# vital data
			file_name = "バイタルデータ.csv"
			df4 = pd.read_csv(file_name,sep=",",encoding="Shift_JISx0213",low_memory=False)
			a4 = df4.values
			vital_info[case_id] = {}
			for i in range(len(a4)):
				line_no = i + 1
				line = list(a4[i])
				val = str(line[5]).replace("\t", " ")
				str_started_at = str(line[4])
				str_code = str(line[1])
				if len(str_started_at) == 14 is not None and str_code in vital_list:
					started_at_datetime = datetime.datetime(int(str_started_at[:4]),int(str_started_at[4:6]),int(str_started_at[6:8]),\
						int(str_started_at[8:10]),int(str_started_at[10:12]),int(str_started_at[12:14]))
					elapsed_seconds = (started_at_datetime - ent_datetime).total_seconds()
					if BEFORE_SEC <= elapsed_seconds and elapsed_seconds <= AFTER_SEC:
						if str_code not in vital_info[case_id]:
							vital_info[case_id][str_code] = (elapsed_seconds, val)
						elif vital_info[case_id][str_code][0] < elapsed_seconds:
							vital_info[case_id][str_code] = (elapsed_seconds, val)
			line_no = 0
			# information about entry time and exit time
			file_name = "入退室情報.csv"
			df5 = pd.read_csv(file_name,sep=",",encoding="Shift_JISx0213",low_memory=False)
			a5 = df5.values
			bed_info[case_id] = {}
			for i in range(len(a5)):
				line_no = i + 1
				line = list(a5[i])
				str_started_at = str(line[3])
				str_ended_at = str(line[4])
				str_code = str(line[1])
				if len(str_started_at) == 14 is not None and str_code in bed_list:
					started_at_datetime = datetime.datetime(int(str_started_at[:4]),int(str_started_at[4:6]),int(str_started_at[6:8]),\
						int(str_started_at[8:10]),int(str_started_at[10:12]),int(str_started_at[12:14]))
					ended_at_datetime = ent_datetime + datetime.timedelta(hours=24)
					if str_ended_at != '99999999999999':
						ead = datetime.datetime(int(str_ended_at[:4]),int(str_ended_at[4:6]),int(str_ended_at[6:8]),\
							int(str_ended_at[8:10]),int(str_ended_at[10:12]),int(str_ended_at[12:14]))
						if ended_at_datetime > ead:
							ended_at_datetime = ead
					elapsed_seconds_started = (started_at_datetime - ent_datetime).total_seconds()
					elapsed_seconds_ended = (ended_at_datetime - ent_datetime).total_seconds()
					if (BEFORE_SEC <= elapsed_seconds_started and elapsed_seconds_started <= AFTER_SEC) or \
						(BEFORE_SEC <= elapsed_seconds_ended and elapsed_seconds_ended < AFTER_SEC):
						bed_minutes = (ended_at_datetime - started_at_datetime).total_seconds() // 60
						if str_code not in bed_info[case_id]:
							bed_info[case_id][str_code] = bed_minutes
						else:
							bed_info[case_id][str_code] += bed_minutes

		except Exception as e:
			error_count += 1
			print("*** error occured ***")
			print(e)
			error_info[case_id] = {}
			error_info[case_id]["file_name"] = file_name
			error_info[case_id]["line_no"] = line_no
			error_info[case_id]["error"] = e

os.chdir(cwd)

with open("patient/ICU_patient_info_summarized4.txt","w") as fo:
	for item in basic_list:
		if item == "pID":
			fo.write(item)
		else:
			fo.write("\t"+item)
	for key in blood_list:
		item = blood_list[key]
		blood_changed_list.append(item)
		fo.write("\t"+item)
	for key in vital_list:
		item = vital_list[key]
		fo.write("\t"+item)
	for key in bed_list:
		item = bed_list[key]
		fo.write("\t"+"bed_"+item)
	fo.write("\n")
	# data
	for case_id in basic_info:
		for item in basic_list:
			if item == "pID":
				if item not in basic_info[case_id]:
					fo.write('NA')
				else:
					fo.write(str(basic_info[case_id][item]))
			else:
				if item not in basic_info[case_id]:
					if item in basic_change_no:
						fo.write('\tNo')
					else:
						fo.write('\tNA')
				else:
					fo.write('\t'+str(basic_info[case_id][item]))
		for key in blood_list:
			if key not in blood_info[case_id]:
				fo.write('\tNA')
			else:
				fo.write('\t'+str(blood_info[case_id][key][1]))
		for key in vital_list:
			if key not in vital_info[case_id]:
				fo.write('\tNA')
			else:
				fo.write('\t'+str(vital_info[case_id][key][1]))
		for key in bed_list:
			if key not in bed_info[case_id]:
				fo.write('\tNA')
			else:
				fo.write('\t'+str(bed_info[case_id][key]))
		fo.write("\n")

with open("patient/ICU_patient_info_summarized_tested4.txt","w") as fo:
	# column
	fo.write("pID")
	fo.write("\tEnt_datetime")
	for item in basic_change_no:
		fo.write("\t"+item+"_tested")
	for item in blood_changed_list:
		fo.write("\t"+item+"_tested")
	fo.write("\n")
	# data
	for case_id in basic_info:
		fo.write(basic_info[case_id]["pID"])
		fo.write("\t"+str(basic_info[case_id]["Ent_datetime"]))
		for item in basic_change_no:
			if item in basic_info[case_id]:
				fo.write("\t1")
			else:
				fo.write("\t0")
		for item in blood_list:
			if item in blood_info[case_id]:
				fo.write("\t1")
			else:
				fo.write("\t0")
		fo.write("\n")

with open("patient_error/ICU_patient_info_error2.txt","w") as fo:
	for case_id in error_info:
		fo.write("{case_id}\t{file_name}\tline:{line_no}\t{error}\n"\
			.format(case_id=case_id, file_name=error_info[case_id]["file_name"],\
			line_no=error_info[case_id]["line_no"], error=error_info[case_id]["error"]))

print("\ndone.\nerror count:"+str(error_count))