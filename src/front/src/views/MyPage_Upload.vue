<template>
  <div class="upload_container">
    <div class="mypage_header">
      <h1>教材の投稿・アップロード</h1>
      <p>作成した教材を投稿・アップロードして、ツギタスをもっと楽しみましょう！</p>
    </div>
    <div class="upload_btn_container">
      <div class="upload_btn" @click="modal_disp_change">
        FILE UPLOAD
      </div>
    </div>
    <div class="materials_label_container">
      <div class="label">
        最近投稿・アップロードした教材
      </div>
      <div class="materials_container">
        <div class="material_container" v-for="created_material in disp_list.created_materials" :key="created_material.id" @click="touchToMaterial(created_material.cid, created_material.bid, created_material.ver)">
          <img class="material_image" :style="{ backgroundImage: 'url(http://127.0.0.1/media/' + created_material.cid + '/b' + created_material.bid + '/v' + created_material.ver + '/' + created_material.content_image_main + ')' }">
          <div class="material_title">
            {{created_material.title.slice(0, 15)}}...
          </div>
          <div class="material_description">
            <p v-html="created_material.context.slice(0, 60) + '...' " style="display: block"></p>
          </div>
          <div class="author_container">
            <div class="author_name">
              {{created_material.display_name}}
            </div>
            <div class="author_date">
              {{created_material.created_at}}
            </div>
          </div>
        </div>
      </div>
    </div>    
    <FooterMenu />
    <div class="modal_container" v-if="Modal_Disp" @click.self="modal_disp_change">
      <div class="upload_form_container">
        <div class="modal_close_btn">
          <img src="../assets/icons/cross_gray.png" class="gray_cross">
          <img src="../assets/icons/cross_pink.png" class="pink_cross" @click.self="modal_disp_change">
        </div>
        <div class="modal_label">
          トップ＆その他イメージ
        </div>
        <div class="material_image_container">
          <div class="material_image_top">
          </div>
          <div class="other_material_image_container">
            <div class="material_image"/>
            <div class="material_image"/>
            <div class="material_image"/>
          </div>
        </div>
        <div class="modal_label">
          タイトル（15字以内）
        </div>
        <input class="input" type="text" placeholder="タイトルを入力">
        <div class="modal_label">
          教科
        </div>
        <div class="subject_tag_container">
          <div class="subject_tag">
            国語
          </div>
          <div class="subject_tag">
            算数
          </div>
          <div class="subject_tag">
            英語
          </div>
          <div class="subject_tag">
            理科
          </div>
          <div class="subject_tag">
            社会
          </div>
          <div class="subject_tag">
            美術
          </div>
          <div class="subject_tag">
            体育
          </div>
          <div class="subject_tag">
            体育
          </div>
          <div class="subject_tag">
            技術
          </div>
          <div class="subject_tag">
            家庭
          </div>
          <div class="subject_tag">
            プログラミング
          </div>
          <div class="subject_tag">
            その他
          </div>
        </div>
        <div class="modal_label">
          教材の説明（200字以内）
        </div>
        <textarea class="textarea" cols="70" rows="3" placeholder="説明文を入力"></textarea>
        <div class="modal_label">
          タグ付け
          <div class="input_container_radio">
            <input class="input_radio" type="checkbox" id="tag_on" v-model="Modal_Tag">
            <label class="label_radio" for="tag_on">自動タグ生成機能を利用する</label>
          </div>
        </div>
        <textarea class="textarea" cols="70" rows="3" placeholder="#キーワードでタグを追加"></textarea>
        <div class="modal_form_submit_btn">
          教材をアップロードする
        </div>
      </div>
    </div>
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
      Modal_Tag:false,
      Modal_Disp:false,
      disp_list:{
        created_materials:[],
      }
    };
  },
  created() {
    firebase.default.auth().onAuthStateChanged((user) => {
      user.getIdToken().then((token) => {
        const config = {
          headers: {
            'Authorization': "JWT " + token,
          },
        };
        this.axios
          .get('http://127.0.0.1:8000/api-v1/contents/me/', config)
          .then((response) => {
            console.log(response.data)
            this.$set(this.disp_list, 'created_materials', response.data)
          })
          .catch(function(error) {
              console.log(error)
          })
      });
    })
  },
  computed: {
  },
  methods: {
    modal_disp_change () {
      this.Modal_Disp = !this.Modal_Disp
    },
    touchToMaterial(cid, bid, vid){
      console.log(cid)
      console.log(bid)
      console.log(vid)
      this.$router.push({ name: 'MaterialsDescription', params: {cid: cid, bid: bid, vid: vid}})
    },
  },
};
</script>

