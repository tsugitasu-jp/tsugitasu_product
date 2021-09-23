<template>
  <div class="login_container">
    <div class="login_content_container">
      <div class="login_container_left">
        <img class="login_image" src="../assets/bgs/login_pic.png" alt="Avatar">
      </div>
      <div class="login_container_right">
        <div class="login_form_container">
          <div class="login_form_header">
            <h2>ログイン</h2>
          </div>
          <div class="input_container">
            <div class="input_label">
              メールアドレス
            </div>
            <input class="input" type="text" placeholder="メールアドレス" v-model="mail">
          </div>
          <div class="password_container">
            <div class="input_label">
              パスワード
            </div>
            <input class="input" :type="this.password.isDisp ? 'text' : 'password'" placeholder="パスワード" v-model="pass">
            <span class="password_btn" @click="password_disp">{{this.password.text = this.password.isDisp ? "非表示" : "表示"}}</span>
          </div>
          <div class="login_check_container">
            <input class="input" type="checkbox" id="check" v-model="LoginState">
            <label class="login_check_label" for="check">ログイン情報を保存する</label>
          </div>
          <div class="submit_btn" @click="login">
            ログイン
          </div>
          <div class="submit_attention">
            パスワードを忘れた場合はこちら
          </div>
        </div>
      </div>
    </div>
    <FooterMenu />
  </div>
</template>

<script>
import FooterMenu from "../components/FooterMenu.vue";
var firebase = require('firebase/app')
require('firebase/auth')

export default {
  components: { 
    FooterMenu
  },
  data() {
    return {
      password:{
        isDisp:false,
      },
      LoginState:false,
    };
  },
  created() {
  },
  computed: {
  },
  methods: {
    password_disp() {
      this.password.isDisp = !this.password.isDisp;
    },
    login(){
      console.log(this.mail)
      console.log(this.pass)
      firebase.default.auth().signInWithEmailAndPassword(this.mail, this.pass)
      .then(
        user => {
          console.log(user)
          if (this.$route.query.redirect){
            this.$router.push(this.$route.query.redirect)
          }else{
            location.reload();
          }
        },
      )
      .catch(function (error) {
        //var error_code = error.code;
        var errorMessage = error.message;
        console.log(errorMessage);
      });
    }
  },
};
</script>

<style lang="scss" scoped>
.login_container{
  width: 100%;
  background-color: #F8F8F8;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  .login_content_container{
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    .login_container_left{
      width: 50%;
      height: 900px;
      display: flex;
      align-items: center;
      justify-content: center;
      .login_image{
        width: 490px;
        height: 735px;
      }
    }
    .login_container_right{
      width: 50%;
      height: 900px;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      .login_form_container{
        width: 600px;
        height: 735px;
        border-radius: 20px;
        background-color: #FFFFFF;
        box-shadow: #3A3A3A29 6px 6px 15px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;  
        .login_form_header{
          width: 200px;
          height: 60px;
          margin: 50px 0;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          border-bottom: 3px solid #365A0C;
        }
        .input_container{
          width: 450px;
          margin: 20px 0;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: center;
          .input_label{
            font-size: 18px;
            font-weight: 600;
            margin: 5px 0;
          }
          .input{
            outline: none;
            width: 100%;
            height: 50px;
            border: 2px solid #C4C4C4;
            border-radius: 10px;
            padding: 0 20px;
          }
        }
        .password_container{
          width: 450px;
          margin: 20px 0;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: center;
          position: relative;
          .input_label{
            font-size: 18px;
            font-weight: 600;
            margin: 5px 0;
          }
          .input{
            outline: none;
            width: 100%;
            height: 50px;
            border: 2px solid #C4C4C4;
            border-radius: 10px;
            padding: 0 20px;
          }
          .password_btn{
            cursor: pointer;
            position: absolute;
            right: 7px;
            bottom: 14px;
            font-size: 15px;
            font-weight: 600;
          }
        }
        .login_check_container{
          width: 450px;
          margin: 20px 0 50px 0;
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: flex-start;
          .input{
            outline: none;
            width: 20px;
            height: 20px;
            border: 2px solid #C4C4C4;
            border-radius: 10px;
            padding: 0 20px;

          }
          .login_check_label{
            font-size: 18px;
            font-weight: 600;
            margin: 5px 0;
          }
        }
        .submit_btn{
          width: 350px;
          height: 50px;
          margin-top: 30px;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          border-radius: 10px;
          background-color: #3EB595;
          color: #FFFFFF;
          font-size: 20px;
          font-weight: 600;
          cursor: pointer;
          &:hover{
            background-color: #365A0C;
          }
        }
        .submit_attention{
          margin-top: 30px;
          color: #757474;
          font-size: 15px;
          font-weight: 600;
        }
      }
    }
  }
}
</style>