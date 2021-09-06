<template>
  <div class="footer">
    <div class="logo_container">
      <img
        class="logo"
        alt="Tsugitasu Logo"
        src="../assets/logo.svg"
      />
    </div>
    <div class="menu_container">
      <div class="links_container">
        <div class="link_container">
          <div class="link" style="font-weight:600; cursor:default;">
            検索
          </div>
          <div class="link" @click="router_to('/filter/')">
            教材を探す
          </div>
          <div class="link" @click="router_to('/filter/')">
            授業を探す
          </div>
          <div class="link" @click="router_to('/filter/')">
            アイデアと出会う
          </div>
        </div>
        <div class="link_container">
          <div class="link" style="font-weight:600; cursor:default;">
            マイスペース
          </div>
          <div class="link" @click="mymanagement()">
            マイ教材・授業
          </div>
          <div class="link"  @click="myupload()">
            投稿する
          </div>
          <div class="link">
            教材・授業管理
          </div>
          <div class="link"  @click="myaccount()">
            マイアカウント
          </div>
        </div>
        <div class="link_container">
          <div class="link" style="font-weight:600; cursor:default;">
            その他
          </div>
          <div class="link">
            ヘルプ・お問い合わせ
          </div>
          <div class="link">
            よくあるご質問
          </div>
          <div class="link">
            プライバシーポリシー
          </div>
          <div class="link">
            利用規約
          </div>
          <div class="link" @click="logout">
            ログアウト
          </div>
        </div>
      </div>
      <div class="round_logo_container">
        <img
          class="round_logo"
          alt="Tsugitasu Logo"
          src="../assets/round_logo.svg"
        />
      </div>
    </div>
  </div>
</template>


<script>
var firebase = require('firebase/app')
require('firebase/auth')

export default {
  name: "FooterMenu",
  methods: {
    router_to (target) {
      this.$router.push(target);
    },
    logout () {
      var unsubscribe = firebase.default.auth().onAuthStateChanged(user => {
        if (user){
          firebase.default
          .auth()
          .signOut()
          .then(() => {
            alert('ログアウトしました');
          })
          .catch((error) => {
            console.log(`ログアウト時にエラーが発生しました (${error})`);
          });
          this.router_to("/login");
        }else{
          location.reload();
        }
        unsubscribe();
      });
    },
    myaccount(){
      var unsubscribe = firebase.default.auth().onAuthStateChanged(user => {
        if (user){
          this.router_to("/mypage/" + user.uid);
        }else{
          location.reload();
        }
        unsubscribe();
      });
    },
    myupload(){
      var unsubscribe = firebase.default.auth().onAuthStateChanged(user => {
        if (user){
          this.router_to("/mypage/" + user.uid + "/upload");
        }else{
          location.reload();
        }
        unsubscribe();
      });
    },
    mymanagement(){
      var unsubscribe = firebase.default.auth().onAuthStateChanged(user => {
        if (user){
          this.router_to("/mypage/" + user.uid + "/management");
        }else{
          location.reload();
        }
        unsubscribe();
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .footer {
    width: 80%;
    height: 260px;
    margin: 50px 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    .logo_container{
      width: 100%;
      margin-bottom: 20px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      .logo{
        width:200px
      }
    }
    .menu_container{
      width: 100%;
      height: 200px;
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      .links_container{
        width: 70%;
        height: 200px;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        .link_container{
          width: 33%;
          height: 200px;
          display: flex;
          flex-direction: column;
          justify-content: flex-start;
          align-items: flex-start;
          .link{
            cursor: pointer;
            font-size: 18px;
            font-weight: 400;
            margin-bottom: 10px;
          }
        }
      }
      .round_logo_container{
        width: 30%;
        height: 200px;
        display: flex;
        justify-content: flex-end;
        align-items: flex-end;
        .round_logo{
          width:150px
        }
      }
    }
  }
</style>
