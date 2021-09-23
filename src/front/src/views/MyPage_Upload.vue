<template>
  <div class="upload_container">
    <div class="mypage_header">
      <h1>教材の投稿・アップロード</h1>
      <p>作成した教材を投稿・アップロードして、ツギタスをもっと楽しみましょう！</p>
      <p>↓まずは教材イメージをアップロード</p>
    </div>
    <div class="upload_btn_container">
      <div class="upload_btn">
        FILE UPLOAD
        <input class="upload_btn_input" type="file" multiple @change="file_upload" accept="image/*">
      </div>
    </div>
     <div class="materials_label_container">
      <div class="label">
        最近投稿・アップロードした教材
      </div>
      <div class="materials_container">
        <div class="material_container" v-for="created_material in disp_list.created_materials" :key="created_material.id" @click="touchToMaterial(created_material.cid, created_material.bid, created_material.ver)">
          <img class="material_image" :style="{ backgroundImage: 'url(/media/' + created_material.cid + '/b' + created_material.bid + '/v' + created_material.ver + '/' + created_material.content_image_main + ')' }">
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
    <div class="modal_container" v-if="UploadModal.isShown" @click.self="modal_disp_change">
      <div class="upload_form_container">
        <div class="modal_close_btn">
          <img src="../assets/icons/cross_gray.png" class="gray_cross">
          <img src="../assets/icons/cross_pink.png" class="pink_cross" @click.self="modal_disp_change">
        </div>
        <div class="modal_label">
          トップ＆その他イメージ
        </div>
        <div class="material_image_container">
          <img :src="UploadModal.Disp_File_Image_top" class="material_image_top">
          <div class="other_material_image_container">
            <img v-for="filepath in UploadModal.Disp_File_Image " :key="filepath.id" :src="filepath" class="material_image"/>
          </div>
        </div>
        <div class="modal_label">
          教材ファイルをアップロード
        </div>
        <div class="modal_o">
          <input @change="selectedFile" type="file" name="file">
        </div>
        <div class="modal_label">
          タイトル（15字以内）
        </div>
        <input class="input" type="text" placeholder="タイトルを入力" :v-model="UploadModal.Title">
        <div class="modal_label">
          教科
        </div>
        <div class="subject_tag_container">
          <div :class="(UploadModal.Subject == 'japanese') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('japanese')">
            国語
          </div>
          <div :class="(UploadModal.Subject == 'math') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('math')">
            算数
          </div>
          <div :class="(UploadModal.Subject == 'english') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('english')">
            英語
          </div>
          <div :class="(UploadModal.Subject == 'science') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('science')">
            理科
          </div>
          <div :class="(UploadModal.Subject == 'social_studies') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('social_studies')">
            社会
          </div>
          <div :class="(UploadModal.Subject == 'art') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('art')">
            美術
          </div>
          <div :class="(UploadModal.Subject == 'pt') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('pt')">
            体育
          </div>
          <div :class="(UploadModal.Subject == 'dt') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('dt')">
            技術
          </div>
          <div :class="(UploadModal.Subject == 'home_economics') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('home_economics')">
            家庭
          </div>
          <div :class="(UploadModal.Subject == 'programing') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('programing')">
            プログラミング
          </div>
          <div :class="(UploadModal.Subject == 'other') ? 'subject_tag_checked' : 'subject_tag'" @click="subjects_apply('other')">
            その他
          </div>
        </div>
        <div class="modal_label">
          教材の説明（200字以内）
        </div>
        <textarea class="textarea" cols="70" rows="3" placeholder="説明文を入力" v-model="UploadModal.Description"></textarea>
        <div class="modal_label">
          タグ付け
          <div class="input_container_radio">
            <input class="input_radio" type="checkbox" id="tag_on" v-model="UploadModal.AutoGenTag">
            <label class="label_radio" for="tag_on">自動タグ生成機能を利用する</label>
          </div>
        </div>
        <textarea class="textarea" cols="70" rows="3" placeholder="#キーワードでタグを追加"  v-model="UploadModal.Tags"></textarea>
        
        <div class="modal_form_submit_btn" @click="material_upload">
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
      UploadModal :{
        isShown:false,
        Disp_File_Image:[],
        Disp_File_Image_top:"",

        // ****ここからアップロードするデータ****
        // ファイルの情報が配列で入っている
        File_Info:[],
        // 教材のタイトル
        Title:"",
        // 教材の教科
        Subject: "",
        // 教材の説明
        Description: "",
        // 自動タグ付け機能のオン・オフ
        AutoGenTag:false,
        // タグ
        Tags:""
      },
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
          .get('/api-v1/contents/me/', config)
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
    selectedFile(e) {
      // 選択された File の情報を保存しておく
      e.preventDefault();
      let files = e.target.files;
      this.UploadModal.material = files[0];
    },
    modal_disp_change () {
      console.log("modal change")
      this.UploadModal.isShown = !this.UploadModal.isShown;
    },
    file_upload (file) {
      // ファイル情報の初期化
      this.UploadModal.Disp_File_Image=[]
      this.UploadModal.Disp_File_Image_top=""
      this.UploadModal.File_Info=[]
      this.UploadModal.Title=""
      this.UploadModal.Subject=""
      this.UploadModal.Description=""
      this.UploadModal.AutoGenTag=false
      this.UploadModal.Tags=""
      
      if(file.target.files.length != 0){
        this.UploadModal.File_Info = file.target.files;

        // プレビュー用のURLを発行処理
        this.UploadModal.File_Info.forEach(file => {
          this.UploadModal.Disp_File_Image.push(URL.createObjectURL(file));
        });
        this.UploadModal.Disp_File_Image_top = this.UploadModal.Disp_File_Image.shift();

        this.modal_disp_change();
      }
    },
    touchToMaterial(cid, bid, vid){
      console.log(cid)
      console.log(bid)
      console.log(vid)
      this.$router.push({ name: 'MaterialsDescription', params: {cid: cid, bid: bid, vid: vid}})
    },
    subjects_apply (subject) {
      this.UploadModal.Subject = subject;
    },
    array_to_formdata(data, formData){
      Object.keys(data).forEach(key => {
        const value = data[key];
        if (Array.isArray(value)) {
          value.forEach(entry => {
            formData.append(key + '[]', entry);
          });
        } else {
          formData.append(key, value);
        }
      });
    },
    // 教材をアップロードする処理
    material_upload (){
      let file_lst = this.UploadModal.File_Info
      console.log(this.UploadModal.Tags)
      let tags = []
      let tag_o = this.UploadModal.Tags.split(/\r|\s|#/)
      for (let i = 0; i< tag_o.length;i++){
        if (tag_o[i] == ''){
          continue
        }
        tags.push(tag_o[i])
      }
      
      console.log(tags)
      let files = []
      for (let i = 0; i< file_lst.length;i++){
        if (i==0) {
          continue;
        }
        files.push(file_lst[i])
      }
      
      // FormData を利用して File等 を POST する
      let formData = new FormData();
      formData.append('fd', this.UploadModal.material);
      formData.append('image_main', file_lst[0]);
      formData.append('title', this.UploadModal.Title);
      formData.append('subject', this.UploadModal.Subject)
      formData.append('context', this.UploadModal.Description)
      formData.append('tag_flag', this.UploadModal.AutoGenTag)
      this.array_to_formdata({'image_sub': files}, formData)
      this.array_to_formdata({'tag': tags}, formData)

      firebase.default.auth().onAuthStateChanged((user) => {
        user.getIdToken().then((token) => {
          const config = {
            headers: {
              'Authorization': "JWT " + token,
              'content-type': 'multipart/form-data'
            }
          };
          this.axios
            .post('http://127.0.0.1:8000/api-v1/content/create/', formData, config)
            .then(function(response) {
                console.log(response.data)
            })
            .catch(function(error) {
                console.log(error)
            })
        })
      }),

      // Modalを閉じる処理
      this.modal_disp_change();
    }
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
    position: relative;
    .upload_btn{
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
      pointer-events: none;
      &:hover {
        background-color: #cb2257;
      }
      .upload_btn_input{
        cursor: pointer;
        opacity: 0;
        width: 500px;
        height: 100px;
        border-radius: 15px;
        position: absolute;
        pointer-events: auto;
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
          cursor: pointer;
          background-color: #FFFFFF;
          font-size: 15px;
          color: #757474;
          padding: 5px 15px;
          margin: 5px 10px;
          border: 1px solid #757474;
          border-radius: 5px;
          &:hover {
            background-color: #EEEEEE;
          }
        }
        .subject_tag_checked{
          cursor: pointer;
          background-color: #757474;
          font-size: 15px;
          color: #FFFFFF;
          padding: 5px 15px;
          margin: 5px 10px;
          border: 1px solid #757474;
          border-radius: 5px;
        }
      }
      .modal_o{
        flex-shrink: 0;
        width: 65%;
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
      background-color: #FFFFFF;
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
      transition: 0.2s ;
      &:hover {
        color: #FFFFFF;
        background-color: #757474;

      }
    }
  }
}
</style>