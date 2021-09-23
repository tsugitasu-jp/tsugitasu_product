<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.2.2/jszip.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>

<template>
  <div class="materials_description_container">
    <div class="materials_main_description">
      <div class="materials_main_description_image" :style="{ backgroundImage: 'url(/' + main_material.content_image_main + ')' }">
      </div>
      <div class="materials_main_description_text">
        <div class="materials_main_description_text_title">
          {{ main_material.title }}
        </div>
        <div class="materials_main_description_text_tags_container">
          <div class="star_tag">
            ★ {{main_material.good}}
          </div>
          <div class="material_tag_container" v-for="tag in main_material.tags" :key="tag.id">
            <div class="material_tag">
              {{tag}}
            </div>
          </div>
        </div>
        <div class="materials_main_description_text_date">
          {{main_material.created_at}}
        </div>
        <div class="materials_main_description_text_description">
          <p v-html="main_material.context" style="display: block"></p>
        </div>
        <div class="materials_main_description_text_author">
          <div class="author" @click=touchToUser(main_material.uid)>
            <div class="author_image" :style="{ backgroundImage: 'url(/media/' + main_material.photo_url + ')' }"></div>
            {{ main_material.displayname }}
          </div>
          <div class="follow_btn" style="cursor: pointer;">
            + 作成者をフォロー
          </div>
        </div>
      </div>
    </div>
    <div class="materials_slide_description_container">
      <div class="slide-wrapper" v-for="img in main_material.content_image_subs" :key="img.id">
        <div class="slide" :style="{ backgroundImage: 'url(/' + img + ')' }">
          
        </div>
      </div>
    </div>
    <div class="btn_container">
      <div class="base_btn_style keep_btn" @click="change_good_state">
        マイページにキープする
      </div>
      <div class="base_btn_style dl_btn" @click="getFiles">
        この教材をダウンロード
      </div>
      <div class="base_btn_style comment_btn">
        作者にコメントを送る
      </div>
     
    </div>
    <div class="comments_content_container">
      <div class="comment_label_container">
        <div class="comment_label">
          コメント
        </div>
        <div class="comment_number">
          12
        </div>
      </div>
      <div class="comments_container">
        <div class="comment_container">
          <div class="author_container">
            <div class="author_image">
            </div>
            <div class="name_date_container">
              <div class="name">
                Tatsuya Okazaki
              </div>
              <div class="date">
                5日前
              </div>
            </div>
          </div>
          <div class="comments_description">
            <p>かわいいイラストと楽しめる教材ですね！来月の授業で１年生に使ってみようと思います。</p>
            <p>あと少しだけ意見させてください。ところどころ小学生が読めないような漢字が使われているスライドがいくつか見受けられます。そこを修正すると良いと思います。</p>
          </div>
        </div>
        <div class="comment_container">
          <div class="author_container">
            <div class="author_image">
            </div>
            <div class="name_date_container">
              <div class="name">
                Tatsuya Okazaki
              </div>
              <div class="date">
                5日前
              </div>
            </div>
          </div>
          <div class="comments_description">
            <p>かわいいイラストと楽しめる教材ですね！来月の授業で１年生に使ってみようと思います。</p>
            <p>あと少しだけ意見させてください。ところどころ小学生が読めないような漢字が使われているスライドがいくつか見受けられます。そこを修正すると良いと思います。</p>
          </div>
        </div>
        <div class="comment_container">
          <div class="author_container">
            <div class="author_image">
            </div>
            <div class="name_date_container">
              <div class="name">
                Tatsuya Okazaki
              </div>
              <div class="date">
                5日前
              </div>
            </div>
          </div>
          <div class="comments_description">
            <p>かわいいイラストと楽しめる教材ですね！来月の授業で１年生に使ってみようと思います。</p>
            <p>あと少しだけ意見させてください。ところどころ小学生が読めないような漢字が使われているスライドがいくつか見受けられます。そこを修正すると良いと思います。</p>
          </div>
        </div>
        <div class="comment_container">
          <div class="author_container">
            <div class="author_image">
            </div>
            <div class="name_date_container">
              <div class="name">
                Tatsuya Okazaki
              </div>
              <div class="date">
                5日前
              </div>
            </div>
          </div>
          <div class="comments_description">
            <p>かわいいイラストと楽しめる教材ですね！来月の授業で１年生に使ってみようと思います。</p>
            <p>あと少しだけ意見させてください。ところどころ小学生が読めないような漢字が使われているスライドがいくつか見受けられます。そこを修正すると良いと思います。</p>
          </div>
        </div>
      </div>
    </div>
    <div class="branch_container">
      <div class="branch_label_container">
        <div class="branch_label">
          <div class="label">
            この教材の状況を確認する
          </div>
          <div class="update_number">
            <!-- 現在 <span style="color:#51B1F3;">4つ</span>のアップデート版が存在します -->
          </div>
        </div>
        <div class="material_title">
          {{ main_material.title }}
        </div>
        <div v-if=main_material.is_latest>
          <div class="now_watchng">
            最新版を閲覧しています
          </div>
        </div>
        <div v-else>
          <div class="now_watchng" @click="touchToMaterial(main_material.cid, main_material.bid, main_material.latest_vid)" style="cursor: pointer">
            最新版はこちら
          </div>
        </div>
      </div>
      <div class="branch_tree_container">
        <div class="branch_materials_cotainer">
          <div class="branch_materials_row_cotainer" v-for="(materials_row, i) in disp_branch" :key="materials_row.id">
            <div class="branch_materials_container" v-for="(materials, j) in materials_row" :key="materials.id">
              <div v-if="(materials_row.id == i) && (materials.id == j)" class="own_material" >
                <div class="own_material_image">
                  スライド
                </div>
              </div>
              <div class="branch_material_mes" @click="touchToMaterial(materials.cid, materials.bid, materials.vid)">
                <div v-if="materials.mes != ''" class="left_top" />
                <div v-if="materials.mes != ''" class="right_top" />
                <div v-if="materials.mes != ''" class="right_bottom" />
                <div v-if="materials.mes != ''" class="left_bottom" />
                <p v-if="materials.mes != ''" >{{materials.mes}}</p>
                <div v-if="materials.mes != ''" class="branch_material_author">
                  <div class="author_image" :style="{ backgroundImage: 'url(/media/' + materials.photo_url + ')' }">
                  </div>
                  <div class="author_date_container">
                    <div class="author">
                      {{materials.author}}
                    </div>
                    <div class="date">
                      {{materials.created_at}}
                    </div>
                  </div>
                </div>
              </div>
              <div class="branch_border_container">
                <div v-if="materials.top" class="top" />
                <div v-if="materials.right" class="right" />
                <div v-if="materials.left" class="left" />
                <div v-if="materials.bottom" class="bottom" />
              </div>
              
            </div>
          </div>
        </div>
      </div>
    </div>
    <FooterMenu />
  </div>
