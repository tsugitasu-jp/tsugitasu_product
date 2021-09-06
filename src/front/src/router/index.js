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
    meta: { requiresAuth: true, validUid: true }
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
    path: "/:cid/:bid/:ver/",
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
    }
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
  var unsubscribe = firebase.default.auth().onAuthStateChanged((user) => {
    if (checkLogin && user) {
      console.log("checklogin&user")
      // サインアップ・ログインはログインユーザには表示させない
      // => ワークスペースにリダイレクト
      next({
        path: '/mypage/' + user.uid + '/management',
      })
    }
    if (requiresAuth) {
      // このルートはログインされているかどうか認証が必要です。
      // もしされていないならば、ログインページにリダイレクトします。
      if (!user) {
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        })
      } else {
        // uidがログインユーザのものと同一か検証
        if (validUid && user.uid != to.params.uid) {
          return
        }
        next()
      }
    } else {
      next() // next() を常に呼び出すようにしてください!
    }
    // リスナー解除
    unsubscribe();
  });  
})



export default router;
