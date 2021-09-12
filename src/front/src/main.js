import Vue from 'vue'
import App from './App.vue'
import axios from 'axios' //追記
import VueAxios from 'vue-axios' //追記
import router from "./router"

var AWS = require('aws-sdk');
var firebase = require("firebase/app")

const firebaseConfig = {
  apiKey: "AIzaSyBUBFnHLfz_evRY_w_hG7jvWfzG4h4GR3U",
  authDomain: "drf-firebase-admin.firebaseapp.com",
  projectId: "drf-firebase-admin",
  storageBucket: "drf-firebase-admin.appspot.com",
  messagingSenderId: "690248261249",
  appId: "1:690248261249:web:31a187d0a27eb7c2763780",
};

firebase.default.initializeApp(firebaseConfig);

AWS.config.update(
  {
    "accessKeyId": "AKIAQ7J3FIK6FGBSTY7Q",
    "secretAccessKey": "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",
  }
);

Vue.config.productionTip = false
Vue.use(VueAxios, axios, firebase, AWS) //追記

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