<style lang="scss" scoped>
.upload_container{
  background-color: #FFFFFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  .upload_btn_container{
    width: 80%;
    margin: 30px 0 15px 0;
    padding-left: 50px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    .upload_btn{
      cursor: pointer;
      background-color: #F14479;
      width: 500px;
      height: 100px;
      border-radius: 15px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      font-size: 40px;
      font-weight: 900;
      color: #FFFFFF;
      &:hover{
        background-color: #cb2257;
      }
    }
  }
  .mypage_header{
    width: 80%;
    margin: 30px 0 15px 0;
    padding-left: 50px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
  }
  .materials_label_container{
    background-color: #F6F6F6;
    width: 80%;
    padding: 15px;
    margin: 25px 0;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    .label{
      padding: 10px 15px;
      font-size: 25px;
      font-weight: 600;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
    }
    .materials_container{
      background-color: #F6F6F6;
      width: 100%;
      max-height: 800px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      flex-wrap: wrap;
      overflow-y: scroll;
      .material_container{
        cursor: pointer;
        flex-shrink: 0;
        width: 250px;
        height: 250px;
        margin: 15px;
        border: 1px solid #757474;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: #75747455 1px 1px 5px;
        transition: 0.2s;
        &:hover{
          box-shadow: #757474 3px 3px 0px;
          position: relative;;
          top: -3px;
          left: -3px;
        }
        .material_image{
          border-radius: 10px 10px 0 0;
          width: 250px;
          height: 140px;
        }
        .material_title{
          font-size: 15px;
          font-weight: 500;
          padding: 0 10px;
        }
        .material_description{
          width: 100%;
          height: 60px;
          font-size: 11px;
          font-weight: 400;
          padding: 0 10px;
          display: flex;
          flex-direction: row;
          align-items: flex-start;
          justify-content: flex-start;
        }
        .author_container{
          font-size: 10px;
          font-weight: 400;
          padding: 0 10px;
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: space-between;
        }
      }
    }
  }
  .modal_container{
    background-color: #707070AA;
    width: 100%;
    height: 100%;
    position: fixed;
    z-index: 5000;
    top: 0;
    left: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    .upload_form_container{
      background-color: #FFFFFF;
      width: 70%;
      height: 90%;
      padding: 50px 0;
      border-radius: 15px;
      overflow-y: scroll;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      position: relative;
      .modal_close_btn{
        cursor: pointer;
        width: 30px;
        height: 30px;
        position: absolute;
        right: 60px;
        top: 60px;
        z-index: 5100;
        .pink_cross{
          position: absolute;
          opacity: 0;
          transform: rotate(0deg);
          transition: 0.2s;
        }
        .gray_cross{
          position: absolute;
          opacity: 1;
          transform: rotate(0deg);
          transition: 0.2s;
        }
        &:hover > .pink_cross{
          opacity: 1;
          transform: rotate(180deg);
        }
        &:hover > .gray_cross{
          opacity: 0;
          transform: rotate(180deg);
        }
      }
      .material_image_container{
        flex-shrink: 0;
        width: 65%;
        margin: 5px 0;
        color: #757474;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .material_image_top{
          background-color: deeppink;
          width: 250px;
          height: 150px;
          margin-right: 10px;
          box-shadow: 2px 3px 6px #00000033;
        }
        .other_material_image_container{
          width: calc(100% - 250px);
          height: 180px;
          overflow-y: scroll;
          display: flex;
          flex-direction: row;
          align-items: flex-start;
          justify-content: flex-start;
          flex-wrap: wrap;
          .material_image{
            flex-shrink: 0;
            background-color: deepskyblue;
            width: 150px;
            height: 90px;
            margin: 10px;
            box-shadow: 2px 3px 6px #00000033;
          }
        }
      }
      .input{
        flex-shrink: 0;
        outline: none;
        width: 65%;
        height: 40px;
        border: 1px solid #757474;
        border-radius: 10px;
        padding: 0 20px;
      }
      .textarea{
        flex-shrink: 0;
        width: 65%;
        height: 110px;
        outline: none;
        border: 1px solid #757474;
        border-radius: 10px;
        padding: 10px;
        resize: none;
      }
      .subject_tag_container{
        flex-shrink: 0;
        width: 65%;
        max-height: 100px;
        overflow-y: scroll;
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        justify-content: flex-start;
        flex-wrap: wrap;
        .subject_tag{
          font-size: 15px;
          color: #757474;
          padding: 5px 15px;
          margin: 5px 10px;
          border: 1px solid #757474;
          border-radius: 5px;
        }
      }
      .modal_label{
        flex-shrink: 0;
        width: 65%;
        margin: 35px 0 10px 0;
        font-size: 17px;
        font-weight: 400;
        color: #757474;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .input_container_radio{
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: flex-start;
          .input_radio{
            cursor: pointer;
            margin: 0 10px;
            outline: none;
            width: 15px;
            height: 15px;
          }
          .label_radio{
            cursor: pointer;
            font-size: 14px;
          }
        }
      }
    }
    .modal_form_submit_btn{
      cursor: pointer;
      padding: 5px 20px;
      margin-top: 35px;
      border: 2px solid #707070;
      border-radius: 7px;
      color: #757474;
      font-size: 15px;
      font-weight: 500;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
    }
  }
}
</style>