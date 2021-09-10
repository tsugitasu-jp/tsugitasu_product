import Vue from "vue";
import VueRouter from "vue-router";
// ビューのインポート
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import MyPage_Management from "../views/MyPage_Management.vue";
import MyPage_Upload from "../views/MyPage_Upload.vue";
import MyPage from "../views/MyPage.vue";
import Filter from "../views/Filter.vue";
import MaterialsDescription from "../views/MaterialsDescription.vue";
import UserInfo from "../views/UserInfo.vue";

// メニューのインポート
import BaseMenu from "../views_menu/BaseMenu.vue";
import SearchMenu from "../views_menu/SearchMenu.vue";
var firebase = require('firebase/app')
require('firebase/auth')
require('firebase/firestore')

Vue.use(VueRouter);

const routes = [
  
  {
    path: "/",
    name: "Home",
    components: {
      default: Home,
      menu: BaseMenu
    }
  },
  {
    path: "/login/",
    name: "Login",
    components: {
      default: Login,
      menu: BaseMenu
    },
    meta: {checkLogin: true}
  },
  {
    path: "/signup/",
    name: "Signup",
    components: {
      default: Signup,
      menu: BaseMenu
    },
    meta: {checkLogin: true}
  },
  {
    path: "/mypage/:uid/management/",
    name: "MyPageManagement",
    components: {
      default: MyPage_Management,
      menu: SearchMenu
    },
    meta: { requiresAuth: true, validUid: true }
  },
  {
    path: "/mypage/:uid/upload/",
    name: "MyPageUpload",
    components: {
      default: MyPage_Upload,
      menu: SearchMenu
    },
    meta: { requiresAuth: true, validUid: true }
  },
  {
    path: "/mypage/:uid/",
    name: "MyPage",
    components: {
      default: MyPage,
      menu: SearchMenu
    },
    meta: { requiresAuth: true, checkUid: true, follow: true }
  },
  {
    path: "/filter/",
    name: "Filter",
    components: {
      default: Filter,
      menu: SearchMenu
    }
  },
  {
    path: "/:cid/b:bid/v:vid/",
    name: "MaterialsDescription",
    components: {
      default: MaterialsDescription,
      menu: SearchMenu
    }
  },
  {
    path: "/:uid/",
    name: "UserInfo",
    components: {
      default: UserInfo,
      menu: SearchMenu
    },
    //meta: { user_info_f: true }
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  let checkLogin = to.matched.some(record => record.meta.checkLogin)
  let requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  let validUid = to.matched.some(record => record.meta.validUid)
  var displayname;
  var db = firebase.default.firestore();

  /*
  * user_info_f: 
  * requiresAuth: jwt認証必須
  *     - checkLogin: 認証してたらワークスペースにリダイレクト
  *     - validUid: urlパラメータのuid=認証ユーザのuidでなければ404
  *     - follow: follow数をパラメータに組み込む
  */

  /* 
  * チェック1: urlパラメータのuidが存在するかどうか
  * チェック2: urlパラメータのuidが認証ユーザのuidならマイページにリダイレクト
  * チェック3: follow数、follower数の取得
  */

  firebase.default.auth().onAuthStateChanged((user) => {
    if (checkLogin && user) {
      console.log("checklogin&user")
      // サインアップ・ログインはログインユーザには表示させない
      if(to.query.backuri){
        // => 戻り先にリダイレクト
        next({
          path: to.query.backuri,
        })
      }else{
        // => ワークスペースにリダイレクト
        next({
          path: '/mypage/' + user.uid + '/management',
        })
      }
    }
    if (requiresAuth) {
      // このルートはログインされているかどうか認証が必要です。
      // もしされていないならば、ログインページにリダイレクトします。
      if (!user) {
        next({
          path: '/login',
          query: { redirect: to.fullPath },
        })
      } else {
        // uidがログインユーザのものと同一か検証
        if (validUid && user.uid != to.params.uid) {
          return
        }
        // ユーザ情報の取得
        db.collection("users").where("uid", "==", to.params.uid).limit(1)
        .get()
        .then((querySnapshot) => {
          querySnapshot.forEach((doc) => {
            displayname = doc.data()['displayname']
            to.query.displayname = displayname
            next()
          });
        });
        return
      }
    } else {
      next() // next() を常に呼び出すようにしてください!
    }
  });  
})



export default router;
