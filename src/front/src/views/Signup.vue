<template>
  <div
    class="signup_container">
    <div id="signup_form_container">
      <div class="signup_form_header">
        <h2>アカウント作成</h2>
      </div>
      <div class="input_container">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            氏名
          </div>
        </div>
        <div class="input_container_right">
          <input class="input" type="text" placeholder="ツギタス 太郎" v-model="name">
        </div>
      </div>
      <div class="input_container">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            性別
          </div>
        </div>
        <div class="input_container_right">
          <div class="input_container_right_radio">
            <input class="input_radio" type="radio" value="maile" id="maile" v-model="gender">
            <label class="label_radio" for="maile">男性</label>
          </div>
          <div class="input_container_right_radio">
            <input class="input_radio" type="radio" value="femaile" id="femaile" v-model="gender">
            <label class="label_radio" for="femaile">女性</label>
          </div>
          <div class="input_container_right_radio">
            <input class="input_radio" type="radio" value="other" id="other" v-model="gender">
            <label class="label_radio" for="other">その他</label>
          </div>
        </div>
      </div>
      <div class="input_container">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            メールアドレス
          </div>
        </div>
        <div class="input_container_right">
          <input class="input" type="text" placeholder="tsugitasu@study.com" v-model="mail">
        </div>
      </div>
      <div class="input_container">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            メールアドレス<span style="font-size:15px;">（確認用）</span>
          </div>
        </div>
        <div class="input_container_right">
          <input class="input" type="text" placeholder="tsugitasu@study.com">
        </div>
      </div>
      <div class="input_container">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            所属学校
          </div>
        </div>
        <div class="input_container_right">
          <input class="input" type="text" placeholder="ツギタス市立ツギタス小学校" v-model="school">
        </div>
      </div>
      <div class="input_container">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            担当学年
          </div>
        </div>
        <div class="input_container_right">
          <select class="input_select" v-model="select_grade">
            <option value="1">１年</option>
            <option value="2">２年</option>
            <option value="3">３年</option>
            <option value="4">４年</option>
            <option value="5">５年</option>
            <option value="6">６年</option>
          </select>
        </div>
      </div>
      <div class="input_container">
        <div class="input_container_left" style="width:100%;">
          <div class="label_line" />
          <div class="label">
            使用教科書
          </div>
          <div class="sub_label">
            所属学校と担当学年を入力すると自動で使用教科書を表示します。
          </div>
        </div>
      </div>
      <div class="material_grid_container">
        <div class="material_container">
          <div class="material_subject">
            国語
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
        <div class="material_container">
          <div class="material_subject">
            数学
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
        <div class="material_container">
          <div class="material_subject">
            英語
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
        <div class="material_container">
          <div class="material_subject">
            理科
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
        <div class="material_container">
          <div class="material_subject">
            社会
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
        <div class="material_container">
          <div class="material_subject">
            美術
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
        <div class="material_container">
          <div class="material_subject">
            音楽
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
        <div class="material_container">
          <div class="material_subject">
            技術
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
        <div class="material_container">
          <div class="material_subject">
            家庭
          </div>
          <div class="material_image">
          </div>
          <div class="material_title">
            国語総合
          </div>
        </div>
      </div>
      <div class="input_container" style="margin: 20px 0 0 0;">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            ユーザーネーム
          </div>
        </div>
        <div class="input_container_right">
          <input class="input" type="text" placeholder="ツギタス太郎" v-model="display_name">
        </div>
      </div>
      <div class="input_container" style="margin: 0 0 20px 0;">
        <div class="input_container_left" style="width:100%;">
          <div class="sub_label">
            アプリケーション内で表示される名前です
          </div>
        </div>
      </div>
      <div class="input_container">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            パスワード
          </div>
        </div>
        <div class="input_container_right">
          <input class="input" :type="this.password.isDisp ? 'text' : 'password'" placeholder="パスワード" v-model="pass">
          <span class="password_btn" @click="password_disp">{{this.password.text = this.password.isDisp ? "非表示" : "表示"}}</span>
        </div>
      </div>
      <div class="input_container">
        <div class="input_container_left">
          <div class="label_line" />
          <div class="label">
            パスワード<span style="font-size:15px;">（再入力）</span>
          </div>
        </div>
        <div class="input_container_right">
          <input class="input" :type="this.password.isDisp ? 'text' : 'password'" placeholder="パスワード（再入力）">
          <span class="password_btn" @click="password_disp">{{this.password.text = this.password.isDisp ? "非表示" : "表示"}}</span>
        </div>
      </div>
      <div class="submit_btn" @click="signUp">
        登録する
      </div>
      <div class="submit_attention">
        アカウントを作成すると、利用規約、およびプライバシーポリシーに同意したものとみなされます。
      </div>
    </div>
    <FooterMenu/>
  </div>
</template>

<script>
import FooterMenu from "../components/FooterMenu.vue";
var firebase = require('firebase/app')
require('firebase/auth')
require('firebase/firestore')

