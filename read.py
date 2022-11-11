import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

cond = input("請輸入課程關鍵字:")
cond = input("\n請輸入教師關鍵字:")
collection_ref = db.collection("111")
docs = collection_ref.get()
result = ""
for doc in docs:
	dict = doc.to_dict()
	if cond in dict["Course"]:
		#print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
		result += dict["Leacture"] + "老師開的" + dict["Course"] + "課程,每週"
		result += dict["Time"] + "於" + dict["Room"] + "上課\n"
print(result)

