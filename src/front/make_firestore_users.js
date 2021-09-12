var firebase = require("firebase/app")
require('firebase/firestore')

const firebaseConfig = {
  apiKey: "AIzaSyBUBFnHLfz_evRY_w_hG7jvWfzG4h4GR3U",
  authDomain: "drf-firebase-admin.firebaseapp.com",
  projectId: "drf-firebase-admin",
  storageBucket: "drf-firebase-admin.appspot.com",
  messagingSenderId: "690248261249",
  appId: "1:690248261249:web:31a187d0a27eb7c2763780",
};

firebase.default.initializeApp(firebaseConfig);
var db = firebase.default.firestore();

const fs = require('fs');

const jsonObject = JSON.parse(fs.readFileSync('./users.json', 'utf8'));

jsonObject.forEach((obj) => {
    db.collection("users").add(obj)
});