</template>

<script>
import FooterMenu from "../components/FooterMenu.vue";
var AWS = require('aws-sdk');
const bucket_name = "tsugitasu-static"
var zip = new JSZip();
var firebase = require('firebase/app')
require('firebase/auth')

AWS.config.update(
  {
    "accessKeyId": "AKIAQ7J3FIK6FGBSTY7Q",
    "secretAccessKey": "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",
  }
);
var s3 = new AWS.S3();

export default {
  components: { 
    FooterMenu
  },
  data() {
    return {
      disp_branch:[],
      main_material: {
        "mes": "",
        "context": "",
        "content_image_main": "",
        "tags": [],
        "displayname": "",
        "created_at": "1999.01.01",
      },
      progress: {"rate": ""},
    };
  },
  created() {
    this.scrollTop();
    this.init()
  },
  computed: {
  },
  watch: {
    '$route': function (to, from) {
      if (to.path !== from.path) {
        this.init();
      }
    }
  },
  methods: {
    init() {
      // 教材の取得
      let cid = this.$route.params.cid
      let bid = this.$route.params.bid
      let vid = this.$route.params.vid
      this.axios
        .get(`/api-v1/content/${cid}/b${bid}/v${vid}/`)
        .then((response) => {
          console.log(response.data)
          const main_url = `media/${cid}/b${bid}/v${vid}/`
          const c_at = response.data['created_at'].split(/[-T]/)
          const image_subs = response.data['content_image_subs']
          
          this.$set(this.main_material, 'title', response.data.title)
          this.$set(this.main_material, 'context', response.data.context)
          this.$set(this.main_material, 'content_image_main', main_url + response.data.content_image_main)
          this.$set(this.main_material, 'content_image_subs', main_url + response.data['content_image_subs'])
          this.$set(this.main_material, 'tags', response.data['tags'])
          this.$set(this.main_material, 'displayname', response.data['displayname'])
          this.$set(this.main_material, 'created_at', `${c_at[0]}.${c_at[1]}.${c_at[2]}`)
          this.$set(this.main_material, 'file_path', response.data.content_image_main)
          this.$set(this.main_material, 'cid', response.data.cid)
          this.$set(this.main_material, 'bid', response.data.bid)
          this.$set(this.main_material, 'is_latest', response.data.is_latest)
          this.$set(this.main_material, 'latest_vid', response.data.latest_vid)
          this.$set(this.main_material, 'good', response.data.good)
          this.$set(this.main_material, 'photo_url', response.data.photo_url)
          this.$set(this.main_material, 'uid', response.data.uid)

          var map_images = image_subs.map(function(img) {
            return main_url + img
          });

          this.$set(this.main_material, 'content_image_subs', map_images)
          
          console.log(this.main_material)
        })
        .catch((error) => {
            console.log(error)
            // 404ページに遷移(とりあえずHome)
            //this.$router.push({ name: 'Home'})
        })
      
      /* 履歴(教材ツリーの取得) */
      this.axios
        .get(`/api-v1/get_content_tree/${cid}/`)
        .then((response) => {
          console.log(response.data)
          for(let i=0;i < response.data['contents'].length;i++){
            this.disp_branch.splice(i, this.disp_branch.length)
            this.disp_branch.push(response.data['contents'][i])
          }
        });
    },
    change_good_state(){
      let cid = this.$route.params.cid
      let bid = this.$route.params.bid
      let vid = this.$route.params.vid
      firebase.default.auth().onAuthStateChanged((user) => {
        user.getIdToken().then((token) => {
          const config = {
            headers: {
              'Authorization': "JWT " + token,
            },
          };
          this.axios
            .get(`/api-v1/content/${cid}/b${bid}/v${vid}/add_good/`, config)
            .then((response) => {
              alert(response.data.result)
              this.init();
            });
        })
      })
    },
    touchToMaterial(cid, bid, vid){
      console.log(cid)
      console.log(bid)
      console.log(vid)
      this.$router.push({ name: 'MaterialsDescription', params: {cid: cid, bid: bid, vid: vid}})
      this.scrollTop()
    },
    touchToUser(uid){
      this.$router.push({ name: 'UserInfo', params: {uid:uid}})
    },
    scrollTop: function(){
      window.scrollTo({
        top: 0
      });
    },
    requestToS3(path, num, e_num){
      return new Promise((resolve, reject) => {
        s3.getObject({
          Bucket: bucket_name, 
          Key: path
        }, (err, data) => {
          if (err){
            resolve()
          } else {
            this.$set(this.progress, 'rate', `${num}/${e_num}ダウンロード開始`)
            const blob = new Blob([data.Body], {type: data.ContentType});
            const name = path.split('/').slice(-1)[0]
            zip.file(name, blob);
            resolve()
          }
        })
      })
    },
    getFiles() {
      var promises = [];
      var pathes = [this.main_material.content_image_main]
      for (const path of this.main_material.content_image_subs){
        pathes.push(path);
      }

      for(let i = 0; i < pathes.length; i++) {
        promises.push(this.requestToS3(pathes[i], i+1, pathes.length))
      }
      
      return Promise.all(promises)
        .then(() => {
          console.log("圧縮")
          zip.generateAsync({type:"blob"})
            .then((content) =>{
              saveAs(content, "content.zip");
              this.$set(this.progress, 'rate', `${pathes.length}/${pathes.length}ダウンロード完了`)
            });
        })
        .catch((res) => {
          console.log(`Error Getting Templates: ${res}`);
        })
        .finally(() => {
          zip = new JSZip();
        });
    }
  },
};
</script>

