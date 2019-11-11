import firebase_admin
import os

from firebase_admin import firestore
from firebase_admin import credentials

from dotenv import load_dotenv
load_dotenv()

POST_COLLECTION_NAME = u'posts'

cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIALS_FILE'))

firebase_admin.initialize_app(cred, {
    'projectId': os.getenv('FIREBASE_PROJECT_ID'),
})

db = firestore.client()
posts_collection = db.collection(POST_COLLECTION_NAME)

def writePost(post):
    doc_ref = posts_collection.document(post.id)
    doc_ref.set({
        u'content': post.content
    })