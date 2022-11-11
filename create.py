import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
  "Code": 3420,
  "Course": "企業資源規劃",
  "Leacture": "莊育維",
  "Room":"靜宜大學",
  "Time":"四2 3 4",
},

{
  "Code": 3421,
  "Course": "行銷管理",
  "Leacture": "顏永森",
  "Room":"靜宜大學",
  "Time":"四2 3 4",
},

{
  "Code": 3422,
  "Course": "程式語言",
  "Leacture": "鄭婉淑",
  "Room":"靜宜大學",
  "Time":"五 2 3 4",
},

{
  "Code": 3423,
  "Course": "行動電子商務",
  "Leacture": "康贊清",
  "Room":"靜宜大學",
  "Time":"三 7 8 9",
},

{
  "Code": 3424,
  "Course": "網頁前端程式設計",
  "Leacture": "胡育誠",
  "Room":"靜宜大學",
  "Time":"三 2 3 4",
},

{
  "Code": 3425,
  "Course": "物聯網概論",
  "Leacture": "王耀德",
  "Room":"靜宜大學",
  "Time":"三 7 8 9",
}

]

#doc_ref = db.collection("靜宜資管").document("tcyang")
#doc_ref.set(doc)
collection_ref = db.collection("111")
for doc in docs:
  collection_ref.add(doc)