export default {
  components: { 
    FooterMenu
  },
  data() {
    return {
      mail: "",
      pass: "",
      gender: "",
      name: "",
      display_name: "",
      school: "",
      select_grade: "",
      password:{
        isDisp:false,
      },
      disp_cards: [],
      cards: [
        {
          title: "サポーターズハッカソンオンライン開発合宿vol.6",
          description:
            "「日常生活にちょっと面白さを加えるア",
        },
      ],
    };
  },
  computed: {
  },
  methods: {
    router_to: function(target) {
      this.$router.push(target);
    },
    password_disp() {
      this.password.isDisp = !this.password.isDisp;
    },
    signUp: function () {
      var axios = this.axios;
      var router = this.$router;
      var route = this.$route;
      var name = this.name;
      var display_name = this.display_name;
      var school = this.school;
      var gender = this.gender;
      var grade = this.select_grade;

      // Firestoreのオブジェクト取得
      var db = firebase.default.firestore();
      firebase.default.auth().createUserWithEmailAndPassword(this.mail, this.pass)
      .then(function(user){
        var create_obj = {
          uid: user.user.uid,
          name: name,
          displayname: display_name,
          school: school,
          gender: gender,
          grade: grade,
        }
        var set_django_data = {
          display_name: display_name,
          photo_url: "",
        }
        user.user.getIdToken().then(function (token) {
          db.collection("users").add(create_obj)
          .then((doc) => {
            console.log(`追加に成功しました (${doc.id})`);
          })
          .catch((error) => {
            console.log(`追加に失敗しました (${error})`);
          });
          
          /* django側に登録 */
          let config = {
            headers: {
              'Authorization': "JWT " + token,
            },
          };
          axios
          .post('http://127.0.0.1:8000/api-v1/make_account/', set_django_data, config)
          .then(function() {
              if (route.query.redirect){
                router.push(route.query.redirect)
              }else{
                location.reload();
              }
          })
          .catch(function(error) {
              console.log(error)
          })
        })
      })
      .catch(function (error) {
        //var error_code = error.code;
        var errorMessage = error.message;
        console.log(errorMessage);
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.signup_container{
  background-color: #F8F8F8;
  background-image: url("../assets/bgs/signup_bg.svg");
  background-position: right 0;
	background-repeat: repeat-y;
	background-size: 35% auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  #signup_form_container{
    background-color: #FFFFFF;
    width: 900px;
    height: 1900px;
    margin: 100px 100px 50px 100px ;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    box-shadow: #3A3A3A29 6px 6px 15px;
    .signup_form_header{
      width: 270px;
      height: 60px;
      margin: 50px 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border-bottom: 3px solid #365A0C;
    }
    .input_container{
      width: 700px;
      height: 60px;
      margin: 20px 0;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      .input_container_left{
        width: 40%;
        height: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .label_line{
          background-color: #343434;
          width: 5px;
          height: 10px;
        }
        .label{
          margin: 3px 0;
          padding-left: 10px;
          font-size: 18px;
          font-weight: 600;
        }
        .sub_label{
          margin-left: 10px;
          font-size: 15px;
          font-weight: 600;
          color: #757474;
        }
      }
      .input_container_right{
        width: 60%;
        height: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        position: relative;
        .input{
          outline: none;
          width: 100%;
          height: 90%;
          border: 2px solid #C4C4C4;
          border-radius: 10px;
          padding: 0 20px;
        }
        .input_container_right_radio{
          width: 90px;
          margin-right: 10px;
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: flex-start;
          .input_radio{
            cursor: pointer;
            margin: 0;
            outline: none;
            width: 18px;
            height: 18px;
          }
          .label_radio{
            cursor: pointer;
            margin-left: 5px;
            font-size: 15px;
            font-weight: 600;
          }
        }
        .input_select{
          outline: none;
          width: 130px;
          height: 90%;
          border: 2px solid #C4C4C4;
          border-radius: 10px;
          padding: 0 20px;
          font-size: 15px;
          font-weight: 600;
        }
        .password_btn{
          cursor: pointer;
          position: absolute;
          right: 7px;
          font-size: 15px;
          font-weight: 600;
        }
      }
    }
    .material_grid_container{
      width: 750px;
      height: 480px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      flex-wrap: wrap;
      .material_container{
        width: 140px;
        height: 220px;
        margin: 5px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        .material_subject{
          width: 130px;
          height: 20px;
          font-size: 16px;
          font-weight: 600;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .material_image{
          width: 130px;
          height: 160px;
          border: 2px solid #C4C4C4;
          border-radius: 10px;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .material_title{
          width: 130px;
          height: 40px;
          font-size: 16px;
          font-weight: 600;
          display: flex;
          align-items: center;
          justify-content: center;
        }
      }
    }
    .submit_btn{
      width: 190px;
      height: 50px;
      margin-top: 50px;
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
</style>