<style lang="scss" scoped>
.author{
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  .author_image{
    //background-color: crimson;
    background-size:contain;
    background-repeat: no-repeat;
    background-position: center;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }
}
.materials_description_container{
  background-color: #FFFFFF;
  background-size:contain;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  .materials_main_description{
    width: 90%;
    height: auto;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    .materials_main_description_image{
      //background-color: chartreuse;
      background-size:contain;
      background-repeat: no-repeat;
      width: 350px;
      height: 210px;
      margin: 20px;
      box-shadow: #00000033 2px 3px 6px;
    }
    .materials_main_description_text{
      width: calc(100% - 400px);
      height: 210px;
      margin: 20px;
      display: flex;
      flex-direction: column;
      .materials_main_description_text_title{
        width: 100%;
        font-size: 20px;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: flex-start;
      }
      .materials_main_description_text_tags_container{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .star_tag{
          border-radius: 4px;
          border: 1px solid #707070;
          display: flex;
          align-items: flex-end;
          justify-content: center;
          padding: 1px 5px;
          font-size: 12px;
          font-weight: 500;
        }
        .material_tag{
          background-color: #8FB0FF;
          border-radius: 4px;
          display: flex;
          align-items: flex-end;
          justify-content: center;
          padding: 2px 6px;
          margin: 5px 5px;
          font-size: 12px;
          font-weight: 500;
          color: #FEFEFE;
        }
      }
      .materials_main_description_text_date{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        font-size: 13px;
        font-weight: 500;
      }
      .materials_main_description_text_description{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        font-size: 15px;
        font-weight: 500;
        margin: 2px 0px;
        p{
          width: 100%;
          text-align: left;
          display: flex;
          align-items: flex-start;
          justify-content: flex-start;
        }
      }
      .materials_main_description_text_author{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .author{
          margin-right: 5px;
          font-size: 15px;
          font-weight: 500;
        }
        .follow_btn{
          padding: 5px 5px;
          border-radius: 4px;
          border: 1px solid #707070;
          margin-left: 20px;
          font-size: 13px;
          font-weight: 500;
        }
      }
    }
  }
  .materials_slide_description_container{
    width: 90%;
    height: 200px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    overflow-x: scroll;
    .slide{
      flex-shrink: 0;
      //background-color: darkorange;
      background-position: center;
      background-size:contain;
      background-repeat: no-repeat;
      width: 300px;
      height: 170px;
      margin: 10px;
      box-shadow: #00000033 2px 3px 6px;
    }
  }
  .btn_container{
    width: 90%;
    height: 60px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    .base_btn_style{
      cursor: pointer;
      padding: 5px 15px;
      margin: 10px;
      border: 1px solid #707070;
      border-radius: 5px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      color: #757474;
      font-size: 15px;
      font-weight: 600;
      transition: 0.2s;
    }
    .keep_btn{
      background-color: #FFFFFF;
      &:hover{
        color: #c09521;
      }
    }
    .dl_btn{
      background-color: #FFFFFF;
      &:hover{
        color: #5b856b;
      }
    }
    .comment_btn{
      background-color: #FFFFFF;
      &:hover{
        color: #6f70e7;
      }
    }
  }
  .comments_content_container{
    width: 90%;
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    .comment_label_container{
      width: 100%;
      margin: 10px 0;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-start;
      .comment_label{
        margin-right: 10px;
        font-size: 25px;
        font-weight: 600;
        color: #242424;
      }
      .comment_number{
        font-size: 20px;
        font-weight: 500;
        color: #757474;
      }
    }
    .comments_container{
      width: 100%;
      height: auto;
      max-height: 500px;
      overflow-y: scroll;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      .comment_container{
        width: 90%;
        padding: 15px 0;
        border-top: 1px solid #E7E7E7;
        border-bottom: 1px solid #E7E7E7;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        .author_container{
          width: 100%;
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: flex-start;
          .author_image{
            //background-color: crimson;
            background-size:contain;
            background-repeat: no-repeat;
            background-position: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
          }
          .name_date_container{
            margin-left: 10px;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: flex-start;
            .name{
              font-size: 15px;
              font-weight: 500;
              color: #242424;
            }
            .date{
              font-size: 13px;
              font-weight: 500;
              color: #757474;
            }
          }
        }
        .comments_description{
          width: 100%;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: flex-start;
          p{
            width: 100%;
            text-align: left;
            display: flex;
            align-items: flex-start;
            justify-content: flex-start;
          }
        }
      }
    }
  }
  .branch_container{
    width: 100%;
    height: 550px;
    margin: 20px 0;
    background-image: url("../assets/bgs/bg_branch.png");
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    .branch_label_container{
      width: 70%;
      margin-top: 20px;
      margin-bottom: 20px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      .branch_label{
        width: 100%;
        padding: 5px;
        border-bottom: 2px solid #242424;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .label{
          margin-right: 25px;
          font-size: 20px;
          font-weight: 600;
        }
        .update_number{
          font-size: 15px;
          font-weight: 500;
          color: #757474;
        }
      }
      .material_title{
        width: 100%;
        margin: 10px 0;
        font-size: 20px;
        font-weight: 500;
        display: flex;
        align-items: center;
        justify-content: flex-start;
      }
      .now_watchng{
        width: 100%;
        font-size: 15px;
        font-weight: 500;
        color: #42ABF2;
        display: flex;
        align-items: center;
        justify-content: flex-start;
      }
    }
    .branch_tree_container{
      background-color: #EEEEEE77;
      width: 70%;
      height: 400px;
      margin-bottom: 20px;
      overflow: scroll;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      .own_material{
        flex-shrink: 0;
        width: 250px;
        height: 155px;
        margin: 10px 0 0 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        .own_material_image{
          position: absolute;
          background-color: orange;
          width: 230px;
          height: 140px;
          left: 0;
          top: 0;
          box-shadow: #00000033 2px 3px 6px;
        }
        .own_material_mes{
          position: absolute;
          width: auto;
          height: 50px;
          right: 0;
          bottom: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          .left_top{
            position: absolute;
            top: 0;
            left: 0;
            width: 15px;
            height: 15px;
            border-top: 2px solid #083D61;
            border-left: 2px solid #083D61;
          }
          .right_top{
            position: absolute;
            top: 0;
            right: 0;
            width: 15px;
            height: 15px;
            border-top: 2px solid #083D61;
            border-right: 2px solid #083D61;
          }
          .right_bottom{
            position: absolute;
            bottom: 0;
            right: 0;
            width: 15px;
            height: 15px;
            border-bottom: 2px solid #083D61;
            border-right: 2px solid #083D61;
          }
          .left_bottom{
            position: absolute;
            bottom: 0;
            left: 0;
            width: 15px;
            height: 15px;
            border-bottom: 2px solid #083D61;
            border-left: 2px solid #083D61;
          }
          p{
            margin: 5;
            padding: 3px 20px;
            margin: 0 10px;
            background: transparent linear-gradient(103deg, #083D61 0%, #0F5787 45%, #105A8D 97%, #00416E 100%) 0% 0% no-repeat padding-box;
            box-shadow: 1px 1px 2px #00000029;
            border-radius: 3px;
            font-size: 20px;
            font-weight: 600;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
          }
        }
      }
      .branch_materials_cotainer{
        flex-shrink: 0;
        margin-top: 70px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        .branch_materials_row_cotainer{
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: flex-start;
          .branch_materials_container{
            margin-right: 10px;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            .branch_border_container{
              width: 150px;
              height: 140px;
              margin: 0 10px;
              display: flex;
              align-items: center;
              justify-content: center;
              position: relative;
              .top{
                position: absolute;
                width: 4px;
                height: 72px;
                background-color: #333333;
                top: 0;
              }
              .right{
                position: absolute;
                width: 77px;
                height: 4px;
                background-color: #333333;
                right: 0;
              }
              .bottom{
                position: absolute;
                width: 4px;
                height: 72px;
                background-color: #333333;
                bottom: 0;
              }
              .left{
                position: absolute;
                width: 77px;
                height: 4px;
                background-color: #333333;
                left: 0;
              }
            }
            .branch_material_mes{
              position: relative;
              cursor: pointer;
              width: 250px;
              height: 50px;
              display: flex;
              align-items: center;
              justify-content: center;
              .left_top{
                position: absolute;
                top: 0;
                left: 0;
                width: 15px;
                height: 15px;
                border-top: 2px solid #083D61;
                border-left: 2px solid #083D61;
              }
              .right_top{
                position: absolute;
                top: 0;
                right: 0;
                width: 15px;
                height: 15px;
                border-top: 2px solid #083D61;
                border-right: 2px solid #083D61;
              }
              .right_bottom{
                position: absolute;
                bottom: 0;
                right: 0;
                width: 15px;
                height: 15px;
                border-bottom: 2px solid #083D61;
                border-right: 2px solid #083D61;
              }
              .left_bottom{
                position: absolute;
                bottom: 0;
                left: 0;
                width: 15px;
                height: 15px;
                border-bottom: 2px solid #083D61;
                border-left: 2px solid #083D61;
              }
              p{
                width: 240px;
                height: 35px;
                margin: 5;
                padding: 3px 20px;
                margin: 0 10px;
                background: transparent linear-gradient(103deg, #083D61 0%, #0F5787 45%, #105A8D 97%, #00416E 100%) 0% 0% no-repeat padding-box;
                box-shadow: 1px 1px 2px #00000029;
                border-radius: 3px;
                font-size: 15px;
                font-weight: 600;
                color: #FFFFFF;
                display: flex;
                align-items: center;
                justify-content: center;
              }
              .branch_material_author{
                position: absolute;
                top: -45px;
                width: 250px;
                height: 40px;
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: center;
                .author_image{
                  background-size:contain;
                  background-repeat: no-repeat;
                  width: 40px;
                  height: 40px;
                  background-position: center;
                  border-radius: 99px;
                  margin-right: 10px;
                }
                .author_date_container{
                  display: flex;
                  flex-direction: column;
                  align-items: flex-start;
                  justify-content: center;
                  color: #757474;
                  font-size: 15px;
                  font-weight: 600;
                }
              }
            }
          }
        }
      }
    }
  }
}
</style>